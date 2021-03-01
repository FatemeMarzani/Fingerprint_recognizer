import pickle

class BinaryReader(object):
    """ A helper for storing objects as file and visa versa
    """
    
    def read(path: str) -> any:
        with open(path, 'rb') as inf:
            return pickle.load(inf)
    
    def write(data: any, path: str) -> None:
        with open(path, 'wb') as outfile:
            pickle.dump(data, outfile)