import mysql.connector
#hacking user name= man' or '1'='0
z=mysql.connector.connect(host="localhost",user="root",password="",database="python")
c=z.cursor()
a=input("enter the name :")
b=input("enter the password :")
z1="select * from  emp4 where name=%s  and pass=%s"
 
b=(a,b)
c.execute(z1,b)
temp=c.fetchone()
#print(temp)
if temp==None:
    print("id and password is invalid or missed match")
else:
    print("your most welcome")
#'''