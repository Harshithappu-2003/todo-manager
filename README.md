# To-Do List Application

A simple and interactive command-line To-Do list application built using Python. This app allows you to manage tasks by creating, viewing, updating the status, and deleting them, with all tasks stored in a `data.json` file. The app uses a color-enhanced interface with ASCII art and user-friendly menus powered by the `inquirer` library.

## Features

- **Add Task**: Create a new task with a name and description.
- **View Tasks**: Display all tasks with their details such as name, description, start date, and status.
- **Delete Task**: Remove a task from the list by selecting its index.
- **Update Status**: Change the status of a task (Mark as completed or pending).
- **Exit Option**: Exit the application gracefully.

## Technologies Used

- **Python**: Main programming language used for the application.
- **JSON**: To store tasks and their data persistently in a `data.json` file.
- **Termcolor**: For displaying colorful text in the terminal.
- **Pyfiglet**: To generate ASCII art for the title.
- **Inquirer**: For creating user-friendly command-line menus with options and selection using arrow keys.

## Setup

1. Clone or download the repository to your local machine.
2. Install the required Python libraries by running the following command:
    (packages to install befor running)
   pip install termcolor pyfiglet inquirer
3. Run the application = python filename.py

## How It Works

The application is built around a ToDoList class, which defines various methods for task management. Here's a breakdown of how the key features work:

1. Add Task
Input: When you select the "Add Task" option, you will be prompted to enter the task name and description.
Processing: The task is stored as a new instance of the ToDoList class, and its data (name, description, start date, status) is saved into a data.json file.
2. View Tasks
Input: By selecting "View Tasks," the program reads all existing tasks from the data.json file.
Processing: Each task is displayed with its name, description, start date, and status (either "Completed" or "Pending"). The tasks are formatted with ASCII art and color for a better visual experience.
3. Delete Task
Input: To delete a task, you will need to provide the index number of the task you want to remove.
Processing: The task at the given index is removed from the list, and the updated list is saved back into the data.json file.
4. Update Task Status
Input: By selecting "Update Status," you will be prompted to enter the index of the task you want to update and choose the new status (either true for completed or false for pending).
Processing: The task’s status is updated, and the changes are saved into the data.json file.
5. Exit
Input: When you select "Exit," the program terminates gracefully, saving all data to the file before closing the app.
