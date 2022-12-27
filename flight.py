from distutils.util import execute
from sqlite3 import connect
import pandas as pd
import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Gauri@123'
)
print(mydb)



def menu():
    print()
    print("*********************************************")
    print(    "     Flight Management System".center(50) )
    print("*"*126)
    print("1. create table passenger")
    print("2. Add new Passanger detail")
    print("3. Create Table Classtype")
    print("4. add new class type detail")
    print("5. create table food ")
    print("6. add food item detail")
    print("7. Show food menu")
    print("8. search by food item name")
    print("9. Delete food item detail if no more available")
    print("10. revise rates of food items ")
    print("11. create Table luggage")
    print("12. Add new charges for more weights")
    print("13. show all types of seats and their ticket price")
    print("14. show type of seats passenger has chosen and its ticket price")
    print("15. if extra luggage then its Bill")
    print("16. if food item ordered then its Bill")
    print("*********************************************")
    print("*"*126)


     
menu()

def create_passenger():
    c1=connect.cursor()
    c1.execute('create table if not exisits passenger(name varchar(25), address varchar(25), mobile int , returndate date, source varchar(25),destination varchar(25)')
    print('table passenger created')
    
def add_passenger():
    c1=connect.cursor()
    L=[]
    name=input("ENTER NAME: ")
    L.append(name)
    address=input("ENTER ADDRESS:" )
    L.append(address)
    mobile=input("ENTER MOBILE NUMBER: ")
    L.append(mobile)
    rdate=input("ENTER THE RESERVATION DATE: ")
    L.append(rdate)
    source=input("ENTER SOURCE: ")
    L.append(source)
    destination=input("ENTER DESTINATION: ")
    L.append(destination)
    pas=(L)
    sql="insert into passengers(name, address,mobile,rdate,source,destination)"
    c1.execute(sql,pas)
    connect.commit()
    print('Record of Passenger inserted')
    
    
def create_classtype():
    c1=connect.cursor()
    c1.execute('create table if not exists classtype(sno int,classtype varchar(25),rate int')
    print('table classtype created')
      
      
def add_classtype():
    c1=connect.cursor()
    df=pd.read_sql("select * from classtype",connect)
    print(df)
    L=[]
    sno=input("ENTER SERIAL NO.: ")
    L.append(sno)
    itemname=input("ENTER NAME OF CLASS TYPE: ")
    L.append(itemname)
    rate=input("ENTER RATE PER TICKET:")
    L.append(rate)
    ct=(L)
    sql="insert into classtype(sno, classtype,rate)values(%s,%s,%s)"
    c1.execute(sql,ct)
    connect.commit()
    print('Record inserted in classtype')
    
    
def create_food():
    c1=connect.cursor()
    c1.execute('create table if not exists food(sno int, item varchar(25), rate int')
    print('table food created')
    
    
def add_food():
    
    c1=connect.cursor()
    df=pd.read_sql("select * from food",connect)
    print(df)
    L=[]
    sno=input("ENTER SERIAL NO.: ")
    L.append(sno)
    itemname=input("ENTER THE NAME OF THE FOOD ITEM: ")
    L.append(itemname)
    rate=input("ENTER THE RATE OF THE FOOD ITEM PER PIECE: ")
    L.append(rate)
    f=(L)
    sql="insert into food(sno,itemname,rate)values(%s,%s,%s)"
    c1.execute(sql,f)
    connect.commit()
    print('Record inserted in food')
    
def showfoodmenu():
    print('ALL FOOD ITEMS AVAILABLE')
    df=pd.read_sql("select * from food",connect)
    print(df)
    
def search_byfooditem():
    print('ALL FOOD ITEMS AVAILABLE')
    df=pd.read_sql("select * from food",connect)
    print(df)
    a=float(input("enter food item NO. : "))
    qry="select * from food where sno=%s"%(a,)
    df=pd.read_sql(qry,connect)
    print(df)
    connect.commit()
    
def delete_food():
    print('Before any changes in food menu')
    df = pd.read_sql_query("select * from food", connect)
    print(df)
    print()
    print()
    mc = connect.cursor()
    mc.execute("delete from where itemname='samosa'")
    print("record deleted")
    df=pd.read_sql("select * from food".connect)


def revise_foodrate():
    print('Before any changes in Rates')  
    df=pd.read_sql_query("select * from food",connect)
    print(df)
    mc=connect.cursor()
    mc=execute("update food set rate =rate+10 whwere itemname = 'samosa")  
    #connect.commit()
    df=pd.read_sql("select * from food",connect)        
    print(df)    
    
    
    
def create_luggage():
    c1=connect.cursor()
    c1.execute('create table if not exists luggage(sno int,weight varchar(20), rate int')  
    print('table luggage created')
    

def add_luggage():
    c1=connect.cursor()
    df=pd.read_sql_query("select * from luggage",connect)
    print(df)
    L=[]
    sno=input("ENTER Serial NO.: ")
    L.append(sno)
    weight= input("ENTER WEIGHT OF LUGGAGE: ")
    L.append(weight)
    rate=input("ENTER THE RATE OF LUGGAGE: ")
    L.append(rate)    
    lug=(L)
    sql="insert into luggage(sno,weight,rate)values(%s,%s,%s)"
    c1.execute(sql,lug)
    connect.commit()
    print('Record inserted in Luggage')
    
    

def showticketprice():
    print('All records of types of seats available')
    df=pd.read_sql_query("select * from classtype",connect)
    print(df)
    
    
    
def ticketreservation():
    print("WE HAVE THE FOLLOWING SEATS FOR YOU:-")
    print("1. FIRST CLASS RS 6000 per PERSON")
    print("2. BUSINESS CLASS RS 11000 PER PERSON")
    print("3. ECONOMY CLASS RS 5000 PER PERSON")
    print("4. KING ROOM RS 6000 PER PERSON")
    x=int(input("ENTER YOUR CHOICE OF TICKET PLEASE_>"))
    n=int(input("HOW MANY TICKETS YOU NEED: "))
    if(x==1):
        print("YOU HAVE CHOSEN FIRST CLASS")
        s=6000*n 
    elif(x==2):
        print("YOU HAVE CHOSEN BUSINESS CLASS")
        s=11000*n
    elif(x==3):
        print ("YOU HAVE CHOSEN ECONOMY CLASS")
        s=5000*n       
    else:
        print("PLEASE CHOOSE A ROOM")  
    print("YOUR TOTAL TICKET PRICE is =",s,"\n")
       
       

def luggagebill():
    x=int(input("ENTER SERIAL NO. OF WEIGHT OF EXTRA LUGGAGE->"))       
     
    if(x==1):
        print("YOU HAVE 20KG EXTRA")
        s=2000
    elif(x==2):
        print("YOU HAVE 25KG EXTRA")
        s=3500
    elif(x==3):
        print("YOU HAVE 30KG EXTRA")
        s=4000
    elif(x==4):
        print("YOU HAVE 35KG EXTRA")
        s=5000
    elif(x==5):
        print("YOU HAVE 40KG EXTRA")
        s=6000
    else:
        print("PLEASE CHOOSE A CORRECT serial No. ")
    print("your cost of extra luggage is",s)
    
    
    
def foodbill():
    print('ALL FOOD ITEMS AVAILABLE')
    df=pd.read_sql("select * from food", connect)
    print(df)
    
    c=int(input("order you ITEM NO.: "))
    d=int(input("enter the quantity:"))
    if (c==1):
        s=20 *d
    elif(c==2):
        s=30*d
    elif(c==3):
        s=60*d
    elif(c==4):
        s=100*d
    elif(c==5):
        s=150*d
    else:
        print("invalid option")
    print("total food Bill = Rs", s, "\n")
    
    
opt=""
opt=int(input("enter your choice : "))
if opt==1:
    create_passenger()
elif opt==2:
    add_passenger()
elif opt==3:
    create_classtype()
elif opt==4:
    add_classtype()
elif opt==5:
    create_food()
elif opt==6:
    add_food()
elif opt==7:
    showfoodmenu()
elif opt==8:
    search_byfooditem()
elif opt==9:
    delete_food()
elif opt==10:
    revise_foodrate()
elif opt==11:
    create_luggage()
elif opt==12:
    add_luggage()
elif opt==13:
    showticketprice()
elif opt==14:
    ticketreservation()
elif opt==15:
    luggagebill()
elif opt==16:
    foodbill()
else:
    print('invalid option')        

                                           
                          
            