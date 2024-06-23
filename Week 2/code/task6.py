def update_inventory(inventory_dict, item, quantity):
    """
    Updates the inventory dictionary by adding or removing the specified quantity of the item.
    Ensures that the quantity of any item does not go below zero.
    
    :param inventory_dict: Dictionary where keys are item names and values are quantities.
    :param item: The item name to be updated.
    :param quantity: The quantity to add or remove (negative values for removal).
    :return: The updated inventory dictionary.
    """
    if item in inventory_dict:
        inventory_dict[item] += quantity
        if inventory_dict[item] < 0:
            inventory_dict[item] = 0
    else:
        if quantity > 0:
            inventory_dict[item] = quantity
        else:
            inventory_dict[item] = 0
    return inventory_dict

def main():
    # Step 1: Initialize an inventory dictionary with at least 5 items
    inventory = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "milk": 2,
        "bread": 6
    }
    
    print("Initial inventory:", inventory)
    
    # Step 2: Prompt the user to update the inventory by adding or removing quantities of 3 items
    for _ in range(3):
        item = input("\nEnter the item name to update: ")
        quantity = int(input(f"Enter the quantity to add/remove for {item} (use negative values for removal): "))
        inventory = update_inventory(inventory, item, quantity)
    
    # Step 3: Display the updated inventory
    print("\nUpdated inventory:", inventory)

if __name__ == "__main__":
    main()
