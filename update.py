import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_Train_names, get_Train, edit_Train_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Train_no','Name','Train_type','source','Destination','Availability'])
    with st.expander("Current Train"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_Train_names()]
    selected_train = st.selectbox("Train to Edit", list_of_trains)
    selected_result = get_Train(selected_train)
    # st.write(selected_result)
    if selected_result:
        Train_no = selected_result[0][0]
        Name = selected_result[0][1]
        Train_type = selected_result[0][2]
        source = selected_result[0][3]
        Destination = selected_result[0][4]
        Availability = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_Train_no = st.text_input("Train_no:", Train_no)
            new_Name = st.text_input("Name:", Name)
        with col2:
            new_Train_type = st.selectbox(Train_type, ["Superfast", "Fast", "Mail"],key='newTrainType')
            new_source = st.text_input("source:", source)
            new_Destination = st.text_input("Destination:", Destination)
            new_Availability = st.selectbox("Availability",["yes","no"], key='new_avail_key')
        if st.button("Update Train"):
            edit_Train_data(new_Train_no,new_Name,new_Train_type,new_source,new_Destination,new_Availability,Train_no,Name,Train_type,source,Destination,Availability)
            st.success("Successfully updated:: {} to ::{}".format(Name, new_Name))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Train_no','Name','Train_type','source','Destination','Availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)
