import pyDes


data = input("Please enter plain text for encryption:")
keystring=input("Enter 16/24 byte string for key generation:")
k = pyDes.triple_des(keystring, padmode=pyDes.PAD_PKCS5)
e = k.encrypt(data)
print ("cipher text: %r" % e)
#%r to be useful for printing a string of unknown encoding
print ("plain text: %r" % k.decrypt(e))

print("encrypted text: ")
print(e)





































# For Python3, you'll need to use bytes, i.e.:
#key  -> Bytes containing the encryption key. 8 bytes for DES, 16 or 24 bytes
#	 for Triple DES
#mode -> Optional argument for encryption type, can be either pyDes.ECB
#	(Electronic Code Book), pyDes.CBC (Cypher Block Chaining)
#IV   -> Optional Initial Value bytes, must be supplied if using CBC mode.
#	 Must be 8 bytes in length.
#pad  -> Optional argument, set the pad character (PAD_NORMAL) to use
#	 during all encrypt/decrypt operations done with this instance.
#padmode -> Optional argument, set the padding mode (PAD_NORMAL or
#	 PAD_PKCS5) to use during all encrypt/decrypt operations done
#	 with this instance.