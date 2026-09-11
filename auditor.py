inventory = 0
failed_entries = 0

while True:
    stock = input("Enter the stock quantity: ")

    if stock.lower() == "quit":
        break

    if stock.startswith("-") and stock[1:].isdigit():
        print("Please enter the valid number.")
        failed_entries += 1
        continue

    if not stock.isdigit():
        print("Please enter the valid integer.")
        failed_entries += 1
        continue

    stock = int(stock)

    inventory += stock
    print("Total inventory: ", inventory)

    if inventory > 500:
        print("The total inventory cannot exceed 500 units!")
        break

print("=========================")
print("Total Units Processed: ", inventory)
print("Number of failed entries: ", failed_entries)