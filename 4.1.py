
def caesar_cipher_encrypt(plaintext, k):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            base = ord('A')
            new_char = chr((ord(char) - base + k) % 26 + base)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext



plaintext = 'NGUYENNGOCOANH'
k = 15

ciphertext = caesar_cipher_encrypt(plaintext, k)
print('Plaintext:', plaintext)
print('Ciphertext:', ciphertext)