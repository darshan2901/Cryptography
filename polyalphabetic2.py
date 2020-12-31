import string

plaintext = ""
key = "joy"
cipher = "jpfrgct"

index = 0

for c in cipher:
    if c in string.ascii_lowercase:
        offset = ord(key[index]) - ord('a')
        positive_offset = 26 - offset

        decrypted_c = chr((ord(c) - ord('a') + positive_offset) % 26 + ord('a'))

        plaintext += decrypted_c
        index = (index + 1) % len(key)

    else:
        plaintext += c

print("cipher : " + cipher)
print("plain : " + plaintext)