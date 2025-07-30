tasks = []

def main():

    while True:
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")


        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added successfully")


        elif choice == '2':
            if len(tasks) == 0:
                print("There are no tasks yet")
            else:
                print("\nTasks: ")
                for t in tasks:
                    print("->", t)


        elif choice == '3':
            task = input("Enter the task you want to remove: ")
            tasks.remove(task)
            print("Task successfully removed")


        elif choice == '4':
            break


        else:
            print("Invalid option!")

main() #run everything inside the main function.



