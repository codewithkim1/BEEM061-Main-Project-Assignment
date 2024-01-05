import requests

# Replace 'block_height' with the actual block height you want to explore
block_height = 825811

# Fetch data from the whatsonchain API
api_url = f'https://api.whatsonchain.com/v1/bsv/main/block/height/{block_height}'
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    block_data = response.json()

    # Extract required information
    height = block_data.get('height')
    timestamp = block_data.get('timestamp')
    difficulty = block_data.get('difficulty')
    merkle_root = block_data.get('merkleroot')
    transactions = block_data.get('txcount')
    version = block_data.get('version')
    chainwork = block_data.get('chainwork')
    total_fee = block_data.get('totalFees')
    nonce = block_data.get('nonce')
    miner = block_data.get('miner')
    average_fee = block_data.get('fee')
    bits = block_data.get('bits')
    size = block_data.get('size')
    confirmations = block_data.get('confirmations')

    # Print the extracted information
    print(f"Height: {height}")
    print(f"Timestamp (UTC): {timestamp}")
    print(f"Difficulty: {difficulty}")
    print(f"Merkle Root: {merkle_root}")
    print(f"Transactions: {transactions}")
    print(f"Version: {version}")
    print(f"Chainwork: {chainwork}")
    print(f"Total Fee: {total_fee}")
    print(f"Nonce: {nonce}")
    print(f"Miner: {miner}")
    print(f"Average Fee: {average_fee}")
    print(f"Bits: {bits}")
    print(f"Size: {size} MB")
    print(f"Confirmations: {confirmations}")

else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
