# Task Tracker CLI

A simple command-line Task Tracker application built in Python. Tasks are stored in a local JSON file and can be created, updated, listed, and deleted through terminal commands.

---

## Features

* Add tasks
* List all tasks
* Update task descriptions
* Update task status
* Delete tasks
* Persistent storage using JSON
* Command-line argument validation
* Automatic task ID generation
* Created and updated timestamps

---

## Project Structure

```text
task-tracker/
│
├── main.py          # CLI entry point
├── helper.py        # Business logic and file operations
├── tasks.json       # Persistent storage
└── README.md
```

---

## Commands

### Add Task

```bash
python main.py add Learn Python
```

### List Tasks

```bash
python main.py list
```

### Update Task Description

```bash
python main.py update 1 Learn FastAPI
```

### Update Task Status

```bash
python main.py mark-done 1
python main.py mark-todo 1
python main.py mark-in-progress 1
```

### Delete Task

```bash
python main.py delete 1
```

---

## Data Model

Each task is stored as:

```json
{
    "id": 1,
    "status": "todo",
    "description": "Learn Python",
    "created_at": "2026-06-21 10:00:00",
    "updated_at": "2026-06-21 10:00:00"
}
```

---

# Key Concepts Learned

## 1. File Handling

### Read File

```python
with open(filename, "r") as file:
```

### Write File

```python
with open(filename, "w") as file:
```

### Check File Existence

```python
os.path.exists(filename)
```

---

## 2. JSON Handling

### Load JSON

```python
tasks = json.load(file)
```

### Save JSON

```python
json.dump(tasks, file, indent=4)
```

---

## 3. CRUD Operations

### Create

Add new tasks.

### Read

List existing tasks.

### Update

Update task description or status.

### Delete

Remove tasks.

---

## 4. Command Line Arguments

Access command line arguments:

```python
sys.argv
```

Example:

```bash
python main.py add Learn Python
```

Produces:

```python
[
    "main.py",
    "add",
    "Learn",
    "Python"
]
```

---

## 5. Multi-Word Arguments

Convert multiple arguments into a single string:

```python
description = " ".join(sys.argv[2:])
```

Result:

```text
Learn Python
```

---

## 6. Error Handling

Convert strings to integers safely:

```python
try:
    task_id = int(sys.argv[2])
except ValueError:
    print("Task ID must be an integer")
```

---

## 7. Separation of Concerns

### main.py

Responsible for:

* Parsing commands
* Input validation
* Routing commands

### helper.py

Responsible for:

* Business logic
* File operations
* Data manipulation

This keeps code easier to maintain.

---

## 8. DRY Principle

Initially file handling logic was repeated.

Refactored into:

```python
load_tasks()
save_tasks()
```

Benefits:

* Less duplication
* Easier maintenance
* Cleaner code

---

## 9. List Comprehensions

Used for deleting tasks.

```python
updated_tasks = [
    task
    for task in tasks
    if task["id"] != delete_id
]
```

---

## 10. Time and Space Complexity

### Find Largest ID

```python
max(task["id"] for task in tasks)
```

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(1)
```

---

### Delete Using List Comprehension

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(n)
```

---

### Update Task

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(1)
```

---

## Design Decisions

### Why JSON?

Simple persistent storage without requiring a database.

### Why Separate main.py and helper.py?

Keeps command parsing separate from business logic.

### Why Store Timestamps?

Tracks task creation and modification history.

### Why Validate Input?

Prevents crashes caused by invalid user input.

---

## Future Improvements

* Filter tasks by status
* Sort tasks by creation date
* Search tasks
* Use SQLite instead of JSON
* Add unit tests
* Package as installable CLI tool
* Add colored terminal output

---

## Interview Notes

If asked about this project:

1. Implemented a complete CRUD application.
2. Used JSON as persistent storage.
3. Applied separation of concerns.
4. Added input validation and error handling.
5. Used list comprehensions and generators.
6. Considered time and space complexity during implementation.
7. Refactored duplicate code using the DRY principle.

```
```
