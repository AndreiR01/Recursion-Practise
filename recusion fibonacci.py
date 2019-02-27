# We are looking at building a a solution to a problem where we have to use multiple recursive calls within the function definition
#Looking at the Fibonacci in order to calculate the current fibonacci number we are going to need two recursive calls since we need the last two numbers

def fibonacci(n):
    #Below we are looking at the base case
    if n == 1:
        return 1
    elif n == 0:
        return 0
    #Below we are looking at the recursive step
    return fibonacci(n-2) + fibonacci(n-1)

time_complexity = "2^N"
