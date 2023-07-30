import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.jpg")

with col2:
    st.title("Arghyadeep Guria")
    content1 = """
Hii, I'm Arghyadeep! I am a Python Programmer, Website Developer, and an AI learner.
I passed my high-school in the year 2022. I'm seeking a job now.
"""
    st.info (content1)

content2 = """
Below you can find some of the apps I Built. Feel free to contact me
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep= ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:]. iterrows():
        st.header(row["title"])