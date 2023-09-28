#This Program Calculates and displays travel expenses
#9/28/2023
# CTI-110 P1HW2 - Travel Expense
# William Ford


print("travel Budget")
#get budget
budget = float (input("enter Budget:"))
#get travel destination
travel_destination = (input("enter travel destination:"))
#get amount they will spend on gas
Gas_amount = float(input("enter gas amount:"))
#get , budget for accomodation
accomodation = float(input("enter accomodation/hotel:"))	
#food expense
food = float(input("enter food expense:"))
print ("------------Travel Expenses-----------")
print (f"location:{travel_destination}")
print (f"initial Budget:{budget}")


print(f"fuel:{Gas_amount}")
print(f"Accomodation:{accomodation}")
print(f"food:{food}")

Remaining = (budget) - (Gas_amount)- (accomodation)- (food)	
print (f"Remaining balance:{Remaining}")