#We are building our recursive funtion which takes an integer as an input and returns the sum of all numbers from the input down to 1
#the functiuon will look like so if we were to write it iteratively:
#------------
#def sum_to_one(n):
#  result = 0
#  for num in range(n, 0, -1):
#    result += num
#  return result
#------------
#sum_to_one(4)
#num is set to 4, 3, 2, and 1
#10
#------------

#However we can think of each recursive call as an iteration of the loop above
#recursive_sum_to_one(4)
#recursive_sum_to_one(3)
#recursive_sum_to_one(2)
#recursive_sum_to_one(1)
#------------------
# Every recursive method does need a base case when the function does not recurse and a recursive step, when the recursing fuction mmoves toward the base step

#Base case:
#The integer given as input is 1.
#---------------
#Recursive step:
#The recursive function call is passed an argument 1 less #than the last function call.

def sum_to_one(n):
    #setting up our base case
    if n == 1:
        return n
    print("Recursing with input: {0}".format(n))
    #setting up our recursive step
    return n + sum_to_one(n-1)

print(sum_to_one(4))
