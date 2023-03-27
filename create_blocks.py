from random import randint
from typing import List

File = 'sampleData.txt'


class part:
    PREVIOUS_BLOCK_HASH = ""
    FULL_PREVIOUS_BLOCK = ""

    def __init__(self, data: str):
        self.previousBlockHash = part.PREVIOUS_BLOCK_HASH
        self.fullPreviousBlock = part.FULL_PREVIOUS_BLOCK

        self.data = data
        self.randomNumber = None
        self.currentBlockHash = None

        # Generate random number and hash
        self._generateRandomNumber()

        # Update the static variable PREVIOUS_BLOCK_HASH and FULL_PREVIOUS_BLOCK
        part.PREVIOUS_BLOCK_HASH = self.currentBlockHash
        part.FULL_PREVIOUS_BLOCK = self.__str__()

    def _generateRandomNumber(self) -> None:
        while True:
            self.randomNumber = str(randint(10000, 99999))
            self.currentBlockHash = str(hash(str(self.previousBlockHash) + self.data + self.randomNumber))

            all_in_hash = True
            for digit in self.randomNumber:
                if digit not in self.currentBlockHash:
                    all_in_hash = False
                    break

            if all_in_hash:
                break

    def __str__(self):
        return f'{self.previousBlockHash}{self.data}{self.randomNumber}{self.currentBlockHash}'


class create_BlockChain:
    def __init__(self, name):
        part.FULL_PREVIOUS_BLOCK = ""
        part.PREVIOUS_BLOCK_HASH = ""
        self.name = name
        self.blocks = []
        self.size = 0

    def add_block(self, data: str) -> None:
        self.blocks.append(part(data))
        self.size += 1

    def __str__(self):
        res = f'{self.name} blockchain ({self.size} blocks)\n'
        for block in self.blocks:
            res += f'PH: {block.previousBlockHash}\n'
            res += f'D: {block.data}\n'
            res += f'RN: {block.randomNumber}\n'
            res += f'CH: {block.currentBlockHash}\n'
            res += '\n'
        return res


def create_blockchain(semester: str) -> create_BlockChain:

    if len(semester) != 50:
        print("Invalid semester data, the length must be 50.")
        return None

    # S1,5,COM111|075,OPS110098,ULI101076ENG100055MTH10108700
    # S1, 5, COM111
    semester_number = semester[:2]
    number_of_course = int(semester[2])

    # Create a blockchain
    blockchain = create_BlockChain(semester_number)
    for i in range(3, 3 + number_of_course * 9, 9):
        course = semester[i:i + 9]
        blockchain.add_block(course)
    return blockchain


def get_blockchains(file: str) -> List[create_BlockChain]:
    values = []
    with open('sampleData.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            value = create_blockchain(line)
            values.append(value)
    return values


if __name__ == '__main__':
    blocks = get_blockchains(File)
    for block in blocks:
        print(block)
        print('=' * 36)
