#Create a python program that generates a strong random password.
#The user will enter the length of the password , and your program should create a mix of letters,
#numbers and symbols.

#Use python's random and secrets module to pick characters randomly.
#This task helps you understand loops ,string handling and how to work with python's built-in modules

import random
import string

length=int(input("Enter password length : "))
letters=string.ascii_letters    # It contain letter
numbers=string.digits       # It contain digit
symbols=string.punctuation  # It contain symbol

password=""     #create for store password

# use for loop
for i in range(length):
    password+=random.choice(letters+numbers+symbols)

print(password)


