'''
# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    return "ANSWER HERE" # Remove this line and implement
'''


months= ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre", "octubre","noviembre","diciembre"]

def number_to_month(month):
    if month < 1 or month > 12:
        return "error"
    return months [month -1]
'''
month = int(input("Enter a number"))
print(number_to_month(month))
'''