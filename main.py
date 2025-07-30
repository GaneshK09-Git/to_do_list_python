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
            if not tasks:
                print("There are no tasks yet")
            else:
                print("\nTasks: ")
                print("==========================================")
                for index, task in enumerate(tasks, start=1): # enumerate() returns an iterator that yields pairs of (index, value) for each item in an iterable.
                    print(f"{index}. {task}")
                print("==========================================")


        elif choice == '3':
            task = int(input("Enter the task number you want to remove: "))
            if task in tasks:
                tasks.remove(task)
                print("Task successfully removed")
            else:
                print("No such task!")


        elif choice == '3':
            if not tasks:
                print("No tasks to remove")
            else:
                # Step 1: Show tasks with numbers
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

                while True:

                # Step 2: Ask for task number to remove
                    try:
                        remove = int(input("Enter the task number you want to remove: "))
                        index = remove - 1
                        
                        # Step 3: Check if number is valid
                        if 0 <= index < len(tasks):
                            removed_task = tasks.pop(index)
                            print(f"Removed: {removed_task}")
                            break                               # exit the loop after successful removal

                        else:
                            print("Invalid task number, try again!")

                    except ValueError:
                        print("Enter a valid number!")


        elif choice == '4':
            break          #Exit


        else:
            print("Invalid option!")

main() #run everything inside the main function.



