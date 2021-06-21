import os
import sys
import datetime
import colorama
from colorama import Fore
colorama.init()

print(Fore.RESET + "Welcome to the RandomCLI")
print("Author : MathewTheProgrammer \n")

# COMMANDS
command = input('Please enter a command:')

while True:
    if command == "Help" or command == "help":
        print('Commands: help\n'
              '          hello\n'
              '          clear\n'
              '          calculator\n'
              '          date\n'
              '          color\n'
              '          exit')
        command = input('Please enter a command:')

    if command == "Hello" or command == "hello":
        print('Hello!')
        command = input('Please enter a command:')

    if command == "Clear" or command == "clear":
        os.system('cls')

        print("Welcome to the RandomCLI")
        print("Author : MathewTheProgrammer \n")
        command = input('Please enter a command:')

    if command == 'Calculator' or command == 'calculator':
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        op = input("What would you like to do(+ , - , * , / ):")
        if op == "+":
            sum_ = num1 + num2
            print(sum_)
        if op == "-":
            sum_ = num1 - num2
            print(sum_)
        if op == "*":
            sum_ = num1 * num2
            print(sum_)
        if op == "/":
            sum_ = num1 / num2
            print(sum_)
        command = input('Please enter a command:')

    if command == 'date' or command == 'Date':
        now = datetime.datetime.now()

        print("The current date and time is:")
        print(now.strftime("%y-%m-%d %H:%M:%S"))
        command = input('Please enter a command:')

    if command == 'color' or command == 'Color':
        print("Available colors are : BLUE , CYAN , RED , GREEN and GREY")
        color = str(input("What color would you like:"))
        if color == "BLUE":
            os.system('cls')

            print(Fore.BLUE + "Welcome to the RandomCLI")
            print("Author : MathewTheProgrammer \n")

        if color == "CYAN":
            os.system('cls')

            print(Fore.CYAN + "Welcome to the RandomCLI")
            print("Author : MathewTheProgrammer \n")

        if color == "RED":
            os.system('cls')

            print(Fore.RED + "Welcome to the RandomCLI")
            print("Author : MathewTheProgrammer \n")

        if color == "GREEN":
            os.system('cls')

            print(Fore.GREEN + "Welcome to the RandomCLI")
            print("Author : MathewTheProgrammer \n")

        if color == "GRAY":
            os.system('cls')

            print(Fore.RESET + "Welcome to the RandomCLI")
            print("Author : MathewTheProgrammer \n")
        command = input("Please enter a command:")

    if command == 'exit' or command == 'Exit':
        sys.exit(0)
