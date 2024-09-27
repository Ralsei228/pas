
import random
import string


def gen_pass(length):
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    
    return password

print(gen_pass(12))  
