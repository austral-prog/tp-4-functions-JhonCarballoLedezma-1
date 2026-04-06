# Replace the "ANSWER HERE" for your answer
'''
def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    return "ANSWER HERE" # Remove this line and implement


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    return "ANSWER HERE" # Remove this line and implement

'''
'''
x = int(input())
y = int(input())
z = int(input())
'''
def max_of_two(x, y):
    if x >= y : #son iguales
        print(x)
        return x
    elif x < y: #x mayor a y
        print(y)
        return y


def max_of_three(x, y, z):
    if x >= y >= z:
        return x
    elif y >= x >= z :
        return y
    else:
        return z

#print(max_of_two(x,y))
#print(max_of_three(x,y,z))


    