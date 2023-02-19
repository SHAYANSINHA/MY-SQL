

import mysql.connector
# import mysql.connector
# create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("select * from ineuron.fsds")

for i in mycursor:
    print(i)

#
mycursor.execute("select student_id,first_name,class from ineuron.fsds")

for i in mycursor :

    print(i)  
#
mycursor.execute("select * from ineuron.fsds where student_id = 130")

for i in mycursor :

    print(i) 
#
mycursor.execute("select * from ineuron.fsds where student_id > 130")

for i in mycursor :

    print(i) 
#
mycursor.execute("select * from ineuron.fsds where first_name = 'shubham' and class = 'sql' ")

for i in mycursor :

    print(i) 
#
mycursor.execute("update ineuron.fsds set first_name = 'SHAYAN' where student_id = 125 ")

mydb.commit()            
#
mycursor.execute("update ineuron.fsds set class = 'mysql'")
mydb.commit()
#
mycursor.execute("delete from ineuron.fsds where last_name = 'gupta'")
mydb.commit()
# minimum student_id or very first student_id
mycursor.execute("select min(student_id) from ineuron.fsds")
for i in mycursor :

    print(i) 
# maximum student_id or last student_id .
mycursor.execute("select max(student_id) from ineuron.fsds")
for i in mycursor :
 print(i)  
# try to give count of total record available in entire database.
mycursor.execute("select count(*) from ineuron.fsds")
for i in mycursor :
 print(i)
#
mycursor.execute("update ineuron.fsds set class = 'sql' where student_id between 125 and 128 ")
mydb.commit()
#
mycursor.execute("update ineuron.fsds set class = 'mongodb' where student_id between 129 and 133 ")
mydb.commit()
#
mycursor.execute("select count(*) ,class from ineuron.fsds group by class")
for i in mycursor:
    print(i)
#
"""mycursor.execute("drop table ineuron.fsds")
mydb.commit()"""

#
mycursor.execute("drop database ineuron")
mydb.commit()

 
   




    




      


