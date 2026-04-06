
# Replace the "ANSWER HERE" for your answer
'''
def roots(a, b, c):
    return "ANSWER HERE"


def value_y(a, b, c, x):
    return "ANSWER HERE"


def to_string(a, b, c):
    return "ANSWER HERE"


def derivation(a, b, c):
    return "ANSWER HERE"
'''

def roots(a, b, c):
    discriminante = b **2 - 4 * a * c
    raiz = (- b + discriminante ** 0.5 ) / (2 * a)
    raiz2 = (- b - discriminante ** 0.5 ) / (2 * a)
    if discriminante < 0:
        return "( )"
    elif discriminante == 0:
        return f"({raiz})"
    else:
        return f"({raiz}, {raiz2})"
    
    
def value_y(a, b, c, x):
    valor = a * x ** 2 + b * x + c
    return valor
    
    
def to_string(a, b, c):
    anwser = "f(x) = "
    if a != 0 :
        anwser += f"{a} * X^2"
        
    if b != 0 :
        if a != 0:
            anwser += " + "
        anwser += f"{b} * X"
    
    if c != 0:
        if a != 0 or b != 0:
            anwser += " + "
        anwser += f"{c}"
    return anwser

def derivation(a, b, c):
    anwser = "f'(x) = "
    if a != 0 :
        anwser += f"{a*2} * X"
        if b != 0 :
            anwser += " + "
    if b != 0:
        anwser += f"{b}"
    if a == 0 and b == 0:
        anwser += "0"
        
    return anwser