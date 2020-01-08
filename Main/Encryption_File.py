import pyAesCrypt
import os
from os import path

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "12345"

# User input
print("# e - For encrypt")
print("# d - For Dencrypt")
user_input = input("")

# encrypt
if user_input == "e":
    if path.exists("Encrypted_Data/Data_To_Encrypt.txt"):
        pyAesCrypt.encryptFile("Encrypted_Data\Data_To_Encrypt.txt", "Encrypted_Data\Data_To_Encrypt.aes", password, bufferSize)
        os.remove("Encrypted_Data/Data_To_Encrypt.txt")
    else:
        print("File Not Exist")

# decrypt
if user_input == "d":
    if path.exists("Encrypted_Data/Data_To_Encrypt.aes"):
        password_user_input = input("Type Password to Decrypt: ")
        try:
            pyAesCrypt.decryptFile("Encrypted_Data\Data_To_Encrypt.aes", "Encrypted_Data\Decrypted.txt", password, bufferSize)
        except ValueError:
            print("Password Error [!]")