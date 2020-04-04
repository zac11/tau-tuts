"""
BASIC CALCULATOR
"""

def add():
    a = float(input("Please enter first number"))
    b = float(input("Please enter second number"))
    print("Sum is ",a+b)

def subtract():
    a = float(input("Please enter first number"))
    b = float(input("Please enter second number"))
    print("Subtraction is ", a - b)

def multiply():
    a = float(input("Please enter first number"))
    b = float(input("Please enter second number"))
    print("Multiplication is ", a * b)

def divide():
    a = float(input("Please enter first number"))
    b = float(input("Please enter second number"))
    print("Division is ", a / b)

# define the operation

operation = input("Please type your choice : +,-,*,/")
if operation=='+':
    add()

elif operation == '-':
    subtract()

elif operation == '*':
    multiply()

elif operation == '/':
    divide()

else:
    print("Operation entered is not permitted.")