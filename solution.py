import hashlib


def hashit(hash):
    result = hashlib.sha224(hash.encode())
    return result.hexdigest()


hash = "343cfcf0df92d5c8f19e24b3ac4a70516dc23efa59650f453c028c9b"

with open('top-passwords.txt') as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        with open('known-salts.txt') as foo:
            for salt in foo.readlines():
                salt = salt.replace("\n", "")
                psaltedLine = line[0:2] + salt + line[2:]
                psaltedLine = psaltedLine[0:3] + salt + psaltedLine[3:]
                psaltedLine = salt + psaltedLine
                psaltedLine = psaltedLine + salt
                if(hashit(psaltedLine) == hash):
                    print(line)
