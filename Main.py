import AESEncryptDecrypt as AES
import RandomFileGenerator as RFG
import FileOpener as FO
import subprocess


AES.write_key() # creates as AES key file
key = AES.load_key() # loads AES key present in key file


flag = True # set flag as True
while flag:
    filename = input("Enter the name of the file to be encrypted: ")
    filedata1 = FO.file_read(filename)
    opt = input("Do you want to open the file? ")
    if opt == "yes":
        print("printing the filedata of the un-encrypted file: ....\n",filedata1)
        subprocess.call(('open', filename)) # opens the file in its default application
    AES.encrypt(filename, key) # encrypting the file with the key
    filedata2 = FO.file_read("encrypted"+filename)
    opt = int(input("Enter 1 to open the encrypted file else 0 to not open the encrypted file: "))
    if opt == 1:
        print("printing the filedata of the encrypted file: ....\n",filedata2)
        subprocess.call(('open', "encrypted"+filename)) # opens the file in its default application
    AES.decrypt("encrypted"+filename, key) # decrypting the file with the key
    filedata3 = FO.file_read("newdecryptedencrypted"+filename)
    opt = input("Do you want to open the decrypted file? ")
    if opt == "yes":
        print("printing the filedata of the un-encrypted file: ....\n",filedata3)
        subprocess.call(('open', "newdecryptedencrypted"+filename)) # opens the file in its default application
    opt = input("Do you want to continue? ")
    if opt == "yes":
        flag = True
    else:
        flag = False
