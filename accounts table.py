import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='mysql12',database='travel_booking')
c1=conn.cursor()
c1.execute('create table accounts(Phone_number int(13) primary key,name varchar(30),password  bigint(10));')
conn.commit()
print("Table  accounts created successfully")
