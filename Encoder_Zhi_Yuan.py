
# Encoder Lab 9 COP3502C

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





