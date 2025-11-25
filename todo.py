
Tasks = []

def box_title(title):
    print("\n" + "="* 40)
    print(title.center(40))
    print("="* 40)


def view_Tasks():
    box_title("Your Tasks:")

    if not Tasks:
        print("No tasks added yet!")
    else:
        
        for i, task in enumerate(Tasks, 1):
            print(f"{i}: {task}")


def Add_Tasks():
    box_title("Add Your Task")
    item = input("Enter The New Task: ")
    Tasks.append(item)
    print("Task Added!")


def Delete_Task():
    box_title("Delete Task")
    view_Tasks()
    if Tasks:
        num = int(input("Enter The Task Number to Delete: "))
        if 1 <= num <= len(Tasks):
            removed = Tasks.pop(num - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid Number!")

while True:
    box_title("To-Do Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        view_Tasks()
    elif choice == 2:
        Add_Tasks()
    elif choice == 3:
        Delete_Task()
    elif choice == 4:
        print("------Good Bye!------")
        break
    else:
        print("Invalid Choice!")
