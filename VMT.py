# Product list with numbers and prices
items = {
    1: {"name": "cookie", "price": 1.75},
    2: {"name": "energydrink", "price": 2.00},
    3: {"name": "candy", "price": 1.00},
    4: {"name": "water", "price": 2.00},
}

# Display menu
print("\n=== VENDING MACHINE ===")
for item_num, details in items.items():
    print(f"{item_num}. {details['name']} - ${details['price']:.2f}")
print("========================\n")

# Cart to store selected items
cart = []

# Loop to choose items by number
while True:
    choice = input("Enter item number (or type 'done' to finish): ").lower()
    
    if choice == 'done':
        break
    
    # Convert to integer and validate
    try:
        item_num = int(choice)
        if item_num in items:
            cart.append(items[item_num])
            print(f"✓ Added {items[item_num]['name']} to cart")
        else:
            print("Invalid item number. Please try again.")
    except ValueError:
        print("Please enter a valid number or 'done'")

# Print receipt
if cart:
    print("\n===== RECEIPT =====")
    for item in cart:
        print(f"{item['name']}: ${item['price']:.2f}")
    print("===================")
    print(f"TOTAL: ${sum(item['price'] for item in cart):.2f}")
    print("===================\n")
else:
    print("No items selected.")
