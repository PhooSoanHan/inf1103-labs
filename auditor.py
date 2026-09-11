inventory = 0

while True:
    stock = input("Enter the stock quantity: ")

    if stock.lower() == "quit":
        break

    if not stock.isdigit():
        print("Please enter the valid integer.")
        continue

    stock = int(stock)