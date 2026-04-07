import random
import string
def choose(prompt):
    while True:
        pick = input(prompt).strip().lower()
        if pick == 'y':
            return True
        elif pick == 'n':
            return False
        else:
            print("Write y or n")

def charters(character,generate):
    return generate if character else ""

while True:
    print("Password generator")
    try:
        length = int(input("Password length: "))
    except ValueError:
        print("Write a valid number")
        continue
    if length <= 0:
        print("Write number above 0")
        continue
    
    upper = choose("Do you want upper letters (y/n)? ")
    numbers = choose("Do you want numbers (y/n)? ")
    symbols = choose("Do you want symbols (y/n)? ")

    char = string.ascii_lowercase
    char += charters(upper,string.ascii_uppercase)
    char += charters(numbers,string.digits)
    char += charters(symbols,string.punctuation)
    
    if not char:
        print("Choose at least one option")
        continue

    generate = "".join(random.choice(char) for _ in range(length))

    print(f"Your generated password is: {generate}")

    if not choose("Start over? (y/n): "):
        exit()
