# function to multiply
def multiply(a,b):
    return a * b

# function to add
def add(a,b):
    return a + b

# function to divide
def divide(a,b):
    return a / b

# function to substract
def substract(a,b):
    return a - b

print("Simple Calculator")
print("Select the operation")
print("1. Add")
print("2. Multiply")
print("3. Divide")
print("4. Substract")

# Take input from user
choice = input("Enter choice 1/2/3/4:")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if choice == "1":
    print(a, "+", b, "=", add(a,b))
elif choice == "2":
    print(a, "*", b, "=", multiply(a,b))
elif choice == "3":
    print(a, "/", b, "=", divide(a,b))
elif choice == "4":
    print(a, "-", b, "=", substract(a,b))
else:
    print("Invalid entry for operation. Exiting.")


