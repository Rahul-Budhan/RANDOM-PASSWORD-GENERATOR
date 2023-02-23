import random

print("Welcome to your password generator")

chars = 'abcdefghijklmnopqrstuzwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?:}{/}+_-'

number = input("Amount of passwords to generate")
number = int(number)

length = input("Input your password length")
length = int(length)

print("\nhere are your passwords: ")

for password in range(number):
    passwords = ''
    for c in range(length):
        passwords+= random.choice(chars)
    print(passwords)