from Block import Block
from Blockchain import Blockchain
from datetime import datetime

if __name__ == '__main__':
    # print_hi('PyCharm')
    block_chain = Blockchain()
    block_chain.add_new_block(Block(1, datetime.now(), 'Block #1'))
    block_chain.add_new_block(Block(2, datetime.now(), 'Block #2'))

    print('Is the block chain valid?', block_chain.is_chain_valid())  # Is the block chain valid? True

    i = 1
    block_chain.chain[i].data = 'anything could be entered here'  # Try to change a block and recalculate all the hashes after that...

    print('Is the block chain valid?', block_chain.is_chain_valid())  # Is the block chain valid? False
    while i < len(block_chain.chain) - 1:
        block_chain.chain[i].hash = block_chain.chain[i].calculate_hash()
        block_chain.chain[i + 1].previous_hash = block_chain.chain[i].hash
        i += 1

    print('Is the block chain valid?', block_chain.is_chain_valid())  # Is the block chain valid? False
