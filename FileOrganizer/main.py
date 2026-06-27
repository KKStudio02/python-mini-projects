# File organizer
import sys
import helper as h

def main():
    cmd_len = len(sys.argv)
    if cmd_len < 2:
        print("Usage: python main.py organize < directory >")
        return
    
    command = sys.argv[1].lower()
    if command == "organize":
        if cmd_len != 3:
            print("Usage: python main.py organize command")
            return

        path = sys.argv[2]
        if not h.validate_dir(path):
            return

        organize_summary = h.organize_dir(path)
        total = 0
        print("-"*30)
        print("Organization Complete")
        for category, count in organize_summary.items():
            print(f"{category:15} : {count}")
            total += count
        print("-"*30)
        print(f"Total Files Organized : {total}")






if __name__ == '__main__':
    main()