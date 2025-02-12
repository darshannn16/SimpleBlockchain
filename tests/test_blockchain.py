import unittest
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.bc = Blockchain()
    
    def test_blockchain_validity(self):
        self.bc.add_block("Transaction 1")
        self.bc.add_block("Transaction 2")
        self.assertTrue(self.bc.is_chain_valid())

if __name__ == "__main__":
    unittest.main()
