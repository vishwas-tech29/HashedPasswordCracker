# HashedPasswordCracker
# 🔐 Hashed Password Cracker

A Python-based educational tool that demonstrates how dictionary attacks work on hashed passwords (e.g., MD5, SHA1, SHA256). This helps raise awareness of weak passwords and the need for strong cryptographic practices.

---

## 🧠 Features
- Supports multiple hashing algorithms: `md5`, `sha1`, `sha256`
- Takes in a hashed password and tries to crack it using a wordlist
- Includes hash generator for testing

---

## 📁 Files
- `cracker.py`: Main script for cracking
- `hash_generator.py`: (Optional) Converts plaintext to hash
- `wordlist.txt`: Sample list of common passwords
- `sample_hashes.txt`: Example test hashes

---

## ▶️ How to Run

### 1. Cracking a Password

```bash
python cracker.py

It will ask:

for the hash to crack

the hash type (md5, sha1, or sha256)

uses wordlist.txt for comparison


2. Generating a Hash (optional)
bash
Copy
Edit
python hash_generator.py

🧪 Example
Input:

yaml
Copy
Edit
Hashed password: 5f4dcc3b5aa765d61d8327deb882cf99
Algorithm: md5
Output:

pgsql
Copy
Edit
[+] Password found: password
⚠️ Disclaimer
This project is strictly for educational and ethical purposes. Never use this on systems or data you do not own or have permission to test. The goal is to educate on password security.

🧰 Future Ideas
Add multithreading for speed

GUI interface with Tkinter

Crack salted hashes

Integrate rainbow table support

📜 License
MIT License – use, modify, and share responsibly.

yaml
Copy
Edit

---

Would you like me to zip all these into a downloadable folder or generate a GitHub repository setup command?







