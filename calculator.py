# This is a simple calculator program in Python

# Ask the user for the first number
num1 = float(input("Enter the first number: "))
# Ask the user for the second number
num2 = float(input("Enter the second number: "))
# Ask the user for the operation (+, -, *, or /)
op = input("Enter +, -, *, or /: ")

# Compute the result based on the operation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2

# Print the result in the format: 10 + 5 = 15
print(num1, op, num2, "=", result)
