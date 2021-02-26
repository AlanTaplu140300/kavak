import mysql.connector

#Creamos la conexión 
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)
print(database)
cursor = database.cursor()
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)