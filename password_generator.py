import string
import random


def generate(length, min_upper, min_digit, min_symbol):
    min_lower = length - min_symbol - min_digit - min_upper

    lowers = random.choices(string.ascii_lowercase, k=min_lower)
    uppers = random.choices(string.ascii_uppercase, k=min_upper)
    digits = random.choices(string.digits, k=min_digit)
    symbols = random.choices(string.punctuation, k=min_symbol)

    pswd = lowers + uppers + digits + symbols

    return ''.join(random.sample(pswd, len(pswd)))


if __name__ == '__main__':
    length = int(input("Length of Password: "))
    min_upper = int(input("Minimum number of upper case characters: "))
    min_digit = int(input("Minimum number of digits: "))
    min_symbol = int(input("Minimum number of symbols: "))

    print(generate(length, min_upper, min_digit, min_symbol))
