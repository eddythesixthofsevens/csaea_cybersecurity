# hashing: one way function. same input ---> always same output, 

import hashlib

password = "MyPasswordIsUnbreakable444"

data = password.encode("utf-8")
digest = hashlib.md5(data).hexdigest()

print(f"Password: {password}")
print(f"Hash: {digest}")
print()

diffpasswords = ["MyPasswordIsUnbreakable444" , "ILoveMonkeys300!" , "IAmCoolio68!" , "@w@y684", "a"]

for p in diffpasswords:
    ep = p.encode("utf-8")
    hp = hashlib.sha256(ep).hexdigest()
    print(f"Password: {p}\n Hash: {hp} \n")