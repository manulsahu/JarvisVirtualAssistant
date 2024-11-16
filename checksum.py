import hashlib

def calculate_checksum(file_path):
    """Calculate SHA-256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Replace 'your_main_script.py' with the actual path of your main script
file_path = "enhancedkw.py"
print("Checksum for file:", calculate_checksum(file_path))
