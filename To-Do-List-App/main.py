tasks = []

def add_Task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("new task added..")

def remove_Task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed")
    else:
        print("There is no tasks.. ")

def show():
    i = 0
    print("............Your list..............")
    for task in tasks:
        print(i,task)
        i = i + 1


print("..........Welcome to your To-Do-List..........")
while True:
    print("Select option......")
    print("1. Add New Task")
    print("2. Remove task")
    print("3. Show task list")
    print("4. Exit")
    case = input("Enter selection: ")

    if case == '1':
        add_Task()
    elif case == '2':
        remove_Task()
    elif case == '3':
        show()
    elif case == '4':
        exit()
    else:
        print("Invalid selection")
