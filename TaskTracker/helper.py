import json
from datetime import datetime
import os

FILENAME = "tasks.json"
#basic functions
def load_tasks():
    tasks = []
    if not os.path.exists(FILENAME):
        save_tasks(tasks)
        return tasks
    with open(FILENAME, "r") as file:
        tasks = json.load(file)
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def get_largest_id(tasks):
    largest_id = max(task['id'] for task in tasks)
    return largest_id


def add_task(description):
    updated_id = 1
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tasks = load_tasks()
    if tasks:
        updated_id = get_largest_id(tasks) + 1
    new_task = {'id': updated_id,
                'status': 'todo',
                'description': description,
                'updated_at': date_time,
                'created_at': date_time
                }
    tasks.append(new_task)
    save_tasks(tasks)

    return f"task '{description}' added with id [{updated_id}]"


def show_tasks():
    tasks = load_tasks()
    if tasks:
        print(f"{'ID':<6} | {'DESCRIPTION':<30} | {'STATUS'}")
        print("-" * 55)
        for task in tasks:
            print(f"{task['id']:<6} | {task['description']:<30} | {task['status']}")
    else :
        print("No Tasks Found.")

def delete_task(del_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['id'] != del_id]
    if len(updated_tasks) < len(tasks):
        save_tasks(updated_tasks)
        return f"task [{del_id}] was deleted successfully"
    return f"No Tasks Found with id [{del_id}]."


def update_task(update_id, update, field_to_update):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == update_id:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task[field_to_update] = update
            task['updated_at'] = current_time
            save_tasks(tasks)
            return f"task [{update_id}] | {task['description']:<30} | {task['status']} was updated successfully "
    return f"No Tasks found with id {update_id}."
