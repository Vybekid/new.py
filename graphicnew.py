# One Liner Factorial Python Code

factorial = lambda x: x and x * factorial(x-1) or 1

print('Factorial of 5 is', factorial(5))