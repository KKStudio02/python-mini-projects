import sys
import helper as h

allowed_statuses = {
    "todo",
    "done",
    "in-progress"
}

def main():
    cmd_length = len(sys.argv)
    if cmd_length < 2:
        print("please provide a command")
        exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if cmd_length < 3:
            print("Usage: python main.py add <description>")
            return
        description = " ".join(sys.argv[2: ])
        print(h.add_task(description))
    elif command == "list":
        h.show_tasks()
    elif command == "delete":
        if cmd_length != 3:
            print("Usage: python main.py delete <task_id>")
            return
        try:
            del_id = int(sys.argv[2])
        except ValueError:
            print("Task id must be an integer")
            return
        print(h.delete_task(del_id))
    elif command == "update":
        if cmd_length < 4:
            print("Usage: python main.py update <task_id> <description>")
            return
        try:
            update_id = int(sys.argv[2])
        except ValueError:
            print("Task id must be an integer")
            return
        description = " ".join(sys.argv[3: ])
        print(h.update_task(update_id, description, 'description'))
    elif command.startswith("mark-"):
        if cmd_length != 3:
            print("Usage: python main.py mark-done <task_id>")
            return
        try:
            update_id = int(sys.argv[2])
        except ValueError:
            print("Task id must be an integer")
            return
        status = command.replace("mark-", "")
        if status not in allowed_statuses:
            print("Task status must be one of: " + ", ".join(allowed_statuses))
            return
        print(h.update_task(update_id, status, 'status'))
    else:
        print("please try again wrong command")


if __name__ == '__main__':
    main()

