def encrypt(message):
    caeserMessage = ''
    for i in range(0, len(message)):
        asciiVal = ord(message[i])
        if(asciiVal > 64):
            caeserMessage += chr(asciiVal+3)
    print("This is the encoded message -> " + caeserMessage)

def decrypt(message):
    caeserDecrypt = ''
    for i in range(0, len(message)):
        asciiVal = ord(message[i])
        if(asciiVal > 64):
            caeserDecrypt += chr(asciiVal-3)
    print("This is the decoded message -> " + caeserDecrypt)

def main():
    while(1):
        print("Welcome to the caeser cipher encoder!")
        choice = input("Do you want to encrypt or decrypt?")
        if(choice == 'encrypt'):
            message = input("Please enter the message you wish to be encoded ")
            encrypt(message)
        elif(choice == 'decrypt'):
            message = input("Please enter the message you wish to be decoded ")
            decrypt(message)
        elif(choice == 'no'):
            print("Goodbye")
            quit()
        else:
            print("Please enter either encrypt or decrypt")

main()
