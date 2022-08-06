import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_prodID():
    #generate a random prod ID
    Prod_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Prod_ID

def Register(type,gamer_json_file,seller_json_file,Full_Name,Email,Password):
    '''Register the gamer/ogranizer based on the type with the given details'''
    if type.lower()=='seller':
        f=open(seller_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(gamer_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password,
            'Wishlist' : [],
            'Cart':[],
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()


def Login(type,gamer_json_file,seller_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='seller':
        f=open(seller_json_file,'r+')
    else:
        f=open(gamer_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Product(seller,prod_json_file,prodId, prodtitle, prodtype,prodprice,available):
    '''Create an prod with the details entered by seller'''
    d = {
        'ProductID' : prodId,
        'Product Title': prodtitle,
        'Product Type' : prodtype,
        'Price Per Day' : prodprice,
        'Total Stock Available' : available,
        'Seller':seller
    }
    f = open(prod_json_file,'r+')
    content=json.load(f)
    content = list(content)
    try:
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,f)
    f.close()

def Update_product(seller,prod_json_file,prod_id,detail_to_be_updated,updated_detail):
    '''Update prod by ID || Take the key name to be updated from gamer, then update the value entered by user for that key for the selected prod
    || Return True if successful else False'''
    f = open(prod_json_file,'w')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["ProductID"]==prod_id and content[i]["Seller"]==seller:
            content[i][detail_to_be_updated] = updated_detail
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            return True
    f.close()
    return False

def View_all_products(prod_json_file):
    '''Read all the prods created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(prod_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details
    
def View_all_products_of_seller(seller,prod_json_file):
    '''Read all the prods created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(prod_json_file,'r')
    try:
        content=json.load(f)
        content = list(content)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        print(content[i])
        '''if content[i]['Seller']==seller:
            details.append(content[i])'''
    return content

def View_prod_ByID(prod_json_file,prod_id):
    '''Return details of the prod for the prod ID entered by user'''
    f = open(prod_json_file,'r+')
    prod = {}
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return {}
    for i in range(len(content)):
        if content[i]["ProductID"]==prod_id:
            return content[i]
    f.close()
    return {}

def Manage_Wishlist(gamer,gamer_json,input,prod_id):
    f = open(gamer_json,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Full Name"]==gamer and input==1:
            print(content[i]["Wishlist"])
            content[i]["Wishlist"].append(prod_id)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            return True
        else:
            if prod_id in content[i]['Wishlist']:
                content[i]['Wishlist'].remove(prod_id)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                return True
            
    f.close()
    return False

def Manage_Cart(gamer,gamer_json,input,prod_id,pd_quantity,pd_st,pd_end,pd_price):
    f = open(gamer_json,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Full Name"]==gamer and input==1:
            content[i]["Cart"].append([prod_id,pd_quantity,pd_st,pd_end,pd_price])
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            return True
        elif input ==3:
            print(content[i]["Cart"])
        else:
            if [prod_id,pd_quantity,pd_st,pd_end,pd_price] in content[i]['Cart']:
                content[i]['Cart'].remove([prod_id,pd_quantity,pd_st,pd_end,pd_price])
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                return True
            
    f.close()
    return False

def Place_order(gamer,gamers_json,order_json):
    f = open(gamers_json,'r')
    f1 = open(order_json,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        f1.close()
        return False
    for i in range(len(content)):
        if content[i]["Full Name"]==gamer :
            for j in range(len(content[i]["Cart"])):
                user = gamer
                pd_id = content[i]["Cart"][j][0]
                pd_quantity = content[i]["Cart"][j][1]
                pd_st = int(content[i]["Cart"][j][2])
                pd_end = int(content[i]["Cart"][j][3])
                pd_price = content[i]["Cart"][j][4]
                order_details = {
                    'Gamer':user,
                    'Total Price' : int(pd_price)*int(pd_quantity)*(pd_end-pd_st),
                    'Product ID':pd_id,
                    'Product Quantity':pd_quantity,
                    
                }
                f1.seek(0)
                f1.truncate()
                json.dump(order_details,f1)
                return True
    f.close()
    f1.close()
    return False
    
    

def Update_Details(gamer,gamers_json_file,data,new_data):
    f=open(gamers_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Full Name"]==gamer:
            content[i][data]== new_data
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            return True
    f.close()
    return False
            
       
    '''#$Update the password of the gamer by taking a new passowrd || Return True if successful else return False
'''
    

def View_all_products(prod_json_file):
    '''#Read all the prods created | DO NOT change this function
'''
    '''#Already Implemented Helper Function
'''
    details=[]
    f=open(prod_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details

