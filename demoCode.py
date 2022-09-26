import hashlib

# Hashing plain text, here "Cohealth" is the plain text

print(hashlib.sha224("Cohealth".encode()).hexdigest())

# Same as previous, but with salting.
# Here "HAsnoiqHEh" is the salt

print(hashlib.sha224("CohealthHAsnoiqHEh".encode()).hexdigest())

# Looking up Passwords from the file. Here the salt is added to the 0th and last position

def hashit(hash):
    result = hashlib.sha224(hash.encode())
    #if (result.hexdigest() == hash):
    return result.hexdigest()

hash = hashlib.sha224("CohealthHAsnoiqHEh".encode()).hexdigest()
with open('top-passwords.txt') as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        with open('known-salts.txt') as foo:
            for salt in foo.readlines():
                salt = salt.replace("\n", "")
                psaltedLine = salt + line 
                AsaltedLine = line + salt
                if(hashit(psaltedLine) == hash or hashit(AsaltedLine) == hash):
                    print(line)