def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide(a, b):
    return a / b

print("Operations")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = int(input("Enter and operation: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operation == 1:
    sum = add(num1, num2)
    print("Sum: {}" .format(sum))
elif operation == 2:
    difference = subtract(num1, num2)
    print("Difference: {}" .format(difference))
elif operation == 3:
    product = multiply(num1, num2)
    print("Product: {}" .format(product))
elif operation == 4:
    if num2 != 0:
        modulus = multiply(num1, num2)
        print("Modulus: {}" .format(modulus))
    else:
        print("No division by Zero")
else: 
    print("Invalid operation")
