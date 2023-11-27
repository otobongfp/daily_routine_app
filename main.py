# Some Python
print("A TODO APPLICATION")
todos = []

while True:
    text = input("Select an action: ADD, SHOW, EDIT, COMPLETED or EXIT application -----> ")
    text = text.strip().lower()
    match text:
        case "add":
            todo = input("Add a new task --> ")
            todo = todo.title()
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f'{index + 1}. {item}')
        case "edit":
            edit_value = int(input(f"choose the position number 1 - {len(todos)} to edit: "))
            edit_value = (edit_value - 1)
            new_todo = input("type edit here: ")
            new_todo = new_todo.title()
            todos[edit_value] = new_todo
        case "completed":
            print("CHOOSE A TASK THAT HAS BEEN COMPLETED")
            completed_value = int(input(f"choose the position number 1 - {len(todos)} to delete: "))
            completed_value = completed_value - 1
            todos.pop(completed_value)
        case "exit":
            break
print("Thanks for using the App")
