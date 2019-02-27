# We are looking at building a factorial function using recursion and analysing its Big O
#Finding Big O for a recursive method is looking at recursive funtion calls growth in relation to the size of the input

def factorial(n):
    # setting our base case
    if n == 1:
        return n
    # setting our recirsive function
    return n * factorial(n - 1)

print(factorial(12))
