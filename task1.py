import tkinter as tk
from tkinter import messagebox
import sys

# The task manager class that handles the to-do list operations
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task and task not in self.tasks:
            self.tasks.append(task)
            return True
        return False

    def update_task(self, old_task, new_task):
        if old_task in self.tasks and new_task and old_task != new_task:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            return True
        return False

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False

    def get_tasks(self):
        return self.tasks

# Command-line interface
def command_line_interface():
    task_manager = TaskManager()
    
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter a new task: ")
            if task_manager.add_task(task):
                print("Task added.")
            else:
                print("Task cannot be empty or is a duplicate.")
        
        elif choice == '2':
            old_task = input("Enter task to update: ")
            new_task = input("Enter new task: ")
            if task_manager.update_task(old_task, new_task):
                print("Task updated.")
            else:
                print("Update failed. Task does not exist or new task is invalid.")
        
        elif choice == '3':
            task = input("Enter task to remove: ")
            if task_manager.remove_task(task):
                print("Task removed.")
            else:
                print("Task not found.")
        
        elif choice == '4':
            tasks = task_manager.get_tasks()
            if tasks:
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks found.")
        
        elif choice == '5':
            print("Exiting program.")
            sys.exit()
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# GUI interface
def gui_interface():
    task_manager = TaskManager()

    def add_task():
        task = entry.get()
        if task_manager.add_task(task):
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty or is a duplicate.")

    def remove_task():
        selected_task = listbox.curselection()
        if selected_task:
            task = listbox.get(selected_task)
            task_manager.remove_task(task)
            listbox.delete(selected_task)

    def update_task():
        selected_task = listbox.curselection()
        if selected_task:
            old_task = listbox.get(selected_task)
            new_task = entry.get()
            if task_manager.update_task(old_task, new_task):
                listbox.delete(selected_task)
                listbox.insert(selected_task, new_task)
                entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Update failed. Invalid task.")

    root = tk.Tk()
    root.title("To-Do List")

    entry = tk.Entry(root, width=50)
    entry.pack(pady=20)

    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack(pady=5)

    update_button = tk.Button(root, text="Update Task", command=update_task)
    update_button.pack(pady=5)

    remove_button = tk.Button(root, text="Remove Task", command=remove_task)
    remove_button.pack(pady=5)

    listbox = tk.Listbox(root, width=50)
    listbox.pack(pady=20)

    root.mainloop()

# Main function to toggle between interfaces
if __name__ == "__main__":
    mode = input("Choose interface mode (cli/gui): ").strip().lower()
    if mode == 'cli':
        command_line_interface()
    elif mode == 'gui':
        gui_interface()
    else:
        print("Invalid mode chosen.")
