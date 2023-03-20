FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Reads the todos from the file and returns them as a list"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos( todos_local, filepath=FILEPATH):
    """Writes the todos to the file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


if __name__ == "__main__":
    print("Welcome to the todo app")
    print("Enter your action: ")