# Predefined dictionary of groceries with prices
groceries = {
    "apples": 3.99,
    "bananas": 2.49,
    "milk": 4.29,
    "bread": 2.99,
    "eggs": 5.49,
    "chicken": 12.99,
    "tomatoes": 3.49,
    "lettuce": 2.79,
    "cheese": 6.99,
    "orange juice": 4.99,
    "rice": 8.99,
    "pasta": 3.29
}

# Initialize empty cart
cart = {}

print("🛒 Welcome to Fresh Market!")
print("=" * 50)
print("Available items:")
for item, price in groceries.items():
    print(f"  - {item.title()}: ${price:.2f}")
print("=" * 50)
print("Type item names to add them to your cart.")
print("Type 'checkout' when you're done shopping.\n")

# Shopping loop
while True:
    item_name = input("Enter item name (or 'checkout' to finish): ").lower().strip()
    
    # Check if user wants to checkout
    if item_name == "checkout":
        break
    
    # Check if item exists in groceries
    if item_name in groceries:
        # Ask for quantity with error handling
        while True:
            try:
                quantity = int(input(f"Enter quantity for {item_name}: "))
                if quantity > 0:
                    # Add to cart or update quantity
                    if item_name in cart:
                        cart[item_name] += quantity
                    else:
                        cart[item_name] = quantity
                    print(f"✓ Added {quantity} {item_name} to cart\n")
                    break
                else:
                    print("⚠ Please enter a positive number.\n")
            except ValueError:
                print("⚠ Invalid input. Please enter a number.\n")
    else:
        print(f"⚠ '{item_name}' is not available. Please choose from the list.\n")

# Display final bill
print("\n" + "=" * 50)
print("📋 FINAL BILL")
print("=" * 50)

if not cart:
    print("Your cart is empty!")
else:
    total = 0
    
    # Display each item with subtotal
    for item, quantity in cart.items():
        price = groceries[item]
        subtotal = price * quantity
        total += subtotal
        print(f"{item.title():<20} x {quantity:<3} @ ${price:>6.2f} = ${subtotal:>7.2f}")
    
    print("-" * 50)
    print(f"{'TOTAL':<20}                     ${total:>7.2f}")
    print("=" * 50)
    print("Thank you for shopping with us! 🎉")
