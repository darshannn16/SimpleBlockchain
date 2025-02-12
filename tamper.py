from blockchain import Blockchain

bc = Blockchain()
bc.add_block("Transaction 1")
bc.add_block("Transaction 2")

print("Original Blockchain:")
bc.print_chain()

# Simulating tampering
bc.chain[1].transactions = "Hacked Transaction"

print("\nAfter Tampering:")
print("Blockchain Valid?" if bc.is_chain_valid() else "Blockchain Corrupted!")
