#class -to do list

## create tasks, view tasks, update status of the tasks, delete tasks

## storing all our to-dos in json file

## good using colors and ascii art ..and using inquirer to avoid manual typing

# exit option so that when user clicks app stops

# future enhancements: replace data.json with a database and use flask and streamlit

## add more features to make it complex and different from others!

## inquirer, pyfiglet, termcolor - pip install <name>

## termcolor: it allows to display colored texts

## inquirer: allows selection through up/down arrows <

## pyfiglet: it's used for generating ascii art

# Importing libraries
import json
from datetime import datetime
from termcolor import colored
import pyfiglet
import inquirer

# Creating a class
class ToDoList:
    file_path = 'data.json' #class variables

    # Constructor
    def __init__(self, name, desc, datestart=None, status=False):
        # To-do attributes: name, description, start date, status
        self.name = name
        self.desc = desc
        self.datestart = datestart if datestart else str(datetime.now().date())
        self.status = status

    # Dunder method to customize string representation of ToDoList object
    def __str__(self):
        status_str = 'Completed' if self.status else 'Pending'
        return (f"ToDo: {self.name}\n"
                f"Description: {self.desc}\n"
                f"Start Date: {self.datestart}\n"
                f"Status: {status_str}")

    # Static method to read data from the JSON file
    @staticmethod
    def read_data():
        try:
            with open(ToDoList.file_path, "r") as file:
                # json.load -> JSON string to Python object
                return json.load(file)
        except Exception:
            # If the file doesn't exist or there's an error, return an empty list
            return []

    # Static method to load tasks from JSON into ToDoList objects
    @staticmethod
    def load_tasks():
        """
        Loads tasks from the JSON file and returns a list of ToDoList objects.

        Example structure in JSON:
        [
            { "name": "to-do1", "desc": "Task description", "datestart": "2024-11-30", "status": false },
            { "name": "to-do2", "desc": "Another task", "datestart": "2024-12-01", "status": true }
        ]
        """
        data = ToDoList.read_data()
        # Convert each dictionary from the JSON file to a ToDoList object
        return [ToDoList(**task) for task in data]

    # Method to add a new task
    def add_task(self):
        data = ToDoList.read_data()
        data.append(self.__dict__)  # Convert the object's attributes to a dictionary
        try:
            with open(ToDoList.file_path, "w") as file:
                json.dump(data, file, indent=2)
        except Exception as e:
            print(f"Error while saving task: {e}")

    # Static method to delete a task
    @staticmethod
    def delete_task(index):
        data = ToDoList.read_data()
        try:
            data.pop(index - 1)  # Remove the task at the given index (1-based)
            with open(ToDoList.file_path, "w") as file:
                json.dump(data, file, indent=2)
        except IndexError:
            print(f"Error: No task at index {index}")
        except Exception as e:
            print(e)
            
    #chaning status
    @staticmethod
    def updatestatus(index, new_status) :
        data = ToDoList.read_data()
        try:
            data[index - 1]['status'] = new_status
            with open(ToDoList.file_path, "w") as file:
                json.dump(data, file, indent=2)
        except IndexError:
            print(f"Error: No task at index {index}")
        except Exception as e:
            print(e)
            
            
def main():
    while True:
        print(colored(pyfiglet.figlet_format("To-Do List"),"cyan"))
        menu=[
            inquirer.List(
                'choice',
                message='What would you like to do?',
                choices=['Add Task', 
                        'View Tasks',
                        'Delete Task',
                        'Update Status',
                        'Exit'
                        ]
            ),
        ]
        choice = inquirer.prompt(menu)['choice']
        
        if choice=="Add Task":
            name=input(colored("Enter task name","green"))
            desc=input(colored("Enter task description","green"))
            task=ToDoList(name, desc)
            task.add_task()
            print(colored("Task added successfully", "yellow"))
        
        elif choice=="View Tasks":
            tasks=ToDoList.load_tasks()
            for index, task in enumerate(tasks, start=1):
                '''
                task 1
                ----------
                task name:
                task desc:


                ------
                task 2

                '''
                print(colored(f"\n Task {index}:\n{'-'*20}\n{task}\n{'-'*20}", "blue"))
        elif choice=='Delete Task':
            index=int(input(colored("Enter the task index to delete", 'red')))
            ToDoList.delete_task(index)
            print(colored("Task deleted successfully", 'green'))

        elif choice=='Update Status':
            index=int(input(colored("Enter the task index to update", 'red')))
            status=inquirer.prompt([inquirer.List('status', message="Do you want to update status are you sure", choices=['true','false'])])['status']=='true'
            ToDoList.updatestatus(index, status)
            print(colored("Task updated successfully", 'green'))

        elif choice=='Exit':
            print(colored('Exiting the program','red'))
            break

if __name__=='__main__':
    main()