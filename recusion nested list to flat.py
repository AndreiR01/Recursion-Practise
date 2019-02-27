# We are looking at building a flatten fucntion which that removes nested lists within a list but keeps the values contained

#When approaching this problem via recursion we need to think of the base case and recursive function
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

def flatten(my_list):
    result = []
    for item in my_list:
        if isinstance(item, list):
            print("We got ze list!")
            flat_list = flatten(item)
            result += flat_list
        else:
            result.append(item)

    return result
flatten(planets)
