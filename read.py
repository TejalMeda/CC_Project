import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Train_no','Name','Train_type','source','Destination','Availability'])
    with st.expander("View all Trains"):
        st.dataframe(df)
    with st.expander("Train details"):
        train_df = df['Availability'].value_counts().to_frame()
        train_df = train_df.reset_index()
        st.dataframe(train_df)
        p1 = px.pie(train_df, names='index', values='Availability')
        st.plotly_chart(p1)