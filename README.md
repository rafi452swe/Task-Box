# 📝 Python To-Do List App (CLI Version)

A simple and clean **Command-Line To-Do List Application** written in Python.  
It allows users to **add, view, and delete tasks** with a stylish boxed UI for better readability.

---

## 🚀 Features

✔ Clean and minimal menu UI  
✔ Box-styled section headers  
✔ Add new tasks  
✔ View all tasks  
✔ Delete tasks by number  
✔ Error handling for invalid inputs  
✔ Beginner-friendly code structure  
✔ Fully runs in terminal

---

## 📂 Project Structure
to_do_list/
└── main.py


`main.py` contains all features including the menu, task operations, and box design.

---

## 🖥 Preview (Terminal Output)

========================================
To-Do Menu

View Tasks

Add Task

Delete Task

Exit
========================================


---

## 📌 How It Works

### 🔹 1. View Tasks
Shows all tasks with numbering.

### 🔹 2. Add Task
User types new task → added to list.

### 🔹 3. Delete Task
User enters a task number → task removed.

### 🔹 4. Exit
Cleanly exits the program.

---

## 🧩 Code Overview

### ✔ Box Title Function
Creates beautiful headers for each section.

```python
def box_title(title):
    print("\n" + "=" * 40)
    print(title.center(40))
    print("=" * 40)

▶️ How to Run

Install Python (if not installed)

Download or clone this repository

Open terminal in the project folder

Run: python main.py

👨‍💻 Author

Md.Rafiul Islam Akanda
2nd Year Software Engineering Student
GitHub: https://github.com/rafi452swe

📜 License

This project is free to use for learning and educational purposes.

