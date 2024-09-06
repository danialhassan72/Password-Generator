#Password Generator

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','+']

password = ""
print("welocme to the 3Password Generator!")
na_letters = int(input("how many letters would you like to add in password? \n"))
na_symbols = int(input("how many symbols would you like to add in password? \n"))
na_numbers = int(input("how many numbers would you like to add in password? \n"))

for char in range (1,na_letters + 1):
    password = random.choice(letters)
for char in range (1,na_numbers + 1):
    password += random.choice(numbers)
for char in range(1,na_symbols + 1):
    password += random.choice(symbols)

print(password)
print("".join(random.sample(password, len(password))))
