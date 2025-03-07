#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num

import sys

def calculator(operation, num1, num2):
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "Cannot divide by zero"
    }
    
    if operation in operations:
        return operations[operation]
    else:
        print("Invalid operation!")  # Ensure it prints the required message
        return None  # Ensure it returns None

   
