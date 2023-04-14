import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        Train_no = st.text_input("Number:")
        Name = st.text_input("Name:")
        Train_type = st.text_input("Train_type:")
    with col2:
        source = st.selectbox("Source", ["Bangalore", "Chennai", "Mumbai","Managaluru"],key='source')
        Destination = st.selectbox("Destination", ["Bangalore", "Chennai", "Mumbai","Managaluru"],key='Dest')
        Availability = st.radio("Availability", ["Yes", "No"])
    if st.button("Add Train"):
        add_data(Train_no, Name, Train_type, source, Destination, Availability)
        st.success("Successfully added Train: {}".format(Name))
