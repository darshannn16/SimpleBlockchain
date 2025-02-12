import hashlib
import datetime

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                return False  

            if current_block.previous_hash != previous_block.hash:
                return False  

        return True

    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index} | Hash: {block.hash} | Prev Hash: {block.previous_hash} | Transactions: {block.transactions}")

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("Transaction 1")
    blockchain.add_block("Transaction 2")

    print("Blockchain:")
    blockchain.print_chain()

    print("\nBlockchain Valid?", blockchain.is_chain_valid())
