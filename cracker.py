import hashlib

def crack_password(hash_to_crack, wordlist_path, algorithm='md5'):
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            for word in file:
                word = word.strip()
                hash_func = getattr(hashlib, algorithm)
                hashed_word = hash_func(word.encode()).hexdigest()
                if hashed_word == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return
        print("[-] Password not found.")
    except FileNotFoundError:
        print(f"[!] Wordlist file '{wordlist_path}' not found.")

# Example usage
if __name__ == "__main__":
    hashed_password = input("Enter the hashed password: ").strip()
    algorithm = input("Enter hashing algorithm (md5/sha1/sha256): ").strip()
    wordlist = "wordlist.txt"
    crack_password(hashed_password, wordlist, algorithm)
