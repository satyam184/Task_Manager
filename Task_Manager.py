#using if_else

# def task():
#     tasks=[]
#     print("___TO-DO___")

#     total_task = int(input("Enter how many task you want to add ="))
#     for i in range(1,total_task+1):
#         task_name=input(f"Enter task {i} =")
#         tasks.append(task_name)

#     print(f"Today's tasks are\n{tasks}")    

#     while True:
#         op=int(input("Enter:\n 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Exit\n"))
#         if op==1:
#             add=input("Enter task you want add = ")
#             task.append(add)
#             print(f"Task {add} has been successfully added..")

#         elif op==2:
#             Update_val=input("Enter the task name you want to upadte = ")
#             if Update_val in tasks:
#                 up=input("Enter new task =") 
#                 ind=tasks.index(Update_val) 
#                 tasks[ind]=up
#                 print(f"Updated task {up}")  

#         elif op==3:
#             del_val=input("Enter the task name you want to delete = ")  
#             if del_val in tasks:
#                 ind=tasks.index(del_val)
#                 del tasks[ind]
#                 print(f"Task {del_val} has been deleted... ")

#         elif op==4:
#             print(f"Total tasks {tasks}")

#         else:
#             print("Invalid Input")    


#using switch case
def task():
    tasks = []
    print("___TO-DO LIST___")

    total_task = int(input("Please specify the number of tasks you wish to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter the name of task {i}: ")
        tasks.append(task_name)

    print(f"\nToday's tasks are: {tasks}\n")

    while True:
        op = int(input("Choose an option:\n 1 - Add Task\n 2 - Update Task\n 3 - Delete Task\n 4 - View Tasks\n 5 - Exit\n"))

        match op:
            case 1:
                add = input("Enter the name of the task you wish to add: ")
                tasks.append(add)
                print(f"Task '{add}' has been successfully added.\n")

            case 2:
                update_val = input("Enter the name of the task you wish to update: ")
                if update_val in tasks:
                    up = input("Enter the updated task name: ")
                    ind = tasks.index(update_val)
                    tasks[ind] = up
                    print(f"Task '{update_val}' has been updated to '{up}'.\n")
                else:
                    print(f"Task '{update_val}' was not found. Please verify and try again.\n")

            case 3:
                del_val = input("Enter the name of the task you wish to delete: ")
                if del_val in tasks:
                    tasks.remove(del_val)
                    print(f"Task '{del_val}' has been successfully deleted.\n")
                else:
                    print(f"Task '{del_val}' was not found. Please verify and try again.\n")

            case 4:
                print("Current list of tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                print("") 

            case 5:
                print("Thank you for using the Task Manager. Have a productive day!")
                break

            case _:
                print("Invalid selection. Please enter a number from 1 to 5 corresponding to your desired action.\n")

task()


