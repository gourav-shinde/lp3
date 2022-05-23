from Crypto.Cipher import AES
import sys

#key has to be either 16, 24 or 32 bytes
def paddedKey(key):
    while len(key) % 8 !=0:
        key +=' '
    return key
    
#text has to in multiples of 26 bytes1
def paddedText(text):
    while len(text) % 16 != 0:
        text += ' '
    return text
        
plain_input = input("Enter the text to be encrypted: ")
plain = paddedText(plain_input)
 
key_input = input("Enter in a key between 16 and 32 characters: ")
if(len(key_input)< 16 or len(key_input)> 32):
 print("key must be between 16 and 32 characters!")
 exit()
key = paddedKey(key_input)
 



IV='0123456789abcdef'
cipher = AES.new(key.encode('utf-8'),mode = AES.MODE_CBC,IV=IV.encode('utf-8'))
ciphertext = cipher.encrypt(plain.encode('utf-8'))
print(ciphertext)
 
d_cipher = AES.new(key.encode('utf-8'),mode = AES.MODE_CBC,IV=IV.encode('utf-8'))
cleartext = d_cipher.decrypt(ciphertext)
print(cleartext)