# Importing pakages
import streamlit as st
import mysql.connector

from create import create
from database import create_table
from delete import delete
from read import read
from update import update

mydb = mysql.connector.connect(
    host="cc-project.cvcpbdfon0xp.us-east-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    port="3306",             # Replace with your RDS port number, typically 3306 for MySQL
    user="root",           # Replace with your RDS username
    password="tejal0910&",       # Replace with your RDS password
    database="PES2UG20CS370_Train_lab10"
)
c = mydb.cursor()

#c.execute("CREATE DATABASE PES2UG20CS370_Train_Lab10")


def main():
    st.title("Train App")
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add":
        st.subheader("Enter Train Details:")
        create()

    elif choice == "View":
        st.subheader("View created tasks")
        read()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()

    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
