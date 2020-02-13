import os
import pyAesCrypt

bufferSize = 64 * 1024
password = "12345"

for root, dirs, files in os.walk("/home/golcatlman/PycharmProjects/"
                                 "RansomeWare/Encrypted_Data/"):
    for file in files:
        if file.endswith(".dogma"):  # The arg can be a tuple of suffixes to look for

            # Get Dogma file
            unique_file = os.path.join(file)

            # Get Unique path
            unique_path = os.path.join(root + "/")

            # Reformat .dogma file
            format_file = unique_file[:-5]
            print(unique_path + file)

            # Decrypt file
            pyAesCrypt.decryptFile(unique_path + file,
                                   unique_path + format_file, password,
                                   bufferSize)
            os.remove(unique_path + file)
