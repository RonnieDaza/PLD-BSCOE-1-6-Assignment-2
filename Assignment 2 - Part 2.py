appleQuestion = int(input("How many apples you want to buy? "))
orangeQuestion = int(input("How many oranges you want to buy? "))

applePrice = 20
orangePrice = 25

appleTotal = appleQuestion * applePrice
orangeTotal = orangeQuestion * orangePrice
total = appleTotal + orangeTotal

print(f"The total amount is {total}.")