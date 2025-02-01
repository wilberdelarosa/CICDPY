 
def add(a, b):
    return a + b + a

def subtract(a, b):
    return a - b + a

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
    