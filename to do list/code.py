tasks = []

def add_task():
    task = input("Enter a task: ")
    task1s.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def remove_task():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        view_tasks()
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")

def todo_list():
    while True:
        print("\n====== TO-DO LIST ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        print()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Thank you for using the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the to-do list application
todo_list()
