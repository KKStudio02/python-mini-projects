# 📂 File Organizer CLI

A command-line application built with Python that organizes files into categorized folders based on their file extensions.

This project was built to strengthen my understanding of Python file handling, modular programming, command-line interfaces, and software design principles.

---

# Features

* Organize files using a CLI command
* Automatically create category folders
* Categorize files based on extensions
* Rename duplicate files automatically
* Handle invalid directories gracefully
* Display organization summary
* Continue execution even if individual files fail to move
* Uses only Python Standard Library (No external packages)

---

# Folder Structure

```
file-organizer/
│
├── main.py
├── helper.py
├── config.py
├── README.md
└── .gitignore
```

---

# Project Architecture

```
User

   │

main.py
(Command Validation)

   │

organize_dir()

   │

get_all_files()

   │

group_files()

   │

move_group()

   │

move_files()

   │

rename_file()
```

---

# Technologies Used

* Python 3
* os
* shutil
* sys
* collections.defaultdict

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd file-organizer
```

---

# Usage

```bash
python main.py organize "<directory-path>"
```

Example

```bash
python main.py organize "C:\Users\Krunal\Downloads"
```

---

# Supported Categories

| Folder        | Extensions                                              |
| ------------- | ------------------------------------------------------- |
| IMAGES        | jpg, jpeg, png, gif, bmp, webp, svg, ico, heic          |
| DOCUMENTS     | pdf, doc, docx, txt, rtf, odt                           |
| SPREADSHEETS  | xlsx, xls, csv                                          |
| PRESENTATIONS | ppt, pptx                                               |
| MUSIC         | mp3, wav, aac, flac, ogg, m4a                           |
| VIDEOS        | mp4, mkv, avi, mov, wmv, flv, webm                      |
| ARCHIVES      | zip, rar, 7z, tar, gz                                   |
| EXECUTABLES   | exe, msi, bat, cmd                                      |
| CODE          | py, java, js, ts, html, css, cpp, c, cs, json, xml, sql |
| OTHERS        | Any unsupported extension                               |

---

# Design Decisions

## Why config.py?

Instead of hardcoding categories inside helper.py, they were moved into config.py.

Benefits:

* Better separation of concerns
* Easier to maintain
* Easy to extend with new categories
* Business logic remains independent of configuration

---

## Why defaultdict?

Used for grouping files by category.

Instead of

```python
if key not in dictionary:
```

defaultdict automatically creates an empty list.

---

## Why Sets?

File extensions are stored inside sets instead of lists.

Benefits:

* Faster lookup
* Cleaner code
* Constant-time membership checking

---

## Duplicate File Handling

If a file already exists inside the destination folder

```
resume.pdf
```

the application automatically renames it

```
resume_1.pdf
resume_2.pdf
resume_3.pdf
```

instead of overwriting or skipping.

---

# Error Handling

Handled scenarios include

* Invalid directory
* Path is not a directory
* Empty directory
* Permission denied
* Missing source file
* Unsupported extensions
* Duplicate filenames

---

# Concepts Practiced

## Python Fundamentals

* Functions
* Loops
* Conditionals
* Dictionaries
* Sets
* Lists
* Recursion

---

## File Handling

* os.listdir()
* os.path.exists()
* os.path.isdir()
* os.path.isfile()
* os.makedirs()
* os.path.join()
* os.path.basename()
* os.path.splitext()

---

## File Operations

* shutil.move()

---

## Command Line

* sys.argv

---

## Data Structures

* defaultdict
* Dictionary
* Set
* List

---

## Error Handling

* try / except
* PermissionError
* FileNotFoundError
* OSError

---

# Interview Revision Notes

## os.listdir()

Returns all items inside a directory.

---

## os.path.join()

Creates platform-independent file paths.

---

## os.path.splitext()

Splits a filename into

```
filename
extension
```

Used to identify file categories.

---

## os.makedirs()

Creates directories recursively.

Using

```python
exist_ok=True
```

prevents an exception if the directory already exists.

---

## shutil.move()

Moves files from one location to another.

---

## defaultdict(list)

Automatically initializes missing dictionary keys with empty lists.

Useful for grouping data.

---

## Recursion

Implemented in `rename_file()` to generate unique filenames until an available name is found.

---

# Challenges Faced

* Designing modular functions instead of one large function
* Separating configuration from business logic
* Handling duplicate filenames
* Designing reusable helper functions
* Organizing responsibilities across modules

---

# Future Improvements

* Preview mode (`preview`)
* Undo last organization
* Recursive directory organization
* Ignore configurable file patterns
* Custom categories through configuration
* Logging support
* Unit tests
* Dry-run mode

---

# Learning Outcomes

This project helped me practice:

* Modular programming
* Separation of concerns
* Working with the operating system
* Python file handling
* CLI application development
* Error handling
* Code organization
* Designing reusable helper functions

---

# Author

**Krunal Kharat**

This project is part of my **Python Mini Projects** learning repository, where I build progressively more complex applications while strengthening my Python fundamentals and software engineering skills.
