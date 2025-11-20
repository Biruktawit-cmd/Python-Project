def display_menu():
    """Display the menu options"""
    print("\n=== TO-DO LIST MANAGER ===")
    print("Commands:")
    print("  add <task> - <priority>  : Add a new task (priority: high, medium, low)")
    print("  view                     : View all tasks")
    print("  complete <number>        : Mark a task as complete")
    print("  delete <number>          : Delete a task")
    print("  exit                     : Exit and show summary")
    print("-" * 50)

def display_tasks(tasks):
    """Display all tasks with their status"""
    if not tasks:
        print("\nNo tasks in your list!")
        return
    
    print("\n=== YOUR TASKS ===")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['completed'] else "○"
        priority = task['priority'].upper()
        task_name = task['name']
        
        # Add strikethrough effect for completed tasks
        if task['completed']:
            print(f"{i}. [{status}] {task_name} - [{priority}] (COMPLETED)")
        else:
            print(f"{i}. [{status}] {task_name} - [{priority}]")

def add_task(tasks, task_input):
    """Add a new task with priority"""
    try:
        # Parse input: "task name - priority"
        if ' - ' not in task_input:
            print("Error: Please use format 'task name - priority'")
            return
        
        parts = task_input.split(' - ')
        task_name = parts[0].strip()
        priority = parts[1].strip().lower()
        
        if not task_name:
            print("Error: Task name cannot be empty")
            return
        
        if priority not in ['high', 'medium', 'low']:
            print("Error: Priority must be 'high', 'medium', or 'low'")
            return
        
        tasks.append({
            'name': task_name,
            'priority': priority,
            'completed': False
        })
        print(f"✓ Task added: {task_name} [{priority.upper()}]")
    
    except Exception as e:
        print(f"Error adding task: {e}")

def complete_task(tasks, task_number):
    """Mark a task as complete"""
    try:
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            if tasks[index]['completed']:
                print("This task is already completed!")
            else:
                tasks[index]['completed'] = True
                print(f"✓ Task completed: {tasks[index]['name']}")
        else:
            print("Error: Invalid task number")
    except ValueError:
        print("Error: Please enter a valid number")

def delete_task(tasks, task_number):
    """Delete a task by number"""
    try:
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"✓ Task deleted: {deleted_task['name']}")
        else:
            print("Error: Invalid task number")
    except ValueError:
        print("Error: Please enter a valid number")

def show_summary(tasks):
    """Display summary of completed vs pending tasks"""
    total = len(tasks)
    completed = sum(1 for task in tasks if task['completed'])
    pending = total - completed
    
    print("\n" + "=" * 50)
    print("=== SUMMARY ===")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    
    if completed == total and total > 0:
        print("\n🎉 Congratulations! All tasks completed!")
    elif pending > 0:
        print(f"\n📋 You still have {pending} task(s) to complete.")
    
    print("=" * 50)

def main():
    """Main function to run the to-do list manager"""
    tasks = []
    
    print("Welcome to the To-Do List Manager!")
    display_menu()
    
    while True:
        user_input = input("\nEnter command: ").strip()
        
        if not user_input:
            continue
        
        # Parse command
        parts = user_input.split(maxsplit=1)
        command = parts[0].lower()
        
        if command == "exit":
            show_summary(tasks)
            print("\nThank you for using To-Do List Manager. Goodbye!")
            break
        
        elif command == "add":
            if len(parts) > 1:
                add_task(tasks, parts[1])
            else:
                print("Error: Please specify a task. Format: add <task> - <priority>")
        
        elif command == "view":
            display_tasks(tasks)
        
        elif command == "complete":
            if len(parts) > 1:
                complete_task(tasks, parts[1])
            else:
                print("Error: Please specify a task number")
        
        elif command == "delete":
            if len(parts) > 1:
                delete_task(tasks, parts[1])
            else:
                print("Error: Please specify a task number")
        
        elif command == "help":
            display_menu()
        
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
