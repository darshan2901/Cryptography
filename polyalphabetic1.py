import string

plaintext = "abhisek"
key = "joy"
cipher = ""

index = 0

for c in plaintext:
    if c in string.ascii_lowercase:
        offset = ord(key[index]) - ord('a')

        encrypted_c = chr((ord(c) - ord('a') + offset )% 26 + ord('a'))
        cipher += encrypted_c

        index = (index + 1 )%len(key)
    else:
        cipher += c

print("plain : " + plaintext)
print("cipher : " + cipher)

