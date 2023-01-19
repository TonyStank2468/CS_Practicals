import mysql.connector as sq
mycon = sq.connect(host = "localhost", user = "root", passwd = "Admin@123", database = "employee")
cursor = mycon.cursor()
cursor.execute("SELECT * FROM emp WHERE esalary BETWEEN 30000 AND 55000")
data = cursor.fetchall()
for rec in data:
    print(rec)
    mycon.close()