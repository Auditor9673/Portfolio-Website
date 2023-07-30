import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.jpg")

with col2:
    st.title("Arghyadeep Guria")
    content = """
Hii, I'm Arghyadeep! I am a Python Programmer, Website Developer, and an AI learner. I passed my high-school in the year 2022.
I'm seeking a job now.
"""
    st.info (content)