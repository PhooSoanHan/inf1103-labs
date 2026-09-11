inventory = 0

while True:
    stock = input("Enter the stock quantity: ")

    if stock.lower() == "quit":
        break

    stock = int(stock)