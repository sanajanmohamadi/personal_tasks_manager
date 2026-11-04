import os
from dotenv import load_dotenv
from tasks import show_tasks, save_tasks, load_tasks


name = input("enter your name: ")
print("Welcome", name)

load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? yes/no: ")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin, hello")
    else:
        print("wrong password")



tasks = load_tasks()
count = int(input("how many tasks do you want to add?: "))

for i in range(count):
    task_name = input("enter a task: ")
    priority = input("enter priority(low/medium/high): ").lower()
    task = {
        "name" : task_name,
        "priority" : priority
    }
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)