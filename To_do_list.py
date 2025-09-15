# Step 1: Make an empty list to store tasks
tasks = []

# Step 2: Show menu until user quits
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Quit")

    choice = input("Enter choice: ")

    # Step 3: Add task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"title": task, "done": False})
        print("Task added!")

    # Step 4: View tasks
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "✓" if t["done"] else " "
                print(f"{i}. [{status}] {t['title']}")

    # Step 5: Mark task done
    elif choice == "3":
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked done!")
        else:
            print("Invalid task number.")

    # Step 6: Remove task
    elif choice == "4":
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task removed!")
        else:
            print("Invalid task number.")

    # Step 7: Quit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
