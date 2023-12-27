import pickle
f=open('dress.dat','rb+')
dress=pickle.load(f)
dress1=dress
temp=[]
order=""

def adminLogin():                                        #for admin purpose
    print("1.Display Menu")
    print("2.Add a new item")
    print("3.Remove item")
    print("4.Total goods available")
    print("5.Income and Loss")
    print("6.Update item")
    print("7.Logout")
    
def adminDisplayMenu():
    print("Id\tName\tAvailable\tPrice\tOriginal Price")
    for d in dress:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}\t{d["Original_Price"]}')

def addItem():
    n=int(input("Enter the no of new items to be added with new id : "))
    for i in range(n):
        new_id=int(input("Enter new id : "))
        new_Name=input("Enter new Name : ")
        new_Available=int(input("Enter no of Available items: "))
        new_Price=int(input("Enter Price : "))
        new_original=int(input("Enter the original price : "))
        d=[{"id":new_id,"Name":new_Name,"Available":new_Available,"Price":new_Price,"Original_Price":new_original}]
        dress.extend(d)
        adminDisplayMenu()

def removeItem():
    dressId=int(input("Enter the id need to be deleted : "))
    found=False
    for d in dress1:
        found=d["id"]==dressId
        if found !=True:
            temp.append(d)
            continue
        if found==True:
            dress1.remove(d)
    print("Deleting item....")
    if len(temp)==len(dress1):
        print(f"{dressId} not found")
    else:
        print(f"{dressId}'s one available is removed from the list")
    adminDisplayMenu()
def goods():
    Total=0
    print("\n")
    for d in dress:
        print(f'{d["Name"]} = {d["Available"]}')
        Total+=(d["Available"])
    print("\nTotal available goods is : ",Total)
def incomeLoss():
    total=0
    for d in dress:
        total+=((d["Available"]*d["Price"])-(d["Available"]*d["Original_Price"]))
    print("\nTotal income or loss is : ",total)
def update():
    print("***You cannot update the id for a product because it is fixed for the product***")
    desired_Id=int(input("Enter the id whose values need to be updated : "))
    n=int(input("Enter no of things you want to update:"))
    for i in range(n):
        value=int(input("Press desired no for updating desired value [1->Name],[2->Available],[3->Price],[4->Original_Price] : "))
        found=False
        for d in dress1:
            found=d["id"]==desired_Id
            if found !=True:
                temp.append(d)
                continue
            if found==True:
                    if(value==1):
                        newname=input("Enter new Name:")
                        d['Name']=newname
                    if(value==2):
                        newavailable=int(input("Enter new Available items:"))
                        d['Available']=newavailable
                    if(value==3):
                        newprice=int(input("Enter new Price:"))
                        d['Price']=newprice
                    if(value==4):
                        neworiginalprice=int(input("Enter new Original Price:"))
                        d['Original_Price']=neworiginalprice
             
    print("Item updated....")
    if len(temp)==len(dress1):
        print(f"{desired_Id} not found")
    else:
        print(f"{desired_Id}'s one available is removed from the list")
    adminDisplayMenu()
def logout():
    print("You have successfully logged out")

def adminChoice():                                          
    choice=int(input("Please enter user choice : "))
    if choice==1:
        adminDisplayMenu()
        adminLogin()
        adminChoice()
    elif choice==2:
        adminDisplayMenu()
        addItem()
        adminLogin()
        adminChoice()
    elif choice==3:
        adminDisplayMenu()
        removeItem()
        adminLogin()
        adminChoice()
    elif choice==4:
        goods()
        adminLogin()
        adminChoice()
    elif choice==5:
        incomeLoss()
        adminLogin()
        adminChoice()
    elif choice==6:
        update()
        adminLogin()
        adminChoice()
    elif choice==7:
        logout()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        adminLogin()
        adminChoice()

def userLogin():                                          #for user purpose
    print("1.Display Menu")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Logout")
def userDisplayMenu():
    print("Id\tName\tAvailable\tPrice")
    for d in dress:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
def user_id():
    userDisplayMenu()
    p_id=int(input("\nEnter the id : "))
def placeOrder():
    order_number=0
    userDisplayMenu()
    p_id=int(input("\nEnter the id : "))
    for d in dress:
        if d["id"]==p_id:
            m=int(input("\nEnter how many items you want to buy : "))
            print("\nId\tName\tNo of items\tPrice")
            sum=d["Price"]*m
            print(f'{d["id"]}\t{d["Name"]}\t',m,'\t\t',sum)
            order='{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}'
            conform=input("\nDo u wanna CONFIRM your order[Y/N]:")

            if conform=='Y' or conform=='y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["id"],d["Name"]))
                order_number+=1
                print("Your order number is : ",order_number)
                d["Available"]-=m
                break

            elif conform=='N' or conform=='n' :
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform=input("\nDo u wanna CONFIRM your order[Y/N]:")
                break


    if d["id"]!=p_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        user_id()
    print("\nAvailable products : \n")
    userDisplayMenu()

def cancelOrder():
    found=False
    temp=[]
    order_id=input("Enter the id of the order you placed : ")
    for d in dress:
        found=d["id"]==order_id
        if found!=True:
            temp.append(d)
    if len(temp)==d:
        print(f'{order_id} is not found')
    else:
        print(f'{order_id} is removed from the placed order')

def userChoice():
    choice=int(input("Please enter user choice : "))
    if choice==1:
        userDisplayMenu()
        userLogin()
        userChoice()
    elif choice==2:
        placeOrder()
        userLogin()
        userChoice()
    elif choice==3:
        cancelOrder()
        userLogin()
        userChoice()
    elif choice==4:
        logout()
    else:
        print("Invalid Choice. Please enter valid choice")

def login():
    print("WELCOME TO SHOPPER'S DELIGHT")
    print('************************************')
    tp=input("Admin/User [A/U] : ")
    if tp=='A' or tp=='a' :
        password=input("Enter the password : ")
        if password=="admin":
            adminLogin()
            adminChoice()
        else:
            print("Invalid password. Please enter valid password")
    else:
        print("WELCOME TO SHOPPER'S DELIGHT")
        userLogin()
        userChoice()
login()

'''
dress=[{"id":1001,"Name":"Tops","Available":10,"Price":250,"Original_Price":200},
       {"id":1002,"Name":"Pants","Available":12,"Price":500,"Original_Price":450},
       {"id":1003,"Name":"Sarees","Available":100,"Price":750,"Original_Price":700},
       {"id":1004,"Name":"Shorts","Available":20,"Price":350,"Original_Price":300},
       {"id":1005,"Name":"Kurtas","Available":15,"Price":400,"Original_Price":300}]
dress1=dress
temp=[]
order=""
'''

'''THANKYOU'''

