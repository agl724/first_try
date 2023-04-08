# PASSWORD GENERATOR---------------------do not remove this #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*']
print("Welcome to Pari's Password Generator!")
nr_ltrs = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

#easy level - letter-symbol-number-------------do not remove this #
# password = ""
# for char in range(1, nr_ltrs + 1):
#     password += random.choice(letters)
#
# for sym in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for num in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# print("Here is your password: ", password)

#hard level - random order --------------------------do not remove this #
password_list = []
for char in range(1, nr_ltrs + 1):
    password_list += random.choice(letters)

for sym in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
sample = ""
for fun in password_list:
    sample += fun
print("Here is your password: ", sample)
