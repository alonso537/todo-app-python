import streamlit as st
from functions import get_todos, write_todos
todos = get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    st.session_state.clear()
    write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase my productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add a new todo", placeholder="Enter a new todo", on_change=add_todo, key="new_todo")
