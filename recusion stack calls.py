#We are building our own recursion stack

def sum_to_one(n):
    result = 1
    call_stack = []
    #the below loop represents the recursive calls which lead to the base case
    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print("BASE CASE REACHED")
    # the below loop simulates the recursive function when we return values as the function calls are "popped" off the call stack
    while len(call_stack) != 0:
        return_value = call_stack.pop()
        #each element we pop off the stack is a dictionary which represents a single recursive function call.
        print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
        result += return_value['n_value']
    return result, call_stack

sum_to_one(4)
