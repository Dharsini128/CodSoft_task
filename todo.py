import json
import os

FILE_NAME = "todo_list.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("✅ No tasks found.")
        return
    print("\n📋 Your To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["completed"] else "❌ Not Done"
        print(f"{idx}. {task['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task_desc = input("Enter the task description: ")
    tasks.append({"task": task_desc, "completed": False})
    print("📝 Task added!")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark as completed: "))
        tasks[task_no - 1]["completed"] = True
        print("✔️ Task marked as completed!")
    except:
        print("⚠️ Invalid task number!")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no - 1)
        print("🗑️ Task deleted!")
    except:
        print("⚠️ Invalid task number!")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("👋 Exiting... Your tasks are saved.")
            break
        else:
            print("❗ Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
