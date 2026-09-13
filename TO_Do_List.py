### TO-DO LIST ###

# Make a empty list(tasks)
# while a loop is True:
# a menu that views tasks, add tasks, remove tasks, and quit
# ask user for their choices

tasks = []
while True:
    menu = """
    1. View tasks
    2. Add tasks
    3. Remove tasks
    4. Quit
    """
    print(menu)
    choice = input("Choose what you want to do: ")
    if choice == "1":
        print("Your todo list is empty!")
    else:
        print("\nYour Tasks: ")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    if choice == "2":
        task_add = input("Give name of task: ")
        tasks.append(task_add)
        print("Task added")
    if choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove! ")
        else:
            print("\nWhich task would you like to remove?")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
            user_choice = int(input("Which task number to remove? "))
            real_index = user_choice - 1
            removed = tasks.pop(real_index)
    if choice == "4":
        break
