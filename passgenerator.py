import random
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`'

length = int(input("Enter the length of the your password: "))
if length >= 30:
    print("Length may not work on some websites. Make sure to check the website's password requirements.")
def generate_random_string(length):
    result = ''
    for i in range(length):
        result += random.choice(characters)
    return result
print(generate_random_string(length))
