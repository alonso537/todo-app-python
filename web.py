import streamlit as st
from functions import get_todos, write_todos

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase my productivity.")

for todo in get_todos():
    st.checkbox(todo)

st.text_input(label="Add a new todo", placeholder="Enter a new todo")
