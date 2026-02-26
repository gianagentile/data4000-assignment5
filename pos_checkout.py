import random 
import sys

#Step 1: Student Key 
def get_seed():
    while True:
        try:
            student_key = input("Student Key: ").strip()
            if not student_key:
                raise ValueError("Student Key cannot be empty.")
            seed = sum(ord(char) for char in student_key)
            return seed
        except ValueError as e:
            print(e)

#Step 2/3: Item Entry Loop 
def get_item_name(): 
    while True:
        name = input("Item Name: ").strip()
        if name == "DONE":
            return "DONE"
        if name == "":
            print("Item Name cannot be empty.")
        else:
            return name
        
#Step 3: Unit Price Input 
def get_unit_price():
    while True:
        try:
            price = float(input("Unit Price: ").strip())
            if price <= 0:
                raise ValueError
            return price
        except ValueError:
            print("Unit Price must be a number greater than zero.")

#Step 3: Quantity Input
def get_quantity():
    while True:
        try:
            quantity = int(input("Quantity: ").strip())
            if quantity < 1:
                raise ValueError
            return quantity
        except ValueError:
            print("Quantity must be an integer greater than or equal to one.")

#Step 4: maintain subtotals and total units 
def main():
    seed = get_seed()

    subtotal = 0.0
    total_units = 0

    while True:
        name = get_item_name()
        if name == "DONE":
            break
        price = get_unit_price()
        quantity = get_quantity()

        subtotal += price * quantity
        total_units += quantity

#Step 5: Discount Logic 
    if total_units >= 10 or subtotal >= 100:
        discount = 0.10
    else:
        discount = 0
    discount_amount = subtotal * (discount / 100)
    total = subtotal - discount_amount

# Step 6: Seed-Based Memeber Perk 
    perk_applied = "NO"
    if seed % 2 != 0: 
        total -= 3.00
        perk_applied = "YES"
    if total < 0:
        total = 0.00

# Step 7: Output Format 
    print(f"Seed: {seed}")
    print(f"Units: {total_units}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount * 100}%")
    print(f"Perk Applied: {perk_applied}")
    print(f"Total: ${total:.2f}")
if __name__ == "__main__":
    main() 