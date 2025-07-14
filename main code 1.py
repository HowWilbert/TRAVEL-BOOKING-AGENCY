import mysql.connector as sql
from tabulate import tabulate
conn=sql.connect(host='localhost',user='root',password='mysql12',database='travel_booking')
c1=conn.cursor()
conn.autocommit==True
#time
from time import gmtime, strftime
n=strftime("%a, %d %b %Y", gmtime())
n=str(n)
today=n[5:]


print('\t\t','________AB TRAVELS welcomes U!!!!!!__________')
print()
print('                                   ',n)
print()
print('Press 1 to Login') #admin 
print('Press 2 Create account')
print("press 3 delete account")
print('Press 4 to Exit')
print()
while(True):
    choice=int (input('Enter your choice='))

    if choice ==1:
                    chs=int(input('Enter your Choice\n1).Login as User\n2). Login as Admin\n'))
                    if chs==1: #USER LOGIN
                        print()
                        a=int(input('Enter your phone number='))
                    #Name of the person
                        u=("select  name from accounts where phone_number = "+str(a)+";")
                        c1.execute(u)
                        datan=c1.fetchall()
                        s=c1.rowcount
                        s=abs(s)   
                        if s!= 1:
                            print()
                            print("***********************ACCOUNT DOESN'T EXIST************************")
                            print()
                            create=int(input("Press 32 to create account {{or}} Press 0 to exit="))
                            if create==32:
                                phone_number=int(input('Phone Number='))
                                name=str(input('Name='))
                                password =str(input( 'password[10]='))
                                c1.execute("insert into accounts(Phone_number,password,name )values(" + str(phone_number) +",'" +password  + "',' "+name+" ')")
                                conn.commit()
                                print('Account sucessfully Created')
                                import sys
                                sys.exit()
                            else:
                                import sys
                                sys.exit()
                    
                
                        datan=datan[0]
                        datan=list(datan)
                        datan= datan[0]
                        datan= str(datan)
               
                
                #password
                        y="select password from accounts where phone_number =({})".format(a)
                        c1.execute(y)
                        data=c1.fetchall()
                        data=data[0]
                        data=list(data)
                        data=data[0]

                        b=int(input('Enter your password='))
                        if b!=data:
                            print()
                            print("***********************INVALID PASSWORD**************************")
                        conn.commit()
                    

        
                        if b==data:
                            print()
                            print("LOGGED  IN !!!!!")
                            print()
                            print("HI",datan,"!!")   #datan gets the name of the user
                            print()
                            print("What can I do for you?")
                            print()
                        #CHOICE1
                            print('1)Book for a board')
                            print('2).Bill verification')
                            print('3).My travel log')
                            print('0.Exit')
                            print()
                            choice1=int(input('Enter Your Choice='))
                            if choice1==0:
                                print()
                                print("Thank you , Visit again !!")
                                import sys
                                sys.exit()
                
                            if choice1==1:
                            #Booking for Board
                                your_location=input('Your_location=')
                                your_destination=input('Your_destination=')
                                time=input('time to start board=')
                                driver=input("driver gender preferences=")
                                urgency=input('urgency(yes/no)=')
                                c1.execute("insert into customer_bookings values(" + str(a) +",' " +  your_location + " ' ,'  "+your_destination+ " ' ,' "+time+ " ' ,' "+driver+" ' ,' "+urgency+" ',' "+today+" ' )")
                                conn.commit()
                                print()
                                print('********************************AT YOUR SERVICE AT',time,"********************************")
                                import sys
                                sys.exit()
                       
                        
                            if choice1==2:
                         #Bill Verification
                                Dist=int(input('distance travelled [km]='))
                                bill=Dist*5
                                print('your payment =Rs.',bill)
                            if choice1==3:
                            #my travel vlog
                                    c1.execute("select* from customer_bookings where phone_number = "+str(a)+";")
                                    print(tabulate(c1,headers=['Phone_number','Your_location','Your_destination','Time','Driver(gender)','Urgency','Date_booked'], tablefmt='psql'))
                                    data=c1.fetchall()
                                    for i in data:
                                        print(i)
                            else:
                                    print()
                                    print()
                                    print("********************INVALID CHOICE**********************")
                            import sys
                            sys.exit()
                    if chs==2:
                        A_pass=input('Enter Password = : ')
                        if A_pass=='Adminpass':
                            print("\tWELCOME ADMIN!!\t")
                            print('\t1).View Records\n\t2).Insert records\n\t3).Delete Record\n')
                            b=int(input('Enter your choice : '))
                            if b == 1:#view records
                                en=input('Enter table name to be displayed...')
                                if en=='accounts':
                                    c1.execute('select* from accounts')
                                    print(tabulate(c1,headers=['Phone_number','name','password'], tablefmt='psql'))
                                    data=c1.fetchall()
                                    for i in data:
                                        print(i)
                                if en=='customer_bookings':
                                    c1.execute('select* from customer_bookings')
                                    print(tabulate(c1,headers=['Phone_number','Your_location','Your_destination','Time','Driver(gender)','Urgency','Date_booked'], tablefmt='psql'))
                                    data=c1.fetchall()
                                for i in data:
                                    print(i)
                            if b==2:#insert records in Accounts
                                ans='yes'
                                while ans=='yes':
                                    phone_number=int(input('Phone Number='))
                                    name=str(input('Name='))
                                    password =str(input( 'password[10]='))
                                    sql_insert="insert into accounts values(%s,'%s','%s')"%(phone_number,name,password)
                                    c1.execute(sql_insert)           
                                    conn.commit()
                                    ans=input('Want to Enter more records...')
                                    if ans in 'no':
                                        break
                                c1.execute('select* from accounts')
                                print(tabulate(c1,headers=['Phone_number','Name','Password'], tablefmt='psql'))
                                data=c1.fetchall()
                                for i in data:
                                    print(i)
                            if b==3:
                                try:
                                    en=input('Enter table name to be modified:')
                                    if en=='accounts':
                                        y=input('Enter Phone_number of the record to be deleted...')
                                        query='Delete from accounts where Phone_number='+y
                                        c1.execute(query)
                                        conn.commit()
                                        e=c1.rowcount
                                        if e>0:
                                            print('Deletion done')
                                        else:
                                            print('Phone_number',y,' not found')

                                    elif en=='customer_bookings':
                                        y=input('Enter Phone_number of the record to be deleted...')
                                        query='delete from customer_bookings where Phone_number='+y
                                        c1.execute(query)
                                        conn.commit()
                                        e=c1.rowcount
                                        if e>0:
                                            print('Deletion done')
                                        else:
                                            print('Phone_number',y,' not found')
                                except:
                                    print('Something went wrong')
                        else:
                            print('Invalid Choice')
                    
                          
    if choice==2:
        phone_number=int(input('Phone Number='))
        name=str(input('Name='))
        password =str(input( 'password[10]='))
        c1.execute("insert into accounts(Phone_number,password,name )values(" + str(phone_number) +",'" +password  + "',' "+name+" ')")
        conn.commit()
        print('Account sucessfully Created')
        import sys
        sys.exit()

    if choice==3:
        phone_number=int(input("enter your phone_number="))
        c1.execute("delete from customer_bookings where phone_number ="+str(phone_number)+";")
        c1.execute("delete from accounts where phone_number ="+str(phone_number)+";")
        conn.commit()
        print()
        print("**************************************SUCCESSFULLY ACCOUNT DELETED**************************************")
        import sys
        sys.exit()
    
    if choice==4:
        import sys
        sys.exit()
   

    if choice!=1 or 2 or 3:
        print()
        print()
        print("********************INVALID CHOICE**********************")
