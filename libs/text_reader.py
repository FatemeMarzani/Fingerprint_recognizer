from typing import Iterable

class TextReader(object):
    def read(path: str) -> str:
        file = open(path, 'r')
        return file.read()

    def write(data: str, path: str) -> None:
        file = open(path, 'w')
        file.write(data)

    def write_lines(data: Iterable[str], path: str) -> None:
        file = open(path, 'w')
        file.writelines(data)