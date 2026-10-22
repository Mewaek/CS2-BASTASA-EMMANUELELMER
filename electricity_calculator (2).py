# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")
previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading

# FIXED Electricity Bill Calculator 
import math
RATE=12.90
name=input("Enter customer name: ")
while name == "":
    print("Invalid name. Customer name must not be empty.")
    name=input("Enter customer name: ")
    
while True:
    try:
        previous=float(input("Enter previous meter reading: "))
        if previous >= 0:
            break
        else:
            print("Invalid reading. Enter a number at least 0.")
    except ValueError:
            print("Invalid reading. Enter a valid number.")
    
while True:
    try:
        current=float(input("Enter current meter reading: "))
        if current >= previous:
            break
        else:
            print("Invalid reading. Current reading must be at least the previous reading.")
    except ValueError:
            print("Invalid input. Please enter a valid number.")

consumption=current-previous
total_bill=consumption*RATE

print("Customer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill,2))
