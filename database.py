import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='mysql12')
c1=conn.cursor()
if conn.is_connected:
    c1.execute("create database travel_booking")
    print("database created successfully")
