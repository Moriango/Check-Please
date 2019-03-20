import math

# def bill(total_cost, total_people):
#     if total_people <= 1:
#         raise ValueError("Need more than 1 person to split a check")
#     if total_cost <= 1: 
#         raise ValueError("Need more than 1 dollar to split a check")
#     return math.ceil(total_cost / total_people)
def bill():
    total_cost = float(input("What is the total cost? "))
    while total_cost < 2:
        total_cost = float(input("The bill must be more than 1 dollar \nPlease try again. \nWhat is the total cost? "))
    total_people = int(input("How many people? "))
    while total_people < 2:
        total_people = int(input("There must be more than 1 person to split the bill with. \nPlease try again.\nHow many people? "))
    print("Because there are {} people splitting the bill".format(total_people))
    return math.ceil(total_cost / total_people)
total_cost = bill()
# try:
#     people = int(input("How many people? "))
#     check = float(input("What is the total cost? "))
#     total_cost = bill(check, people)
# except ValueError as err:
#     print("Oh no! That's not a valid value. Try again...")
#     print("({})".format(err))
# else:
#     print("The total cost for everyone is {} dollar(s)".format(total_cost))
    
print("The total cost for everyone is {} dollar(s)".format(total_cost))