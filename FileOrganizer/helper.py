import os
import shutil
from collections import defaultdict
from config import CATEGORY_MAPPING

def validate_dir(dir_path):
    if not os.path.exists(dir_path):
        print("Directory does not exist")
        return False
    if not os.path.isdir(dir_path):
        print("The provided path is not a directory.")
        return False
    return True

def get_all_files(dir_path):
    all_files = []
    for filename in os.listdir(dir_path):
        full_path = os.path.join(dir_path, filename)
        if os.path.isfile(full_path):
            all_files.append(full_path)
    if all_files:
        return all_files
    print("No files found.")
    return []

def get_file_key(full_path):
    _, extension = os.path.splitext(full_path)
    extension = extension.lower()
    for category, ext in CATEGORY_MAPPING.items():
        if extension in ext:
            return category
    return "OTHERS"

def get_unique_filepath(file_name, destination_dir, placeholder = 1):
    name, extension = os.path.splitext(file_name)
    new_file_name = f"{name}_{placeholder}{extension}"
    new_file_path = os.path.join(destination_dir, new_file_name)
    if os.path.exists(new_file_path):
        return get_unique_filepath(file_name, destination_dir, placeholder+1)
    return new_file_path


def move_files(source, destination):
    try:
        os.makedirs(destination, exist_ok=True)
        file_name = os.path.basename(source)
        final_destination = os.path.join(destination, file_name)

        if os.path.exists(final_destination):
            final_destination = get_unique_filepath(file_name, destination)
        shutil.move(source, final_destination)
        return True
    except PermissionError:
        print(f"Permission denied: Check access for '{source}' or '{destination}'.")
    except FileNotFoundError:
        print(f"File not found: Check if '{source}' exists.")
    except OSError as e:
        print(f"OSError while moving '{source}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return False

def group_files(all_files):
    mapped_files = defaultdict(list)
    for file_path in all_files:
        category = get_file_key(file_path)
        mapped_files[category].append(file_path)
    return mapped_files

def move_group(mapped_files, dir_path):
    summary = defaultdict(int)
    for category, files in mapped_files.items():
        print("="*15 + " "+category +" "+ "="*15)
        category_path = os.path.join(dir_path, category)
        for file_path in files:
            result = move_files(file_path, category_path)
            file_name = os.path.basename(file_path)
            if result:
                print(f"✔️ '{file_name}'.")
                summary[category] += 1
            else:
                print(f"❌ '{file_name}'.")
    return summary

def organize_dir(dir_path):
    all_files = get_all_files(dir_path)
    summary = defaultdict(int)
    if not all_files:
        return summary

    mapped_files = group_files(all_files)
    summary = move_group(mapped_files, dir_path)

    return summary

