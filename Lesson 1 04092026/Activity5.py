username = input("Enter username: ")
age = input ("Enter Age: ")
age1=0
age1 = age.isdigit()
category = input ("Enter Content Category: ")


print("\nInstagram Profile")
print("===================")
print("Username: ",username)
print("Age: ",age)
print("Category:",category)

if age1 > 40 and category == "fun":
    print ("You are old what is fun for you??")

#3a.Return type for input(0 is string)
#3b.First they will check is age1 is more than 40 and if category is equal to fun ,if both is true the code will be printed out