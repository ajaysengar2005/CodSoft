def append():
    t = int(input("How many task you want to add : "))
    for i in range(t):
        task = input(f"Enter Task {i+1} : ")
        Tasks.append({"task":task,"done":False})
        print(f"Task '{task}' Added!")

def show_Task():
    length = len(Tasks)
    if length > 0 :
        print("Tasks :")
        for i,task in enumerate(Tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i+1}. {task['task']} - {status}")
    else:
        print("No Tasks are in List")

def mark_Done():
    length = len(Tasks)
    if length > 0:
        r = int(input("Enter Task Number : "))
        if r >= 0 and r < length:
            Tasks[r]["done"] = True
            print("Task Marked!")
        else:
            print("Invalid Number")
    else:
        print("There is No Task in List")


def delete_Task():
    length = len(Tasks)
    if length > 0 :
        d = int(input("Enter Task Number : "))
        if d >= 0 and d < len(Tasks):
            Tasks.pop(d)
            print(f"Task {d}. Removed!")
        else:
            print("Invalid Task Number\nPlease Try Again ")
    else:
        print("No Task to Delete")





if __name__ == "__main__":
    Tasks = []
    while True:
        print("\n")
        print("Welcome to To Do List")
        print("*********************")
        print("1.Add Task ")
        print("2.Show Task ")
        print("3.Mark Task as Done ")
        print("4.Delete Task ")
        print("5.Exit ")
        print("*********************")
        print("\n")


        choice = input("Enter Choice : ")

        if choice == '1':
            append()
            

        elif choice == '2':
            show_Task()
           

        elif choice == '3':
            mark_Done()
            

        elif choice == '4':
           delete_Task()

        elif choice == '5':
            break
    
        else:
            print("Invalid Choice")



