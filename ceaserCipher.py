def encrypt(message):
    ceaserMessage = ''
    for i in range(0, len(message)):
        asciiVal = ord(message[i])
        if(asciiVal > 64):
            ceaserMessage += chr(asciiVal+3)
    print("This is the encoded message -> " + ceaserMessage)

def decrypt(message):
    ceaserDecrypt = ''
    for i in range(0, len(message)):
        asciiVal = ord(message[i])
        if(asciiVal > 64):
            ceaserDecrypt += chr(asciiVal-3)
    print("This is the decoded message -> " + ceaserDecrypt)

def main():
    while(1):
        print("Welcome to the ceaser cipher encoder!")
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
