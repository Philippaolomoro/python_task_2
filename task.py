import string
import random

def get_user_input():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")

    user_details = [first_name, last_name, email]
    return user_details

def password(details):
    gen_password = str(user_details[0][0:2] + user_details[1][-2:] + "".join(random.choice(string.ascii_letters for i in range(5))))
    return gen_password

status = True
container = []
employees = {}
employee_number = 1

while True:
    user_details = get_user_input()
    gen_password = password(details)
