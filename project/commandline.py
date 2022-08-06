from json.decoder import JSONDecodeError
import operations
import json
from json import JSONDecodeError

print("Welcome to Meet app")
tp=open('sellers.json','r+')
try:
    cp=json.load(tp)
    if 'admin@edyoda.com' not in str(cp):
        operations.Register('seller','gamers.json','sellers.json','admin','admin@edyoda.com','admin')
    tp.close()
except JSONDecodeError:
    operations.Register('seller','gamers.json','sellers.json','admin','admin@edyoda.com','admin')
c=1
while True:
    print("Press:")
    print("1: Register")
    print("2: Login")
    print("0: Exit")
    try:
        c=int(input())
    except ValueError:
        print("Please enter valid choice")
        continue
    if c==1:
        print("Press :")
        print("1: Register as seller")
        print("2: Register as gamer")
        try:
            in1=int(input())
        except ValueError:
            print("Please enter valid choice")
        if in1==1:
            print("Enter Full Name:")
            F=input()
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            if (len(F)*len(E)*len(P))==0 or '@' not in E or '.com' not in E:
                print("Please enter valid data")
                continue
            else:
                operations.Register('seller','gamers.json','sellers.json',F,E,P)
                print("Registered successfully as seller")
        elif in1==2:
            print("Enter Full Name:")
            F=input()
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            if (len(F)*len(E)*len(P))==0 or '@' not in E or '.com' not in E:
                print("Please enter valid data")
                continue
            else:
                operations.Register('gamer','gamers.json','sellers.json',F,E,P)
                print("Registered successfully as Gamer")
        else:
            print("Please enter valid choice!")
    elif c==2:
        print("Press: ")
        print("1: Login as Seller")
        print("2: Login as Gamer")
        try:
            in1=int(input())
        except ValueError:
            print("Please enter valid choice")
        if in1==1:
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            s=operations.Login('seller','gamers.json','sellers.json',E,P)
            if s==False:
                print("Invalid Credentials")
                continue
            else:
                t=open('sellers.json','r')
                cnt=json.load(t)
                t.close()
                n=""
                for i in range(len(cnt)):
                    if cnt[i]["Email"]==E and cnt[i]["Password"]==P:
                        n=cnt[i]["Full Name"]
                        break
                print("Welcome "+str(n))
                while True:
                    print("Press :")
                    
                    print("1: Create Products")
                    print("2: View all Products created")
                    print("3: View Product Details by ID")
                    print("4: Update Product")
                    print('5: View User Profile')
                    print("0: Logout")
                    try:
                        i1=int(input())
                    except ValueError:
                        print("Please enter valid choice")
                    if i1==1:
                        prodId=operations.AutoGenerate_prodID()
                        print("prod ID Generated - "+str(prodId))
                        print("Product Title")
                        prodtitle=input()
                        print("Product Type")
                        prodtype=input()
                        print("Price Per Day")
                        prodprice = input()
                        print("Total Stock Available")
                        available = input()
                        try:
            

                            Cap=int(input())
                        except ValueError:
                            print("Please enter valid data")
                            continue
                        else:
                            operations.Create_Product(n,'Products.json',prodId, prodtitle, prodtype,prodprice,available)
                            print("prod created successfully")
                    elif i1==2:
                        pd_details=operations.View_all_products_of_seller(n,'Products.json')
                        print(pd_details)
                        if len(pd_details)==0:
                            print("No prods created yet! \n")
                        else:
                            for i in range(len(pd_details)):
                                print("Product ID: "+str(pd_details[i]['ProductID']))
                                print("Product Name: " +str(pd_details[i]['Product Title']))
                                print("Seller: " +str(pd_details[i]['Seller']))
                                print("Seats Available: "+str(pd_details[i]['Total Stock Available']))
                                print('\n')
                    elif i1==3:
                        print("Enter Product ID")
                        prodId=input()
                        f14=open('Products.json','r')
                        try:
                            c14=str(json.load(f14))
                            if prodId not in c14:
                                print("Invalid prod ID")
                                continue
                        except JSONDecodeError:
                            print("prods not available")
                            continue
                        d=operations.View_prod_ByID('Products.json',prodId)
                        print("prod Title: " +str(d['Product Title']))
                        print("seller: " +str(d['Seller']))
                        print("Seats Available: "+str(d['Total Stock Available']))
                        print('\n')
                    elif i1==4:
                        print("Enter prod ID:")
                        prodId=input()
                        print("Enter detail to be Updated ( Product Title || Product Type || Price Per Day || Total Stock Available ): ")
                        dtl=input()
                        print('Update to:')
                        updtl=input()
                        f11=open('Products.json','r')
                        try:
                            c11=str(json.load(f11))
                            f11.close()
                        except JSONDecodeError:
                            print("No prods created")
                            f11.close()
                            continue
                        if prodId not in c11:
                            print("Invalid prod ID")
                            continue
                        if (len(prodId)*len(dtl)*len(updtl))==0:
                            print("Please enter valid data")
                            continue
                        else:
                            ch=operations.Update_product(n,'Products.json',prodId,dtl,updtl)
                        if ch==False:
                            print("Cannot update prod")
                        else:
                            print("prod updated successfully")
                    elif i1==0:
                        break
                    else:
                        print("Ivalid Option")
        elif in1==2:
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            s=operations.Login('gamer','gamers.json','sellers.json',E,P)
            if s==False:
                print("Invalid Credentials")
                continue
            else:
                t=open('gamers.json','r')
                cnt=json.load(t)
                t.close()
                n=""
                for i in range(len(cnt)):
                    if cnt[i]["Email"]==E and cnt[i]["Password"]==P:
                        n=cnt[i]["Full Name"]
                        break
                print("Welcome "+str(n))
                while True:
                    print("Press:")
                    print("1: View all Product")
                    print("2: Manage wishlist")
                    print("3: Manage cart")
                    print("4: Place order")
                    print("5: Update Profile")
                    print("6: View Orders")
                    print("0: Logout")
                    try:
                        i=int(input())
                    except ValueError:
                        print("Please enter valid choice")
                    if i==1:
                        pd_details=operations.View_all_products('Products.json')
                        print(pd_details)
                        if len(pd_details)==0:
                            print("No prods created yet! \n")
                        else:
                            for i in range(len(pd_details)):
                                print("Product ID: "+str(pd_details[i]['ProductID']))
                                print("Product Name: " +str(pd_details[i]['Product Title']))
                                print("Seller: " +str(pd_details[i]['Seller']))
                                print("Seats Available: "+str(pd_details[i]['Total Stock Available']))
                                print('\n')
                    elif i==2:
                        print('Enter Product Id:')
                        pd_id = input()
                        print('1. Add Item to wishlist')
                        print('2. Remove item from wishlist')
                        j = int(input())
                        l=operations.Manage_Wishlist(n,'gamers.json',j,pd_id)
                        if l:
                            print('Updated Succesfully')
                        else:
                            print('Try again')
                        
                    elif i==3:
                        print('1. Add Item to Cart')
                        print('2. Remove item from Cart')
                        print('3. View Cart')
                        j = int(input())
                        print('Enter Product Id:')
                        pd_id = input()
                        print('Enter Quantity:')
                        pd_quantity = input()
                        print('Enter Booking Startdate:')
                        pd_st = input()
                        print('Enter Booking Enddate:')
                        pd_end = input()
                        x = open('Products.json')
                        content = json.load(x)
                        for i in range(len(content)):
                            if content[i]["ProductID"] == pd_id:
                                pd_price = int(content[i]["Price Per Day"])
                        l=operations.Manage_Cart(n,'gamers.json',j,pd_id,pd_quantity,pd_st,pd_end,pd_price)
                            
                        if l:
                            print('Updated Succesfully')
                        else:
                            print('Try again')
                        
                    elif i==4:
                        l = operations.Place_order(n,'gamers.json','order.json')
                        if l:
                            print('order place succesfully')
                        else:
                            print('Order not placed')
                    elif i==5:
                        print("Enter the detail you want to update Email || Password")
                        data = input()
                        print("Enter the new data")
                        new_data = input()
                        l = operations.Update_Details(n,'gamers.json',data,new_data)
                        if l:
                            print('Updated')
                        else:
                            print('Unsuccesful')
                    elif i==6:
                        f = open('order.json')
                        content = json.load(f)
                        for i in range(len(content)):
                            if content[i]["Gamer"]==n:
                                print(content[i])
                    elif i==0:
                        break
                    else:
                        print("Invalid Choice, Please enter again")
                        continue
    elif c==0:
        break
    else:
        print("Invalid Choice, Please enter again")
        continue
