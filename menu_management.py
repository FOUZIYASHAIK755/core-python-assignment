def add_menu_item(menu, item):
    """Add an item to the menu."""
    if item not in menu:
        menu.append(item)
        print(f"{item} added to the menu.")
    else:
        print(f"{item} is already in the menu.")
    return menu

def remove_menu_item(menu, item):
    """Remove an item from the menu."""
    if item in menu:
        menu.remove(item)
        print(f"{item} removed from the menu.")
    else:
        print(f"{item} is not in the menu. Cannot remove.")
    return menu

def check_menu_item(menu, item):
    """Check if an item is available in the menu."""
    if item in menu:
        return f"{item} is available."
    else:
        return f"{item} is not available."

def main():
    # Initial menu
    menu = ["Pizza", "Burger", "Pasta", "Salad"]
    print("Initial Menu:", menu)
    
    # Inputs
    add_item = "Tacos"
    remove_item = "Salad"
    check_item = "Pizza"
    
    # Menu Operations
    menu = add_menu_item(menu, add_item)
    menu = remove_menu_item(menu, remove_item)
    availability = check_menu_item(menu, check_item)
    
    # Final Output
    print("Updated Menu:", menu)
    print("Availability:", availability)
main()
