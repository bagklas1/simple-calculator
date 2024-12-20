# This function adds two numbers
def add(a, b):
    return a + b
    
# This function subtracts two numbers
def subtract(a, b):
    return a - b

#This functions multiplies two numbers
def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
        
def power(a, b):
    return a ** b


# Example usage
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Power:", power(10, 2))
