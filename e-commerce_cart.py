def calculate_total_price(cart_items):
    if not cart_items:
        return "The cart is empty."
    total_price = sum(cart_items.values())
    item_count = len(cart_items)
    if item_count > 5:
        discount = total_price * 0.10
        total_price -= discount
    
    return total_price

def main():
    cart_items = {}
    
    print("Enter items for your cart (type 'done' to finish):")
    
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        try:
            item_price = float(input(f"Enter price for {item_name}: "))
            cart_items[item_name] = item_price
        except ValueError:
            print("Please enter a valid price.")
        total = calculate_total_price(cart_items)
    print(f"Total Price: {total}")
main=main()