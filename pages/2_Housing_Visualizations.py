import streamlit as st
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "housing11.csv")
df = pd.read_csv(DATA_PATH)

st.title("Dashboard - Housing Data")
furnishingstatus = st.selectbox("Select the status of house:", df['furnishingstatus'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['furnishingstatus'] == furnishingstatus], x="price")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['furnishingstatus'] == furnishingstatus], y="area")
col2.plotly_chart(fig_2, use_container_width=True)

chart_data = pd.DataFrame(df,columns=['parking', 'stories'])
st.line_chart(chart_data)
