Inventory = 0
Finalised_inventory=0
Rejected_count=0
Inventory1=0
Type= ""

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
    




