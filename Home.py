import streamlit as st
import pandas

st.set_page_config("Arghyadeep Guria's Portfolio", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\copy.png")

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
st.subheader(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep= ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:]. iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")