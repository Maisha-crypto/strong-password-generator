import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '>', '<', ';']


#this method creates a random password
def CreatePassword(letters_required, numbers_required, symbols_required):
    password_list = []

    for char_ in range(1,letters_required+1):
        password_list += random.choice(letters)
    for num in range(1, numbers_required+1):
        password_list += random.choice(numbers)
    for symbol in range(1, symbols_required+1):
            password_list += random.choice(symbols)

    random.shuffle(password_list)

    #reshufling the password
    password = ""
    for i in password_list:
        password += i

    username = input("Enter username for the acoount: ")
    print(f"\nYour {username} password is: {password}\n")

    #Saving the password to a txt file named password
    file = open('password.txt', 'a')
    file.write(f"Your {username} password is: {password}\n")
    file.close()
    
let_required = int(input("How many letters in your password?? "))
num_required = int(input("How many numbers in yor password?? "))
sym_required = int(input("How many symbols in your password?? "))
     
CreatePassword(let_required, num_required, sym_required)


