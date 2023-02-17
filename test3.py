import mysql.connector
sudh = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = sudh.cursor()
cur.execute("select * from test.fsds")

for i in cur :
    print(i)