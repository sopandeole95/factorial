# Factorial Calculator
def factorial(n):
    if n < 0:
        return None  # No factorial for negative numbers
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Main program
print("Factorial Calculator")
try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("There is no factorial for negative numbers.")
    else:
        print(f"The factorial of {num} is {factorial(num)}")
except ValueError:
    print("Please enter a valid integer.")