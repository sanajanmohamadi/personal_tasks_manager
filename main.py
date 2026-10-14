name = input("please enter your name: ")
print("welcome", name) 
tasks = []
count = int(input("how meny task do you want to add?"))
for i in range(count):
    task = input("enter a task: ")
    tasks.append(task)
