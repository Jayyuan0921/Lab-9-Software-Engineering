# Decoder Lab 9 COP3502C

def decode(password: str) -> str:
    decoded_password = ' '
    for i in password:
        decoded = int(i) - 3
        if decoded < 0:
            decoded = decoded + 10
        decoded_password += str(decoded)
    return decoded_password
