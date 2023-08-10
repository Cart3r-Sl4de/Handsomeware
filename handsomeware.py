import os
import time
from cryptography.fernet import Fernet

lock = "      ████████████      \n    ████████████████    \n  ██████        ██████  \n  ████            ████  \n  ████            ████  \n  ████            ████  \n  ████            ████  \n  ████████████████████  \n██████████    ██████████\n████████        ████████\n████████        ████████\n██████████    ██████████\n██████████    ██████████\n██████████    ██████████\n████████████████████████\n████████████████████████\n"

def nombre():
    theNombre = input("Please enter the name you want to designate to the key file: ")
    return theNombre

#stores all the files in current directory
def filer(name):
    result = []
    for file in os.listdir():
        if file == "handsomeware.py" or file == "handsomeware.exe" or file.find("thekey.key") != -1:
            #skips the above files
            continue
        #if the file being looked at is a file, not a folder, add it to the list
        elif os.path.isfile(file):
            result.append(file)
    
    print(result)
    return result

def encryptor(check, theName):

    print("Files that were encrypted:")
    files = filer(theName)
    key = Fernet.generate_key()

    #if the key is to be generated
    if check == 256:
        #writes the cryptographic key to thekey.key
        with open(theName + "_thekey.key", "wb") as thekey:
            thekey.write(key)

    #if the key already exists
    elif check == 999:
        with open(theName + "_thekey.key", "rb") as key:
            secretkey = key.read()

    #encryptor
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        #encrypt with generated key
        if check == 256:
            contents_encrypted = Fernet(key).encrypt(contents)
        #encrypt with existing key
        elif check == 999:
            contents_encrypted = Fernet(secretkey).encrypt(contents)
        #actually encrypt the file
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

    print("KEEP THE KEY SAFE! It is your key to getting your previous files back whenever you run this program again!\nDO NOT ENCRYPT AGAIN AFTER ALREADY ENCRYPTING")
    time.sleep(20)


def decryptor(theName):

    print("Files that were decrypted:")
    files = filer(theName)

    #open the key file
    with open(theName + "_thekey.key", "rb") as key:
        secretkey = key.read()

    #encryptor
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    
    time.sleep(10)


def main():

    oops = "Either you didn't have the key file in the current folder, or you backed out.\nWhichever be the case, hope ya have a delightful day!"
    print(lock)
    oopsies = 6969

    #The start, including welcome and making sure one doesn't enter a string where one should only enter numbers
    while oopsies == 6969:
        try:
            firstCheck = int(input("\nWelcome to Handsomeware! I hope you read the readme file, but will ask, do you want to encrypt or decrypt with an existing key (enter 1)\nor do you want to encrypt and generate the key file? (enter 2).\nEnter any other number to exit:\n"))
            oopsies = 1
        except:
            print("In case you mistyped, please type a number when prompted")

    #Encryping and generating the key file for the first time
    if firstCheck == 2:
        confirmation = str(input("\nLively, then you don't have to worry about having a key file as this program will make it for you\nDo you wish to proceed with the encryption? Type Y to proceed, anything else for not\n"))
        if confirmation.lower() == "y":
            inquiry = nombre()
            encryptor(256, inquiry)
        else:
            print("Fair enough, summon me if/when you need me!")


    #Encrypting or Decrypting with existing file
    elif firstCheck == 1:
        confirmation = input("Dandy to hear! Now you need to have the key in the same folder as the one that has the files you wish to encrypt/decrypt!\nType Y to proceed and anything else if not\n")
        integrity = 0
        comedian = 69420
        inquiry = nombre()

        #this checks to make sure the key file is actually in the current directory
        for file in os.listdir():
            if file == inquiry + "_thekey.key":
                integrity = 1

        if confirmation.lower() == "y" and integrity == 1:
            while comedian == 69420:
                finalCountdown = input("\nNow for the event you have been waiting for! Do you wish to encrypt or decrypt? type E for encrypt and D for decrypt:\n")
                if finalCountdown.lower() == "e":
                    encryptor(999, inquiry)
                    comedian = 777
                elif finalCountdown.lower() == "d":
                    decryptor(inquiry)
                    comedian = 777
                else:
                    finalCountdown = input("Whether you are a comedian or mistyped accidentally, you would need to state your preference\nDo you wish to encrypt or decrypt? type E for encrypt and D for decrypt:\n")
        else:
            print(oops)
            time.sleep(10)
    else:
        print("You either backed out or mistyped. Either way, summon me if thou require my assistance!")
        time.sleep(10)


main()
#the thing of nightmares: for root, dir, files in os.walk(search_path)