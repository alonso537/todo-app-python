from functions import get_todos, write_todos
import PySimpleGUI
import time

PySimpleGUI.theme("Black")


clock = PySimpleGUI.Text("", key="clock")
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter a to-do here", key="todo")
list_box = PySimpleGUI.Listbox(values=get_todos(), key="todos", enable_events=True, size=[45, 10])
add_button = PySimpleGUI.Button("Add", size=10)
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")


window = PySimpleGUI.Window('My To-Do App', layout=[
    [[clock], label],
    [input_box, add_button], [list_box, edit_button, complete_button],
    [exit_button]
], font=("Helvetica", 18))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo = values["todos"][0]
                # print(todo)
                new_todo = values["todo"]

                todos = get_todos()
                index = todos.index(todo)
                todos[index] = new_todo + "\n"
                write_todos(todos)
                window["todos"].update(values=get_todos())
            except IndexError:
                PySimpleGUI.popup_error("Please select a todo to edit", font=("Helvetica", 18))
        case "Complete":
            try:
                todo = values["todos"][0]
                todos = get_todos()
                # print(todos)
                todos.remove(todo)
                # print(todos)
                write_todos(todos)
                window["todos"].update(values=todos)
                # window["todos"].update(values="")
            except IndexError:
                PySimpleGUI.popup_error("Please select a todo to complete", font=("Helvetica", 18))
        case "Exit":
            break
        # case 'todos':
        #     window["todo"].update(values=values["todos"][0])
        case PySimpleGUI.WIN_CLOSED:
            break
window.close()
