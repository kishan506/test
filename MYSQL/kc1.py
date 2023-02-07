import mysql.connector as mc
z=mc.connect(host="localhost", user="root", password="",database="python")
print(z)

a=input("Enter Number:")
b=input("Enter user:")
Q4="insert into emp1 values('"+a+"','"+b+"')"
z='insert into emp1 values("'+a+'","'+b+'")'
print(z)

