import json
import os

FILE = "todos.json"

def load_todos():
    if os.path.exist(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f, indent=2)

def show_todos(todos):
    if not todos:
        print("No task yet.")
        return
    for i, todo in enumerate(todos, start=1):
        status = "✔" if todo["done"] else " "
        print(f"{i}. [{status}] {todo['task']}")

def main():
    todos = load_todos()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View | 2. Add | 3. Complete | 4.Delete | 5.Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            task = input("New task: ").strip()
            if task:
                todos.append({"task": task, "done":False})
                save_todos(todos)
                print("Added.")
        elif choice == "3":
            show_todos(todos)
            try:
                num = int(input("Task number to mark done: "))
                todos[num - 1]["done"] = True
                save_todos(todos)
            except (ValueError, IndexError):
                print("Invalid number.")
        elif choice == "4":
            show_todos(todos)
            try:
                num = int(input("Task number to delete: "))
                todos.pop(num - 1)
                save_todos(todos)
                print("Delete.")
            except (ValueError, IndexError):
                print("Invalid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()