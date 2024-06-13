# morse code dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ':': '---...',
                   ' ': ' '}

#variable allows while loop to run
run = True


# function used to get the keys from the morse code dictionary based on the values
def get_key(val):
    for key, value in MORSE_CODE_DICT.items():
        if val == value:
            return key


def encrypt():
    # user input is requested to convert to morse code
    # input is saved in a variable and converted to lower case letters
    message = str(input("\nPlease input a message that you would like to convert to morse code.\n")).upper()

    # each element of the users input is looped through and searched for in the dictionary
    # The element is then added to the morse_message variable

    encypted_message = ""
    for element in message:
        encypted_message += f"{MORSE_CODE_DICT.get(element)} "

    # the morse code is then printed out to the console
    print(f"{encypted_message}\n")


def decrypt():
    # user morse code input is requested to decrypt to plain text
    # message is saved as a variable
    message = str(input("\nPlease input a message that you would like to convert from morse code to plain text.\n"))

    # each element is looped through and searched for in the dictionary and key is found that matches
    # element conversion is then added to the decrypted message variable
    decrypted_message = ""

    # get keys function is called to pull the plain letter keys from the dictionary using the morse code values
    for element in message.split(" "):
        if get_key(element) == None:
            decrypted_message += " "
        else:
            decrypted_message += f"{get_key(element)}"

    print(f"{decrypted_message}\n")


# menu function to allow user to select whether they want to encrypt or decrypt a message
def menu():
    global run
    print("Would you like to encrypt to morse code or decrypt a message to plain text?")
    function_choice = str(input("Type 1 to encrypt.\nType 2 to decrypt.\nType 3 to end the program.\n-"))
    if function_choice == "1":
        encrypt()
    elif function_choice == "2":
        decrypt()
    elif function_choice == "3":
        run = False
    else:
        print("please select from the available options below\n\n")
        menu()


while run:
    menu()
    if not run:
        break
