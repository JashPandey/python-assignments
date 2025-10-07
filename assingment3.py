# task 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter a number: "))
print("factorial of the given number is",factorial(n))

# task 2
import math
n = int(input("Enter a number: "))
print(math.sqrt(n))
print(math.log(n))
print(math.sin(n))