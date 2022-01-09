import random
import string

def string_generator(length: int, upper: bool, numbers: bool, specials: bool):
    special_chars = '!#$%&*?@^'

    available_chars = string.ascii_lowercase
    if upper: available_chars += string.ascii_uppercase
    if numbers: available_chars += string.digits
    if specials: available_chars += special_chars

    print(available_chars)
    
    return ''.join(random.choice(available_chars) for _ in range(length))
