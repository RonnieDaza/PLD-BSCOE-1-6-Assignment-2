money = int(input("Enter the amount of money: "))
apple = int(input("Enter the price of an apple: "))

appleQuantity = money // apple
applePrice = appleQuantity * apple
moneyLeft = money - applePrice

print(f"You can buy {appleQuantity} apples and your change is {moneyLeft} pesos.")