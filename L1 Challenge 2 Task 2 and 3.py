import random


def reverse_name(name):
    return name[::-1]


def intersperse_name(firstname, surname):
    rev1 = reverse_name(firstname)
    new_word = ""
    count = 0
    if len(rev1) >= len(surname):
        for i in range(0, len(surname)):
            new_word += rev1[i]+surname[i]
            count += 1
        new_word += rev1[count:]
    elif len(rev1) < len(surname):
        for i in range(0, len(rev1)):
            new_word += rev1[i]+surname[i]
            count += 1
        new_word += surname[count:]
    return new_word


def format_name(first_name, surname):
    intersperse = intersperse_name(first_name, surname)
    division = len(intersperse)//2
    return intersperse[:division].capitalize(), intersperse[division:].capitalize()


def random_username():
    characters = "abcdeghijklmnopqrstuvwxyz0123456789"
    new_username = ""
    for i in range(0, 10):
        random_char = random.choice(characters)
        new_username = new_username+random_char
    return new_username


print("Welcome to the username creator... Please choose one of the following options:\n 1. Create a username based on a name \n 2. Generate a random username")

option = input("Enter your choice here: ")

if option == "1":
    first_name = input("Please enter your first name: ")
    second_name = input("Please enter your second name: ")
    print(f"Your new user name is: {format_name(first_name, second_name)[0]} {
          format_name(first_name, second_name)[1]}")

elif option == "2":
    print(f"Your random username is: {random_username()}")

else:
    print("Please choose either 1 or 2")
