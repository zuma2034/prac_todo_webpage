def open_file(filename="p_todo.txt"):
    with open(filename,"r") as f:
        todos = f.readlines()
        return todos


def write_file(todo_arg,filename="p_todo.txt"):
    with open(filename,"w") as f:
        f.writelines(todo_arg)

