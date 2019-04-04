#!/bin/python3.6
#
# A Simple Password Generator written in Python

import random
import string 



def gen_pass():
    p = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    pass_len = random.randint(12, 19)
   
    print("Your generated  password is: ")
    return "".join(random.choice(p) for i in range(pass_len))

print(gen_pass())
