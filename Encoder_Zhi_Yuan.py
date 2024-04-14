
<<<<<<< Updated upstream
# Encoder Lab 9 COP3502C
=======
# Decoder Lab 9 COP3502C by Zhijie Yuan and Gabriel Wong
>>>>>>> Stashed changes

def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

# Decoder Lab 9 COP3502C
def decode(password: str) -> str:
    decoded_password = ' '
    for i in password:
        decoded = int(i) - 3
        if decoded < 0:
            decoded = decoded + 10
        decoded_password += str(decoded)
    return decoded_password

def decode(password: str) -> str:
    decoded_password = ' '
    for i in password:
        decoded = int(i) - 3
        if decoded < 0:
            decoded = decoded + 10
        decoded_password += str(decoded)
    return decoded_password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(f"Your password has been encoded and stored! Encoded password: {encoded_password}")

        elif choice == '2':
            encoded_password = input("Please enter the encoded password to decode: ")
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

