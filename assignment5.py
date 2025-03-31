from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)


class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(data)


# Example usage
text_handler = TextFileHandler("example.txt")
text_handler.write("Hello, World!")
print(text_handler.read())

binary_handler = BinaryFileHandler("example.bin")
binary_handler.write(b"Binary Data")
print(binary_handler.read())