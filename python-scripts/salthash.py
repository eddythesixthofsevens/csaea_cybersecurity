import hashlib
import os

plaintext_password = "MonkeysRKule"
password = plaintext_password.encode("utf-8")

#1 no salt: two users, same password -> identical hashes (easy to spot/crack)
hash_a = hashlib.sha256(password).hexdigest()
hash_b = hashlib.sha256(password).hexdigest()

print("No salt.")
print("Hash A: ", hash_a)
print("Hash_B: ", hash_b)

# Salt. Each user gets their own salt.

salt_a = os.urandom(16)
salt_b = os.urandom(16)

print(f"User A Salt: {salt_a}")
print(f"User B Salt: {salt_b}")

salthash_a = hashlib.sha256(salt_a + password).hexdigest()
salthash_b = hashlib.sha256(salt_b + password).hexdigest()

print("\nWith salt.")
print(f"User A Hash: {salthash_a}")
print(f"User B Hash: {salthash_b}")