import mysql.connector
mydb = mysql.connector.connect(
    host="cc-project.cvcpbdfon0xp.us-east-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    port="3306",             # Replace with your RDS port number, typically 3306 for MySQL
    user="root",           # Replace with your RDS username
    password="tejal0910&",       # Replace with your RDS password
    database="PES2UG20CS370_Train_lab10"
)
c = mydb.cursor()
# c.execute("CREATE DATABASE PES2UG20CS370_Train_Lab10")

