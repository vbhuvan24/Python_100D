print('Welcome to the Tip Calculator')
bill = float(input("What was the the total bill? Rs. "))

tip = float(input("What percentage tip would you like to give? 10, 12, 15? "))

person = int(input("How many people to split the bill? "))

result = round((bill + (bill * (tip / 100))) / person, 2)

print(result)