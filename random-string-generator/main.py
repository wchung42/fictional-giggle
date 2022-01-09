import random

def generate_string(length: int, upper: bool, number: bool, special: bool):
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    specials = '!#$%&*?@^'

    available_chars = alpha_lower
    if upper: available_chars += alpha_upper
    if numbers: available_chars += numbers
    if special: available_chars += specials

    result = ''
    for _ in range(length):
        result += random.choice(available_chars)
    
    return result

print(generate_string(15, upper=True, number=True, special=True))