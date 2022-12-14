# Code-Wars-2.0-Round-3-Starter-code
Starter code for Code Wars 2.0 Round 3, Decipher the Code

    There are a total of 4 salts to be added to the Plain-text before hashing. The Position of salts are below in the code block(same as this). Answer the question to decrypt the position and find the position.
    The salts need to be added in the same order as hints.

---
## The hash
        343cfcf0df92d5c8f19e24b3ac4a70516dc23efa59650f453c028c9b
---
### Hint 1
Substitute the Alphabets (It's Simple, for eg A->E, B -> J, etc.)

        SNV
---

From here, the salt postions are [encrypted](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). To decrypt the position 
- Find the answer for the question,
- go to  https://cryptii.com/pipes/vigenere-cipher
- Set it to decode mode (in the middle card)
- Paste the below hash on the left side
- Enter your answer in the "KEY" attribute
- You should have the salt position on the right

---
### Hint 2
- The Encryption Standard written by IBM, which competed with Rijndael to become AES.

        fhvltiivbojafiff
---
### Hint 3
- An Algorithm discovered in the 90s, which not only proves its new computing strategy, but also broke public-key cryptography schemes which run the internet today.

        rlfflo

---
### Hint 4
- Nick name of the exploit which compromised windows systems, where the user password’s hash and its key was stored in the memory. This was used heavily in the initial years of international ransomware attacks.

        xieb


# The Solutions
## Solution for Hint 1
The first Hint was given as ```SNV``` but its actually ```SVN```. To compensate this error, points will be allocated to teams which came close to solving it/spent a lot of time on it (as observed by the organizers)
<br>

So the answer will work out to ```TWO``` (By shifting each letter one step ahead, S -> T, V -> W, N -> O) <br>

## Solution for Hint 2
 The Key is ```MARS```
- https://en.wikipedia.org/wiki/Advanced_Encryption_Standard_process
- https://en.wikipedia.org/wiki/MARS_(cipher)

So the solution will work out to ```thethirdposition```
## Solution for Hint 3
The Key is ```Shor```
- https://en.wikipedia.org/wiki/Shor%27s_algorithm

So the solution will work out to ```zeroth```
## Solution for Hint 4
The Key is ```Mimikatz```
- https://en.wikipedia.org/wiki/Mimikatz#History

So the solution will work out to ```last```

---
# The Final Plain Text is ```Tesladock```