# Some Python
print("A TODO APPLICATION")

while True:
    text = input("Select an action: ADD, SHOW, EDIT, COMPLETED or EXIT application -----> ")
    text = text.strip().lower()
    match text:
        case "add":
            todo = input("Add a new task ---> ") + "\n"
            # convert input to lower, then make it titled
            todo.title()
            # Read the txt file and then append new text
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                todos.append(todo)
            # Add write functionality
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            # Below is a list comprehension that strips the extra line
            # todos = [item.strip('\n') for item in todos]
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                # Also strips the extra line
                item = item.strip('\n')
                print(f'{index + 1}. {item}')
        case "edit":
            with open("./todos.txt", 'r') as file:
                todos = file.readlines()
            edit_value = int(input(f"choose the position number 1 - {len(todos)} to edit: "))
            edit_value = (edit_value - 1)
            new_todo = input("type edit here: ") + "\n"
            new_todo = new_todo.title()
            todos[edit_value] = new_todo
            with open('./todos.txt', 'w') as file:
                file.writelines(todos)
        case "completed":
            print("CHOOSE A TASK THAT HAS BEEN COMPLETED")
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            completed_value = int(input(f"choose the position number 1 - {len(todos)} to delete: "))
            completed_value = completed_value - 1
            todos.pop(completed_value)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "exit":
            break
print("Thanks for using the App")
