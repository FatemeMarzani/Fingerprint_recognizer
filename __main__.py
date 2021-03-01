import argparse
from libs.text_reader import TextReader
from libs.pcap_reader import PcapReader
from libs.binary_reader import BinaryReader
from fingerprint_recognizer import FingerprintRecognizer
from pathlib import Path


# TODO: change lists to dictionary
def run(pcaps_paths=[], flows_paths=[], write_flows_dir='', symbols_path='', out_dir=''):
    # Phase 1: Read flows from pcap file or binary file
    flows_dict = dict()
    if flows_paths:
        flows_dict = dict([(Path(p).stem, BinaryReader.read(p)) for p in flows_paths])
    elif pcaps_paths:
        flows_dict = dict([(Path(p).stem, PcapReader.read(p)) for p in pcaps_paths])
    else:
        raise Exception("There is no input file specified")

    # Phase 2: Save flows as binary if output path is speficied
    if write_flows_dir:
        for key, value in flows_dict.items():
            BinaryReader.write(value, write_flows_dir + '/' + key + '.p')

    # Phase 3: Load previously saved symbols set
    symbols_set = {}
    if symbols_path:
        symbols_set = BinaryReader.read(symbols_path)

    # Phase 4: Generate sequence of symbols based on symbols set and flows
    # IT IS THE MAIN PART OF APPLICATION
    # REST ARE ALL ABOUT MANAGING INPUTS AND OUTPUTS
    fingerprint_recognizer = FingerprintRecognizer(flows_dict, symbols_set)
    fingerprint_recognizer.recognize()

    # Phase 5: Save set of unique symbols to use in the future
    if symbols_path:
        symbols_set = fingerprint_recognizer.get_symbols()
        BinaryReader.write(symbols_set, symbols_path)

    # Phase 6: Save generated sequence of symbols
    if out_dir:
        symbol_sequences_per_app = fingerprint_recognizer.get_symbol_sequences_per_app()
        # Each symbol sequence is a dictionary which has two keys: app, symbols
        # app: unique id of 
        for symbol_sequence in symbol_sequences_per_app.items():
            TextReader.write_lines(symbol_sequence['symbols'], out_dir + '/' + symbol_sequence['app'] + '.txt')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""FingerprintRecognizer: 
        Fingerprint recognition of applications on the network environment by integrating machine and automata learning methods"""
    )

    # Flow data input/output agruments
    group_data_in = parser.add_argument_group("Flow data input/output")
    group_data_in.add_argument('-rp', '--pcaps_paths', type=str, nargs='+')
    group_data_in.add_argument('-rf', '--flows_paths', type=str, nargs='+')
    group_data_in.add_argument('-wf', '--write_flows_dir', type=str)
    group_data_in.add_argument('-s', '--symbols_path', type=str)
    group_data_in.add_argument('-o', '--out_dir', type=str)

    args = parser.parse_args()
    run(**vars(args))
