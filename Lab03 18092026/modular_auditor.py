Inventory = 0
Finalised_inventory=0
Rejected_count=0
Inventory1=0
Type= ""
Delivery_amt=0



'''def get_valid_input():
    while True:
        
        Stock = input("Enter Inventory Stock: ")
        if Stock < 0:
            print("No negative number")
            Rejected_count += 1
            continue
        elif Stock.is_integer() == False:
            print("It is not an integer, Please Re-Enter!")
            Rejected_count += 1
            continue
        else:
            Stock = int(Stock)
            Inventory += Stock
            if Inventory > 500:
                print("Alert: There is more than 500 in the inventory ")
                break
            else:
                Inventory1 = Inventory
                return Inventory1
'''                
        
def get_valid_input1():
    Inventory = 0  # Initialize Inventory to 0
    Rejected_count = 0  # Use the global Rejected_count variable
    Type=input("Continue/Quit: ")
    #if Type.lower()=="quit":
    while Type.lower() != "quit":
        Stock = input("Enter Inventory Stock: ")
        if not Stock.isdigit():
            print("It is not an integer, Please Re-Enter!")
            Rejected_count += 1
            continue
        Stock = int(Stock)
        if Stock < 0:
            print("No negative number")
            Rejected_count += 1
            print("Rejected count: " + str(Rejected_count))
            continue
        else:
            Delivery_amt =input("Enter Delivery Amount: ")
            Delivery_amt = int(Delivery_amt)
            if Delivery_amt < 0:
                print("No negative number")
                Rejected_count += 1
                print("Rejected count: " + str(Rejected_count))
                continue
            else:
            #  Inventory += Stock
                # no_of_deliveries += 1
                return Stock, Delivery_amt,Rejected_count  # Return the valid stock and delivery amount


    return "quit"  # Exit the loop if the user enters "quit"
'''elif Delivery_amt.is_integer() == False:
                print("It is not an integer, Please Re-Enter!")
                Rejected_count += 1
                continue'''                


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


def generate_report(total_units,failed_attempts,Taxes):
    print("Inventory: " + str(total_units))
    print("Rejected count: " + str(failed_attempts))
    print("Total Taxes: " + str(round(Taxes, 2)))

taxs1 = 0
no_of_deliveries = 0
while True:
   
    result = get_valid_input1()

    if result == "quit":
        break

    Stock, delivery_amt, Rejected_count = result

    Inventory1= process_delivery(Inventory, Stock)

    no_of_deliveries += 1

    taxs = calculate_tax(delivery_amt)

    taxs1=taxs1 + taxs

    generate_report(Inventory1,Rejected_count, taxs1)

    print("Number of Deliveries: " + str(no_of_deliveries))










'''
while True:
    stock,delivery_amt=get_valid_input1()
   # get_valid_input1()
    if get_valid_input1() == "quit":
        break
    Inventory1 = process_delivery(Inventory, stock)
    taxs=calculate_tax(delivery_amt)
    generate_report(Inventory1,Rejected_count)
  #  print(no_of_deliveries)
'''



















    
''' Delivery_amt += taxs
    no_of_deliveries += 1'''
'''
while Type != "quit":
    Type=input("Continue/Quit: ")
    if Type.lower()=="quit":
        break
    else:
        try:
          Stock= int(input("Enter Inventory Stock: "))
          Inventory= Inventory +Stock
        except ValueError:
           # Stockdigit=Stock.is_integer
       # if Stockdigit == False: 
            print("It is not an integer,Please Re-Enter!")
            Rejected_count+=1
            continue
        if Stock <0:
            print("No negative number")
            Rejected_count+=1
            continue
            Inventory=+Stock
        else:
         if Inventory > 500:
            print("Alert: There is more than 500 in the inventory ")
            break
          
    Finalised_inventory=Inventory

        
print("Inventory" +str(Finalised_inventory))
print("Rejected_count"+ str(Rejected_count))
    



'''
