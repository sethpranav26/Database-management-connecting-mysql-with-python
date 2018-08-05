import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",db="customer"
    )
mycursor=mydb.cursor()
def select(a):
    global mycursor
    if a=="record":
        mycursor.execute("select * from record")
    else:
        mycursor.execute("select * from item ")
    return mycursor.fetchall()
def message(a):
    global data
    if(a=='record'):
        print("\n\n***************** Customer Information ****************\n")
        print("cid         Name          Age        Address")
    else:
        print("\n\n********************** Product List **********************\n")
        print("pid         Name          Quantity        Price             Type")
    for row in data:
        for i in range (0,len(row)):
            print(row[i],end="           ")
        print()
def menu1():
    print("\n\nTo display list of all customers press 1 : ")
    print("\To display list of all items press 2 : ")
    print("For customer related querry press 3 : ")
    print("For items related querry press 4 : ")
    print("To Buy an item press 5 : ")
    print("To exit press 6 :")
    a=int(input())
    return a
def menu2():
    print("To display info of particular customer press 1 : ")
    print("To update info of particular customer press 2 : ")
    print("To get info of customers with particular item press 3 : ")
    h=int(input())
    return h
def menu3():
    print("To display info of particular item press 1 : ")
    print("To update info of particular item press 2 : ")
    print("To enter a new item press 3 : ")
    print("To delete a particular item press 4 : ")
    print("To get items of particular type press 5 : ")
    print("To get items in sorted order press 6 :")
    print("To update quantity of item press 7 :")
    h=int(input())
    return h
def menu4():
    print("To get items in increasing order of price press 1 :")
    print("To get items in alpahbetical order of name press 2 :")
    print("To get items in increasing order of quantity press 3 :")
    i=int(input())
    return i
def dis_c():
    global mycursor,data
    data=select("record")
    message("record")
def dis_p():
    global mycursor,data
    data=select("item")
    message("item") 
a=0
while(a>-1):
    b=input("Enter user id : ")
    c=input("Enter password : ")
    mycursor.execute("select * from login where user = %s",(b,))
    data=mycursor.fetchall()
    if data == []:
        print("Enter a valid user name , password " )
    for row in data:
        if c in row:
            a=-2
        else:
            print("Enter a valid user name , password " )

while(a>=-3):
    
    a=menu1()
    if a==6:
        break
    elif a==1:
        dis_c()
    elif a==2:
        dis_p()
    elif a==3:
        h=menu2()
        if h==1:
            print("\n\nEnter cid of customer")
            b=int(input())
            sq="select * from record where cid = %s"
            mycursor.execute(sq,(b,))
            data=mycursor.fetchall()
            if data==[]:
                print("Enter valid information :")
            else:
                message("record")
        elif h==2:
            print("\n\nEnter cid of customer")
            b=int(input())
            c=input("Enter new name ")
            d=int(input("Enter new age : "))
            e=input("Enter new address ")
            sq="update record set name = %s,age=%s,address=%s where cid = %s"
            mycursor.execute(sq,(c,d,e,b))
            mycursor.execute("commit")
            print("Record has been updated \n\nUpdated record is : " )
            sq="select * from record where cid = %s"
            mycursor.execute(sq,(b,))
            data=mycursor.fetchall()
            message("record")
        elif h==3:
            print("Enter pid of item : ")
            i=int(input())
            mycursor.execute("select cid from sale where pid = %s",(i,))
            data1=mycursor.fetchall()
            if data1==[]:
                print("Enter valid information :")
            else:
                print("\n\n***************** Customer Information ****************\n")
                print("cid         Name          Age        Address")
                for row in data1:
                    b=row[0]
                    mycursor.execute("select * from record where cid = %s",(b,))
                    data2=mycursor.fetchall()
                    for row1 in data2:
                        print(row1[0],"          ",row1[1],"         ",row1[2],"       ",row1[3])
    elif a==4:
        h=menu3()
        if h==1:
            print("\n\nEnter pid of item :")
            b=int(input())
            sq="select * from item where pid = %s"
            mycursor.execute(sq,(b,))
            data=mycursor.fetchall()
            if data==[]:
                print("Enter valid information :")
            else:
                message("item")
        elif h==2:
            print("\n\nEnter pid of item")
            b=int(input())
            c=input("Enter new name ")
            d=int(input("Enter new Quantity : "))
            e=int(input("Enter new price "))
            f=input("Enter new tupe ")
            sq="update item set pname = %s,qty=%s,price=%s,ptype=%s where pid = %s"
            mycursor.execute(sq,(c,d,e,f,b))
            mycursor.execute("commit")
            print("Record has been updated \n\nUpdated record is : " )
            sq="select * from item where pid = %s"
            mycursor.execute(sq,(b,))
            data=mycursor.fetchall()
            message("item")
        elif h==3:
            b=int(input("Enter pid of new item : "))
            c=input("Enter name of new item : ")
            d=int(input("Enter Quantity of new item: "))
            e=int(input("Enter price of new item : "))
            f=input("Enter type of new item : ")
            sq="insert into item values(%s,%s,%s,%s,%s)"
            mycursor.execute(sq,(b,c,d,e,f))
            mycursor.execute("commit")
            print("Following record has been added\n")
            sq="select * from item where pid = %s"
            mycursor.execute(sq,(b,))
            data=mycursor.fetchall()
            message("item")
        elif h==4:
            b=int(input("Enter pid of item " ))
            mycursor.execute("delete from item where pid = %s",(b,))
            mycursor.execute("commit")
            print("Item deleted\nNew list of items is \n:")
            dis_p()
        elif h==5:
            b=input("Enter type of product : ")
            mycursor.execute("select * from item where ptype = %s",(b,))
            data=mycursor.fetchall()
            if data==[]:
                print("Enter valid information :")
            else:
                message("item")
        elif h==6:
            i=menu4()
            if i==1:
                mycursor.execute("select * from item order by price")
            elif i==2:
                mycursor.execute("select * from item order by pname")
            elif i==3:
                mycursor.execute("select * from item order by qty")
            data=mycursor.fetchall()
            message("item")
        elif h==7:
            b=int(input("enter pid of item : "))
            c=int(input("enter quantity added to previous one : "))
            mycursor.execute("update item set qty = qty + %s where pid = %s ",(c,b))
            mycursor.execute("commit")
            print("Record has been updated \n\nUpdated record is : " )
            sq="select * from item where pid = %s"
            mycursor.execute(sq,(b,))
            data=mycursor.fetchall()
            message("item")
            
    elif a==5:
        h=input("Are you an existing customer y/n")
        if(h=='y'):
            b=int(input("Enter your cid :"))
            mycursor.execute("select * from record where cid = %s ",(b,))
            data=mycursor.fetchall()
            if data==[]:
                print("Enter a valid cid : ")
            else:
                dis_p()
                c=int(input("Enter pid of item you want to order "))
                d=int(input("Enter quantity of item you want : "))
                mycursor.execute("select * from item where pid=%s",(c,))
                data=mycursor.fetchall()
                if data[0][2]<d:
                    print("\n\nThis much amount of item not available")
                else:
                    mycursor.execute("update item set qty = qty - %s where pid = %s",(d,c))
                    mycursor.execute("commit")
                    mycursor.execute("insert into sale values(%s,%s)",(b,c))
                    mycursor.execute("commit")
                    print("\n\nAmount to be paid = ",data[0][3]*d*0.9)
                    print("Discount = 10%")
        else:    
            b=int(input("Enter cid of new customer : "))
            c=input("Enter name of new customer : ")
            d=int(input("Enter age of new customer: "))
            e=input("Enter address of new customer : ")
            dis_p()
            f=int(input("Enter pid of item you want to order "))
            g=int(input("Enter quantity of item you want : "))
            mycursor.execute("select * from item where pid=%s",(f,))
            data=mycursor.fetchall()
            if data[0][2]<g:
                print("\n\nThis much amount of item not available")
            else:
                sq="insert into record values(%s,%s,%s,%s)"  
                mycursor.execute(sq,(b,c,d,e))
                mycursor.execute("commit")
                mycursor.execute("update item set qty = qty - %s where pid = %s",(g,f))
                mycursor.execute("commit")
                mycursor.execute("insert into sale values(%s,%s)",(b,f))
                mycursor.execute("commit")
                print("\n\nAmount to be paid = ",data[0][3]*g)
                print("Discount = 0%")
            
        
