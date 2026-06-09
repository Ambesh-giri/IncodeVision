# Create a simple To-Do List program that works in the Python console.

# Your program should show a small menu where the user can choose to add a task, 
# view all tasks, mark a task as completed, or delete a task.

# Store all tasks inside a list and update the list based on the user's choice.

# This task helps you understand how to use lists, loops, and user input in Python.

def addTask():
    atask=input("Enter Task : ")
    Task.append(atask)
    print()
    print()

def viewTask():
    for task in range(len(Task)):
        print(task+1,'. ',Task[task])
    print()
    print()

def markTask():
    i=0
    completed=False
    for task in Task:
        if task in Mark:
            print('[✓]',task)
        else:
            print('[]',task)
        
    chose=input("Enter your task name for completion : ")
    if chose in Task:
        completed=True
        Mark.append(chose)
        print("complete!!!")
    print()
    print()

def deleteTask():
    task=input("Enter Task Name : ")
    Task.remove(task)
    print()
    print()


condition=True
Task=[]
Mark=[]
while condition:
    print('''    1. Add Task
    2. View Task
    3. Mark Task
    4. Delete Task
    5. Exit''')
    select=int(input("Enter serial number According to your task : "))
    match select:
        case 1: addTask()
        case 2: viewTask()
        case 3: markTask()
        case 4: deleteTask()
        case 5: 
            condition=False
            print('!!! Thank you !!!')

