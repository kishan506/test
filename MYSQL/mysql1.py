import mysql.connector as p

cn=p.connect(host="localhost",user="root",password="",database="python")
print(cn)
cur=cn.cursor()
a=int(input("enter old id :"))

#c=input("enter sal :")
#z="insert into emp2 values('"+str(a)+"','"+b+"','"+c+"')"
#x="update emp2 set id='"+b+"' where id ='"+str(a)+"'"
y="select * from emp1"
#print(y)
cur.execute (y)
x=cur.fetchall()
print(x)  
#cn.commit()