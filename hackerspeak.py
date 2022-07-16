import json 
from random import randint

class LeetSpeak:
    leetspeak = {chr(65+i):[] for i in range(26)}
    
    def __init__(self):
        with open("dictionary.txt") as _file:
            for line in _file.read().strip().split('\n'):
                line = line.split()

                for item in line[1:]:
                    self.leetspeak[line[0]].append(item)

        self.generateDecoder()

    def printCodePage(self):
        for key, val in sorted(self.leetspeak.items(), key = lambda x: x[0]):
            print(key, val)

    def encode(self, text):
        result = ""

        for letter in text:
            if letter.isalpha():
                letter = letter.upper()
                result += self.leetspeak[letter][randint(1,100) % len(self.leetspeak[letter])]
            elif letter == ".":
                result += "!"
            else:
                result += letter
            result += "."

        return result

    def generateDecoder(self):
        self.decoder = []
        self.reverseEncoding = {}
        count = 0
        for key, values in self.leetspeak.items():
            for val in values:
                self.decoder.append(val)
                self.reverseEncoding[val] = key
                count += 1

        self.decoder.sort(key = lambda x: len(x), reverse = True)

        if self.sanityCheck() != True:
            raise Exception("Not going to be able to decode the encoded message. Conflicting symbols!")

    def sanityCheck(self):   
        return len(set(self.decoder)) == len(self.decoder)

    def decode(self, encodedText):
        decoded = ""

        for word in encodedText.split():
            for encoded in word.split("."):
                if encoded in self.decoder:
                    decoded += self.reverseEncoding[self.decoder[self.decoder.index(encoded)]].lower()
                else:
                    decoded += encoded
            decoded += " "

        return decoded

if __name__ == "__main__":
    translation = LeetSpeak()
    #translation.printCodePage()
    #print(translation.decoder)
    
    example = """- For those cyber noobs that aren't down with the NSA, OR just don't care about learning disassembly of programs.
- This is a basic function parser that can be used with Python and C.
- Currently, it does not support classes. This is in the works."""

    print(translation.decode(translation.encode(example)))
