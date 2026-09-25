Inventory = 0
Finalised_inventory=0
Rejected_count=0
Inventory1=0
Type= ""
Delivery_amt=0
next_id=1000
history_list = []
total = 0

Amount=[]

import json
import os

FILENAME = "inventory.txt"  # Define the filename for storing inventory data


import os

FILENAME = "inventory.txt"


def load_inventory():
    """Requirement 1 & 4: Load total and transaction history from file if it exists[cite: 1].

    Returns (total, history_list)
    """
    if not os.path.exists(FILENAME):
        return 0, []

    '''history_list = []
    total = 0'''

    try:
        with open(FILENAME, "r") as file:
            lines = [line.strip() for line in file if line.strip()]

            if lines:
                # First line stores the total inventory count
                total = int(lines[0])

                # Remaining lines store formatted order tuples: 1001, Wireless Mouse, 2
                for line in lines[1:]:
                    parts = line.split(",")
                    if len(parts) == 3:
                        order_id = int(parts[0].strip())
                        product_name = parts[1].strip()
                        quantity = int(parts[2].strip())

                    history_list.append((order_id, product_name, quantity))
        return total,history_list
    except (ValueError, IOError):
        print("Warning: Save file unreadable or corrupt. Starting fresh.")
        return 0, []

def save_inventory(total_units, transaction_history):
   
    """Requirement 3 & 4: Save final total and transaction history to inventory.txt[cite: 1]."""
 
    with open(FILENAME, "w") as file:
        file.write(f"{total_units}\n")
        file.write("ID,Product,Stock\n")
        for transaction in transaction_history:
            order_id, product_name, quantity = transaction
            file.write(f"{order_id},{product_name},{quantity}\n")

def list_current_orders():
    """Reads and prints all current orders saved in inventory.txt."""
    if not os.path.exists(FILENAME):
        print("\nNo order history found.")
        return

    print("\n--- Current Orders in File ---")
    try:
        with open(FILENAME, "r") as file:
            lines = [line.strip() for line in file if line.strip()]

        if not lines:
            print("Inventory file is empty.")
            return

        print(f"Total Inventory Count: {lines[0]}")
        print("-" * 30)

        # Skip header line if it exists
        start_idx = 1
        if len(lines) > 1 and lines[1].startswith("ID,Product,Stock"):
            start_idx = 2

        for line in lines[1:]:
            # Skip header line if present
            if line.startswith("ID,Product,Stock"):
                continue

            parts = line.split(",")
            if len(parts) == 3:
                order_id, product_name, stock = (
                    parts[0].strip(),
                    parts[1].strip(),
                    parts[2].strip(),
                )
                print(
                    f"Order ID: {order_id} | Product: {product_name} | Stock: {stock}"
                )
        print("-" * 30)
    except IOError:
        print("Error reading order history.")

        
def get_valid_input1():
    Inventory = 0  # Initialize Inventory to 0
    Rejected_count = 0  # Use the global Rejected_count variable
    Type=input("Continue/Quit: ")
    #if Type.lower()=="quit":
    while Type.lower() != "quit":
        product_name = input("Enter Product Name: ")
        Stock = input("Enter Inventory Stock: ")
        if not Stock.isdigit():
            print("It is not an integer, Please Re-Enter!")
            Rejected_count += 1
            continue
        Stock = int(Stock)
        print("Product Name: " + str(product_name))
        print("Stock: " + str(Stock))
        if Stock < 0:
            print("No negative number")
            Rejected_count += 1
            print("Rejected count: " + str(Rejected_count))
            continue
        else:
            Delivery_amt =input("Enter Delivery Amount: ")
            Delivery_amt = int(Delivery_amt)
            Amount.append(Delivery_amt)
            if Delivery_amt < 0:
                print("No negative number")
                Rejected_count += 1
                print("Rejected count: " + str(Rejected_count))
                continue
            else:
            #  Inventory += Stock
                # no_of_deliveries += 1
                return Stock,Amount[-1],Rejected_count,product_name  # Return the valid stock and delivery amount


    return "quit"  # Exit the loop if the user enters "quit"
           
def add_order(next_id,Product_name,Stock,transaction_history):
  
    list_current_orders()
    if transaction_history:
        next_id = transaction_history[-1][0] + 1
    else:
        next_id = 1001

    # Append new order tuple
    new_order = (next_id, Product_name, Stock)
    transaction_history.append(new_order)

    print("\nNew Order Added:")
    print(f"{new_order[0]},{new_order[1]},{new_order[2]}")

    return transaction_history  # Return the updated list of orders


def process_delivery(current_total,new_value):
    new_total = current_total + new_value
    if new_total > 500:
        print("Alert: There is more than 500 in the inventory ")
       
        return new_total 
    else:
        return new_total # Return the updated total with the new value added



def calculate_tax(amount):
    tax_rate = 0.1  # 10% tax rate
    tax_amount = amount * tax_rate
    return tax_amount #return the taxed amount of the delivery

'''def current_orders():
    """Requirement 5: Display current orders in a readable format[cite: 1]."""
    print("Current Orders:")
    with open("inventory.txt", "r") as file:
        print(file.read())
    while True:
        print(n+1,f"Product Name: {product_name1}, Stock: {stock1}")'''
    

def generate_report(total_units,failed_attempts,Taxes):
    print("Inventory: " + str(total_units))
    print("Rejected count: " + str(failed_attempts))
    print("Total Taxes: " + str(round(Taxes, 2)))
'''
def History_Tracking(Stock_no,Delivery_amt):
    List=[]
    List.append((Stock_no,Delivery_amt))
    return List
'''

taxs1 = 0
no_of_deliveries = 0
# Initialize transaction_history and load saved inventory at startup
Inventory, transaction_history = load_inventory()
with open(FILENAME, "w") as file:
    pass  # Clear the file contents at the start of the program

while True:
  #  current_orders()  # Display current orders before getting new input
    result = get_valid_input1()

    if result == "quit":
        
        # Save inventory total and transaction history list when user quits
        save_inventory(Inventory, transaction_history)
        print("Data saved successfully.")
        break

    Stock, Amount[-1], Rejected_count, product_name = result

    Inventory= process_delivery(Inventory, Stock)

    transaction_history = add_order(next_id, product_name, Stock, transaction_history)  # Add the order to the transaction history




    no_of_deliveries += 1

    taxs = calculate_tax(Amount[-1])  # Calculate tax for the current delivery amount

    taxs1=taxs1 + taxs

    generate_report(Inventory,Rejected_count, taxs1)

    save_inventory(Inventory, transaction_history)

    print("Number of Deliveries: " + str(no_of_deliveries))











