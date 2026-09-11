inventory = 0

while True:
    stock = input("Enter the stock quantity: ")

    if stock.lower() == "quit":
        break

    if stock.startswith("-") and stock[1:].isdigit():
        print("Please enter the valid number.")
        continue

    if not stock.isdigit():
        print("Please enter the valid integer.")
        continue

    stock = int(stock)

    inventory += stock
    print("Total inventory: ", inventory)