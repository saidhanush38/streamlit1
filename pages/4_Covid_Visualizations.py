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

DATA_PATH = os.path.join(dir_of_interest, "data", "covid11.csv")
df = pd.read_csv(DATA_PATH)

st.title("Dashboard - Covid Data")

df1 = pd.DataFrame(df,columns=['LATITUDE','LONGITUDE'])
st.map(df1)


State = st.selectbox("Select the state:", df['State'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['State'] == State], x="Total Confirmed cases")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['State'] == State], y="Death")
col2.plotly_chart(fig_2, use_container_width=True)
