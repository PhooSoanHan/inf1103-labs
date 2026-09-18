def get_valid_input():
    while True:
        user_input = input("Enter stock quantity (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            return "quit"

        try:
            quantity = int(user_input)

            if quantity < 0:
                print("Invalid input. Stock quantity cannot be negative.")
                return None

            return quantity

        except ValueError:
            print("Invalid input. Please enter a whole number.")
            return None


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print("Total Units:", total_units)
    print("Failed/Rejected Entries:", failed_attempts)


# Main program
inventory = 0
deliveries_processed = 0
failed_attempts = 0

while True:
    delivery = get_valid_input()

    if delivery == "quit":
        break

    if delivery is None:
        failed_attempts += 1
        continue

    inventory = process_delivery(inventory, delivery)
    tax = calculate_tax(delivery)

    deliveries_processed += 1

    print("Delivery accepted:", delivery)
    print("Tax for this delivery:", tax)
    print("Current inventory:", inventory)


print("\nTotal Deliveries Processed:", deliveries_processed)
generate_report(inventory, failed_attempts)