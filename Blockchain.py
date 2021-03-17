from Block import Block
from datetime import datetime


class Blockchain:
    def __init__(self):
        self.chain = []
        self.__create_genesis_block()

    def get_latest_block(self):
        """
        It returns the latest Block instance of the chain.
        :return: Block
        """
        return self.chain[- 1]

    def add_new_block(self, new_block):
        """
        Create a new Block in the Blockchain and add it last in the chain.
        :param new_block: The instance of the new Block.
        :return: Block
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        """
        Checks if the chain is valid.
        :return: Boolean
        """
        i = 1
        while i < len(self.chain):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            i += 1

        return True

    def __create_genesis_block(self):
        genesis_block = Block(index=0, timestamp=datetime.now(), data='Genesis block', previous_hash=-1)
        self.chain.append(genesis_block)
