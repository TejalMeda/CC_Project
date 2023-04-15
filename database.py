import mysql.connector

mydb = mysql.connector.connect(
    host="ycc-project.cvcpbdfon0xp.us-east-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    port="3306",             # Replace with your RDS port number, typically 3306 for MySQL
    user="root",           # Replace with your RDS username
    password="ytejal0910&",       # Replace with your RDS password
    database="PES2UG20CS370_Train_lab10"
)
c = mydb.cursor()



def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS PES2UG20CS370_Train (Train_No int, Name varchar(30), Train_Type varchar(20), Source varchar(20), Destination varchar(20), Availability varchar(5));')


def add_data(Train_no,Name,Train_type,source,Destination,Availability):
    c.execute('INSERT INTO PES2UG20CS370_Train(Train_no,Name,Train_type,source,Destination,Availability) VALUES (%s,%s,%s,%s,%s,%s)',(Train_no, Name, Train_type, source, Destination, Availability))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM PES2UG20CS370_Train')
    data = c.fetchall()
    return data


def view_only_Train_names():
    c.execute('SELECT Name FROM PES2UG20CS370_Train')
    data = c.fetchall()
    return data


def get_Train(Product_name):
    c.execute('SELECT * FROM PES2UG20CS370_Train WHERE Name="{}"'.format(Product_name))
    data = c.fetchall()
    return data


def edit_Train_data(new_Train_no,new_Name,new_Train_type,new_source,new_Destination,new_Availability,Train_no,Name,Train_type,source,Destination,Availability):
    c.execute("UPDATE PES2UG20CS370_Train SET Train_No=%s,Name=%s,Train_Type=%s,Source=%s,Destination=%s,Availability=%s WHERE Train_No=%s and Name=%s and Train_Type=%s and Source=%s and Destination=%s and Availability=%s", (new_Train_no, new_Name, new_Train_type, new_source, new_Destination, new_Availability, Train_no, Name, Train_type, source, Destination, Availability))

    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(product_name):
    c.execute('DELETE FROM PES2UG20CS370_Train WHERE Name="{}"'.format(Product_name))
    mydb.commit()
