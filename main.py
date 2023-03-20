# Chloe Lai Lab 06
def menu_options():
    # function that contains the menu options
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quiz\n")


def encoder(password):
    # encodes the password
    encoded = ""
    for num in password:
        if int(num) <= 6:
            # if number is less than or equal to 6, integer 3 will be added
            number = int(num) + 3
        else:  # numbers greater than six will only have the last digit encoded
            number = int(num) + 3
            number = str(number)[1]
        encoded += str(number)  # add the encoded numbers into a string
    return encoded


# function added by McKenzie Todd
def decoder(string_data):
    decoded = ""
    # runs through each number in the string
    for num in string_data:
        # converts num from a string to an integer
        num = int(num)
        if num >= 3:
            num -= 3
        elif num == 2:
            num = 9
        elif num == 1:
            num = 8
        elif num == 0:
            num = 7
        # converts num back to a string
        decoded += str(num)
    return decoded



if __name__ == "__main__":
    while True:
        # loop continues until the user wants to exit the program
        menu_options()
        option = int(input("Please enter an option: "))

        if option == 1:  # allows user to put in password and encode it
            password = input("Please enter your password to encode: ")
            encoded_num = encoder(password)
            print("Your password has been encoded and stored!\n")
        if option == 2:
            # decodes the user's encoded_num
            decoded_num = decoder(encoded_num)
            # prints the encoded and decoded passwords
            print(f"The encoded password is {encoded_num}, and the original password is {decoded_num}.")
            print()
        if option == 3:  # exits loop if user wants to exit the program
            break