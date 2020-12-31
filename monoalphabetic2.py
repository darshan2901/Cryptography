import string

plaintext = "my name is darshan"
key = "qwertyuiopasdfghjklzxcvbnm"
cipher = " "

for c in plaintext:
    if c in string.ascii_lowercase:
        index = ord(c) - ord('a')
        cipher += key[index]
    else:
        cipher = cipher + c


print("plain : " + plaintext)
print("cipher : " + cipher)