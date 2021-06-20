
import os
import sys
import time

print("Welcome to the terminal")
print("Author : MathewTheProgrammer \n")

#COMMANDS
command = input('Please enter a command:')

while True:
    if(command == "Help" or command == "help"):
        print('Commands: help\n'
              '          hello\n'
              '          clear\n'
              '          calculator\n'
              '          exit')
        command = input('Please enter a command:')

    if(command == "Hello" or command == "hello"):
        print('Hello!')
        command = input('Please enter a command:')

    if(command == "Clear" or command == "clear"):
        os.system('cls')

        print("Welcome to the terminal")
        print("Author : MathewTheProgrammer \n")
        command = input('Please enter a command:')

    if(command == 'Calculator' or command == 'calculator'):
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        op = input("What would you like to do(+ , - , * , / ):")
        if(op == "+"):
            sum = num1 + num2
            print(sum)
        if(op == "-"):
            sum = num1 - num2
            print(sum)
        if(op == "*"):
            sum = num1 * num2
            print(sum)
        if(op == "/"):
            sum = num1 / num2
            print(sum)
        command = input('Please enter a command:')

    if(command == "exit"):
        sys.exit(0)
