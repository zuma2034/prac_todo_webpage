import streamlit as st
import pract_func


todos = pract_func.open_file()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    pract_func.write_file(todos)



st.title("my to do app")
st.subheader("this is my first todo app")
st.write("this app is to increase your productivity")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        pract_func.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ",placeholder="add a new todo",on_change=add_todo,key="new_todo")

