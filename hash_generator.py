import hashlib

def generate_hash(plain_text, algorithm='md5'):
    hash_func = getattr(hashlib, algorithm)
    hashed = hash_func(plain_text.encode()).hexdigest()
    print(f"{algorithm.upper()} Hash of '{plain_text}': {hashed}")

# Example usage
if __name__ == "__main__":
    text = input("Enter text to hash: ")
    algo = input("Enter algorithm (md5/sha1/sha256): ")
    generate_hash(text, algo)
