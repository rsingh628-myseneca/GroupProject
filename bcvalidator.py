from create_blocks import File, get_blockchains, create_BlockChain
from typing import List


def validate_blockchain(create_blockchain: create_BlockChain, line: str) -> bool:
    previous_block = None
    for i, block in enumerate(create_blockchain.blocks):
        if block.previousBlockHash != "":
            expected = str(
                hash(f'{previous_block.previousBlockHash}{previous_block.data}{previous_block.randomNumber}'))
            if expected != block.previousBlockHash:
                print("Invalid previous block hash!")
                return False

        for digit in block.randomNumber:
            if digit not in block.currentBlockHash:
                print("Invalid randomNumber!")
                return False
        data = line[3 + i * 9:3 + i * 9 + 9]
        if previous_block is None:
            expected = str(hash(f'{data}{block.randomNumber}'))
        else:
            expected = str(hash(f'{previous_block.currentBlockHash}{data}{block.randomNumber}'))

        if expected != block.currentBlockHash:
            print("Invalid current block hash!")
            return False

        previous_block = block

    return True


def validate_Values(values: List[create_BlockChain], lines: List[str]) -> bool:
    if len(values) != len(lines):
        print("Invalid number of blockchains!")
        return False

    for i in range(len(values)):
        if not validate_blockchain(values[i], lines[i]):
            return False
    return True


if __name__ == '__main__':
    values = get_blockchains(File)
    with open(File) as f:
        lines = f.readlines()
        if validate_Values(values, lines):
            print("All blockchains are valid!")
        f.close()
