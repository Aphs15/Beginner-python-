import random
import string

def generate_password(length=12, use_symbols=True, use_numbers=True):
    letters = string.ascii_letters  #a-z + A-Z
    digits = string.digits
    symbols = "!@#$%^&*()_+-="

    pool = letters
    if use_numbers:
        pool += digits
    if use_symbols:
        pool += symbols

    #Ensure at least one from each selected catagory
    password = [
        random.choice(letters),
        random.choice(digits) if use_numbers else None,
        random.choice(symbols) if use_symbols else None,
    ]
    password = [c for c in password if c is not None]

    #Fill the rest
    while len(password) < length:
        password.append(random.choice(pool))

    #Shuffle so required chars aren't always first
    random.shuffle(password)
    return"".join(password)

print(generate_password(16))