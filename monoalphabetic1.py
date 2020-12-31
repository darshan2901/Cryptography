import string
key = "qwertyuiopasdfghjklzxcvbnm"
cipher = "dn fqdt ol rqkliqf"
plaintext = ""

for c in cipher:
    if c in string.ascii_lowercase:
        index = key.find(c)
        plaintext += chr(index + ord('a'))
    else:
        plaintext += c

print("cipher : " + cipher)
print("plain :" + plaintext)
