import random
import string

class StringGenerator():
    '''
    Handles string generation and validation
    ''' 
    def generate(self, length: int, upper: bool, numbers: bool, specials: bool):
        '''
        Generates a random string
        
        length: int
        upper: bool
        numbers: bool
        specials: bool
        '''
        special_chars = '!#$%&*?@^'

        available_chars = string.ascii_lowercase
        if upper: available_chars += string.ascii_uppercase
        if numbers: available_chars += string.digits
        if specials: available_chars += special_chars

        return ''.join(random.choice(available_chars) for _ in range(length))


    def validate(self, input: str, upper: bool, numbers: bool, specials: bool):
        '''
        Validates string wiht constraints
        '''
        has_upper = False
        has_number = False
        has_special = False
        for char in input:
            if not has_upper:
                has_upper = char.isupper()
            if not has_number:
                has_number = char.isdecimal()
            if  not has_special:
                has_special = True if char in '!#$%&*?@^' else False

        if has_upper == upper and has_number == numbers and has_special == specials:
            return True
        else:
            return False
