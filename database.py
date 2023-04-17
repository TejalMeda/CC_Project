# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="cc-project.cvcpbdfon0xp.us-east-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    port="3306",             # Replace with your RDS port number, typically 3306 for MySQL
    user="root",           # Replace with your RDS username
    password="tejal0910&",       # Replace with your RDS password
    database="PES2UG20CS370_Train_lab10"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS TRAIN(train_no TEXT, train_name TEXT, train_type TEXT, '
              'train_source TEXT,train_destination TEXT,train_availability TEXT)')


def add_data(train_no, train_name, train_type, train_source, train_destination,train_availability):
    c.execute('INSERT INTO TRAIN(train_no, train_name, train_type, train_source, train_destination,train_availability) VALUES (%s,%s,%s,'
              '%s,%s,%s)',
              (train_no, train_name, train_type, train_source, train_destination,train_availability))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM TRAIN')
    data = c.fetchall()
    return data


def view_only_dealer_names():
    c.execute('SELECT train_no FROM TRAIN')
    data = c.fetchall()
    return data


def get_dealer(train_name):
    c.execute('SELECT * FROM TRAIN WHERE train_name="{}"'.format(train_name))
    data = c.fetchall()
    return data


def edit_dealer_data(new_train_no, new_train_name, new_train_type, new_train_source, new_train_destination,new_train_availability,train_no, train_name, train_type, train_source, train_destination,train_availability):
    c.execute("UPDATE TRAIN SET train_no=%s, train_name=%s, train_type=%s, train_source=%s, train_destination=%s, train_availability=%s WHERE "
              "train_no=%s and train_name=%s and train_type=%s and train_source=%s and train_destination=%s and train_availability=%s", (new_train_no, new_train_name, new_train_type, new_train_source, new_train_destination,new_train_availability,train_no, train_name, train_type, train_source, train_destination,train_availability))
    mydb.commit()




def delete_data(train_no):
    c.execute('DELETE FROM TRAIN WHERE train_no="{}"'.format(train_no))
    mydb.commit()
