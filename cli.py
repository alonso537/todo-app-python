
# todos = [
#     "Buy milk",
#     "Go to the gym",
#     "Learn Python",
#     "Go to the store",
#     "Go to the park",
# ]


from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S", time.localtime())
print("Welcome to the todo app" + " " + now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        try:
            todo = user_action.split("add ")[1]

            todos = get_todos()
            todos.append(todo + "\n")

            write_todos(todos_local=todos)
        except IndexError:
            print("Invalid action")

    elif user_action.startswith("show"):
        try:
            todos = get_todos()

            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}-{item}")
        except FileNotFoundError:
            print("No todos yet")
    elif user_action.startswith("edit"):
        try:
            index = int(user_action.split("edit ")[1])
            index = index - 1

            todos = get_todos()

            if index < 0 or index >= len(todos):
                print("Invalid index")
                continue
            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo

            write_todos(todos_local=todos)
        except ValueError:
            print("Invalid index")
            continue
    elif user_action.startswith("complete"):
        try:
            index = int(user_action.split("complete ")[1])
            index = index - 1

            todos = get_todos()
            if index < 0 or index >= len(todos):
                print("Invalid index")
                continue
            todos.pop(index)

            write_todos(todos_local=todos)

            message = f"Todo {index + 1} completed successfully! and removed from the list"
            print(message)
        except ValueError:
            print("Invalid index")

    elif user_action.startswith("exit"):
        try:
            break
        except ValueError:
            print("Invalid index")
    else:
        print("Invalid action")

print('Bye!')

