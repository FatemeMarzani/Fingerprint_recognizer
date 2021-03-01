from typing import Iterable
from libs.binary_reader import BinaryReader
from libs.pcap_reader import PcapReader


class FingerprintRecognizer(object):
    """
    """

    def __init__(self, flows: dict, symbols: dict):
        self.flows = flows
        self.symbols = symbols
        self.symbol_sequence: dict
    
    def recognize(self):

        # 1: Split flows into batches
        
        # 2: Generate cluster of destinations
        pass

    def get_symbols(self) -> dict:
        return self.symbols

    def get_symbol_sequences_per_app(self) -> dict:
        return self.symbol_sequences_per_app;

