def menu_options():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quiz\n")


def encoder(password):
    encoded = ""
    for num in password:
        number = int(num) + 3
        encoded += str(number)
    return encoded


if __name__ == "__main__":
    menu_options()
    option = int(input("Please enter an option: "))

    while True:
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_num = encoder(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            pass
        if option == 3:
            break