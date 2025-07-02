'''     # This script demonstrates the use of functions in Python.'''
def greet(name):      # Function to greet a person with their name.
    print(f"Hello, {name}!")

greet("Wendy") # Uses default greeting

def add_numbers(a, b):    # Function to add two numbers.
    return a + b

result = add_numbers(5, 10)
print(result)
# This script demonstrates the use of functions in Python.


def factorial(n):  # Function to calculate the factorial of a number.
    if n == 0 or n == 1:  # Base case for factorial.
        return 1
    else:
        return n * factorial(n - 1)

def greet(name, greeting="Hello"):  # Function to greet a person with a custom greeting.
    print(f"{greeting}, {name}!")
        
greet("Alice", "Hi")     # Uses custom greeting
greet("Bob")              # Uses default greeting   
