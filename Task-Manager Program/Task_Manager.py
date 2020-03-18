from datetime import date   #import date.
import os.path              #import path.
user =()                    #define veriable for later use.
choice = ()                 #define veriable for later use.

#Define a function that will welcome you ansk you to enter a username and password. The program will then read from a file and check if
#that username and password is there. If not you will be prompt to try again. If username and password is in the file then you will be
#directed to the next console.
def login():
     
    print('Hello and Welcome. Please enter:')
    with open ('user.txt','r') as uf:
        user=input('Username: ')
        password=input('Password: ')
        name_password = uf.read().strip().split(", ")    
        if user and password in name_password:
            print('Welcome!')
            menu(user)
        else:
            print('Incorrect! Try Again')
            login()

#When login is successful thet user will get a menu ask them if they want to register a new user, add a new task, view all the task,
#view only the tasks assigned to them or exit the program. In order to register a new user, you must be logged in with the admin user 
def menu(user):
            
    choice = input('Please select on of the following options: \n'+'ad - Admin menu\n'+'a - Add task\n'+
        'va - View all task\n'+'vm - View my task\n'+'e - Exit\n'+'\nPlease make you selection: ')
    if choice == "ad" and user == 'admin':
        reg_user(user)
    elif choice == 'a':
        add_task(user)
    elif choice == 'va':
        view_all(user)
    elif choice == 'vm':
        view_mine(user)
    elif choice == 'e': 
        task_ex(user)   
    else:
        print('Unauthorized!! Please contact your Admin')
        menu(user)
 
#If the user is the admin   and they wish to register a new user, the admin will be asked to enter the name, password and re-enter the 
#password. the program will then make sure that the password is correct and write it to the user file.
def reg_user(user): 
    username = []   
    print('Welcome admin!')
    ad_view = input('Please select one of the following options: \n' +
                    'r - Register user\n' + 'a - Add task\n' + 'va - View all task\n'+'vm - View my task\n'+ 'gr - Generate reports\n' +
                    'ds - View all statistics\n' + 'e - Exit\n' + '\nPlease make you selection: ')
    if ad_view == 'r':
        chck_user = input('Please enter the username you would like to create: ')
        with open ('user.txt','a+') as uf:
            for line in uf.readlines():
                username = (line.strip().split(','))
            if chck_user in username:
                print('User already exist')
                reg_user(user)
            elif chck_user not in username:
                print('Please register new user: ')
                new_username = input('Please enter your new user!: ')
                new_password = input('Please enter your password: ')
                re_password = input('Please enter your password again: ')   
                if new_password == re_password:
                    uf.write('\n')
                    uf.write(f"{new_username}, {new_password}")
                    uf.close()
                    reg_user(user)
    
    elif ad_view == 'a':
        add_task(user)

    elif ad_view == 'va':
        view_all(user)
        
    elif ad_view == 'vm':    
        view_mine(user)
        
    elif ad_view == 'gr':
        generate_report(user)
        
    elif ad_view == 'ds':
        display_statistics(user)
        
    elif choice == 'e': 
        task_ex(user)
     
#If the user has selected to add a task to the system then the user will be asked a series of questions nl. 
#For whom is this task for, what is the title, brief discription and when it the task due.Once all that is given the system will
#automatically add the date that this task was created and put it in a not complete state and then write it to the file.
def add_task(user):             
    today = date.today()
    assign_user = input('Please enter the name to whom this task is for: ')
    task_title = input('Please enter the Title of the task: ')
    task_disc = input('Please give the task a brief discription: ')
    issue_date = today.strftime('%d %b %Y')
    year = int(input('Please enter the year that this task is due: '))
    month = int(input('Please enter the month that this task is due: '))
    day = int(input('Please enter the day that this task is due: '))
    user_date = date(year, month, day)
    due_date = user_date.strftime('%d %b %Y')
    complete = 'No'
    with open ('tasks.txt','a+') as tf:
        tf.write('\n')
        tf.write(f"{assign_user}, {task_title}, {task_disc}, {issue_date}, {due_date}, {complete}")
    menu(user) 
        
#If the user has selected to view all the tasks that are stored it the folder then the program will open the file and read all the data
#and print it out in a nicely layedd out format.
def view_all(user):      
    all_task = []      
    with open ('tasks.txt','r') as tf:
        for line in tf.readlines():
            all_task = (line.strip().split(','))
            if user == all_task[0]:
                print('User:\t\t\t '+ all_task[0])
                print('Task Name:\t\t' + all_task[1])
                print('Task Description:\t' + all_task[2])
                print('Issue Date:\t\t' + all_task[3])
                print('Due Date:\t\t' + all_task[4])
                print('Completed:\t\t' + all_task[5])
                print('\n')
        menu(user) 
    
# Create a dictionary of the users for future use 
def task_dict():
    with open('tasks.txt', 'r') as tf:
            task_dictionary = {}
            for i,line in enumerate(tf):
                values = line.strip().split(', ')
                task_dictionary[i + 1] = {
                                            'username' : values[0],
                                            'task_desc' : values[1],
                                            'task_note' : values[2],
                                            'date_created': values[3],
                                            'date_due' : values[4],
                                            'task_complete' : values[5]
                                            }
    return task_dictionary
                
# Create a dictionary of the users for future use
def user_dict():
    with open('user.txt', 'r') as uf:
            user_dictionary = {}
            for i,line in enumerate(uf):
                values = line.strip().split(', ')
                user_dictionary[i + 1] = {
                                            'username' : values[0],
                                            'password' : values[1],
                                            }
    
    return user_dictionary        

#If the user has selected to view my tasks that are stored it the folder then the program will open the file and read all the data
#and search for all tasks that belong that the user and print it out in a nicely layedd out format.
def view_mine(user):
    task_dictionary = task_dict()
    user_tasks = []
    
    for count in task_dictionary:
        task = task_dictionary[count]
        if user == task['username']:
                print(f"{count}) Task: \t\t{task['task_desc']}")
                print(f"Assigned to: \t\t{task['username']}")
                print(f"Task description: \t{task['task_note']}")
                print(f"Date assigned: \t\t{task['date_created']}")
                print(f"Due date: \t\t{task['date_due']}")
                print(f"Task Complete?: \t{task['task_complete']}")
                print('')
                user_tasks.append(count)

    if not task['username']:
        print(f"No tasks found for user {user}")
        menu(user)            
    
    user_choice = int(input("\n Choose a task number to edit or type -1 to return to the menu: "))
    if user_choice != -1 and user_choice in user_tasks:
        edit_user_task(user_choice,task_dictionary)
    elif user_choice == -1:
        menu(user)     

#This function will get the user to change certain info of a task. They will be able to change the assigned user to someone else and change the due date.    
def edit_user_task(x,dictionary): 
    print('Please choose from the following: ')
    print('1) Mark the task as complete')
    print('2) Edit the task')
    print('3) Back to main menu\n')
    user_choice = input(f'Edit task ({x}) or mark as complete?: ')        

    # Checking that the task isn't marked complete already
    # If it is, display the error, if not, mark as complete
    if user_choice == '1':
        if dictionary[x]['task_complete'] == 'Yes':
                print('Task already complete, cannot set to complete again.')
         
        else:   #Change 'task_complete to 'Yes'
            dictionary[x]['task_complete'] = 'Yes'
            print(f"Task \"{dictionary[x]['task_desc']}\" marked as complete.")
            menu(user)
    #If user selects opton 2, then the user will be able to change the assigned user to someone else and change the due date.  
    elif user_choice == '2':
            # Same error check as above
            if dictionary[x]['task_complete'] == 'Yes':
                print('Task already complete, cannot edit')
                menu(user)
            #Choose which one you would like to change.    
            print('Please choose from the following: \n')
            print(f"1) Change the user the task \"{dictionary[x]['task_desc']}\" is assigned to")
            print(f"2) Change the due date for \"{dictionary[x]['task_desc']}\"")
            print('3) Back to main menu\n')
            user_choice_change = input(f'Your choice?: ')
            #Change the name of the user for the specific task that must be edited.
            if user_choice_change == '1':
                new_username = input(f"Please enter the new user to which the task \"{dictionary[x]['task_desc']}\" will be assigned: ")    
                dictionary[x]['username'] = new_username
            #Change the due date of the task.
            elif user_choice_change == '2':
                print(f"Please enter the new due date for task \"{dictionary[x]['task_desc']}\": ")
                year = int(input('Please enter the year that this task is due: '))
                month = int(input('Please enter the month that this task is due: '))
                day = int(input('Please enter the day that this task is due: '))
                new_user_date = date(year, month, day)
                new_due_date = new_user_date.strftime('%d %b %Y')
                dictionary[x]['date_due'] = new_due_date

            elif user_choice == '3':
                menu(user)

    elif user_choice == '3':
        menu(user)
    #open the file and rewirte the tast with en update info.   
    with open('tasks.txt', 'w', encoding='utf-8') as tf:
        for count in dictionary:
            tf.write(f"{dictionary[count]['username']}, {dictionary[count]['task_desc']}, {dictionary[count]['task_note']}, {dictionary[count]['date_created']}, {dictionary[count]['date_due']}, {dictionary[count]['task_complete']}\n")
    menu(user)

#This function will generate a report based on what the admin would like to see. See below as every part of the report will be explained.   
#recall the function that was created earlier that has all the info from the files in a dictionary.
def generate_report(user):
    from_task = task_dict()
      
    #Total number of task.
    total_tasks = len(from_task)    

    #Get the count of the completed tasks
    completed = 0
    for task in from_task.values():
        if task['task_complete'] == 'Yes':
            completed += 1  

    #Calculate total incomplete tasks
    incomplete_tasks = total_tasks - completed

    #Calculate percentage overdue
    per_incomplete = int((incomplete_tasks/ total_tasks) * 100)

    #We call certain dictionary value to get the following: total overdue tasks
    overdue = 0
    from datetime import datetime
    today = datetime.today()
    today_date = today.strftime('%d %b %Y')

    for task in from_task.values():
        due_date = task['date_due']
        if due_date < today_date:
            overdue +=1

    #calculate percentage overdue
    per_overdue = int((overdue/ total_tasks) * 100)

    #Create a veriable that hold these values.
    t_report = (f" Total task: {total_tasks}\n Total tasks completed: {completed}\n Total tasks incomplete: {incomplete_tasks}\n Total amount of tasks overdue: {overdue}\n Total percentage of tasks incomplete: {per_incomplete}\n Total percentage of tasks overdue: {per_overdue}\n" )
    #Create a folder and write the data in it.
    with open ("task_overview.txt", "w+") as to:
        to.write(t_report)
    user_report(user)

#This function will generate a report based on what the admin would like to see. See below as every part of the report will be explained.   
#recall the function that was created earlier that has all the info from the files in a dictionary.
def user_report(user):
    from_task = task_dict()
    from_user = user_dict()
    user_task_count = 0
    complete_count = 0
    overdue_count = 0
    total_tasks = len(from_task)
    from datetime import datetime
    today = datetime.today()
    today_date = today.strftime('%d %b %Y')


    #We call certain dictionary value to get the following: total overdue tasks, total task for specific user and total of completed tasks.
    for task in from_task.values():
        due_date = task['date_due']
        if due_date < today_date:
            overdue_count += 1
            if task['username'] == user:
                user_task_count += 1
                if task['task_complete'].lower() == "yes":
                    complete_count += 1
                
    #Calculate total incomplete tasks.
    incomplete_tasks = total_tasks - complete_count


    #Total number of users.
    total_users = len(from_user)

    #Total number of tasks assigned to specific user.
    user_complete = user_task_count
    #Calaculate percentages of the following: assigned to user, completed, incomplete and overdue.
    user_per_assigned = int((user_task_count/ total_tasks) * 100)

    user_per_completed = int((complete_count/ total_tasks) * 100)

    user_per_incomplete = int((incomplete_tasks/ total_tasks) * 100)

    user_per_overdue = int((overdue_count/ total_tasks) * 100)


    #Create a veriable that hold these values.
    u_report = (f" Total users: {total_users}\n Total task: {total_tasks}\n Total number of tasks assigned to you: {user_complete}\n Total percentage of tasks assigned to you: {user_per_assigned}\n Total percentage of your tasks completed: {user_per_completed}\n Total percentage of your tasks incompleted: {user_per_incomplete}\n Total percentage of your tasks overdue: {user_per_overdue} " )
    #Create a folder and write the data in it.
    with open ("user_overview.txt", "w+") as uo:
        uo.write(u_report)
    reg_user(user)

#The admin can now print out the generated report that was created above. This will print out everything in an easy to read format.
def display_statistics(user):
    #Check if files are already in the folder, if not the auto generate and then read data.
    if not os.path.exists("user_overview.txt") and os.path.exists("task_overview.txt"):
        generate_report(user)       

    with open ("task_overview.txt", "r") as to:
        task_info = to.read()
        print("### Task Overview ###\n")
        print(task_info)
    
    with open("user_overview.txt", "r") as uo:
        user_info = uo.read()
        print("### User Overview ###\n")
        print(user_info)
        reg_user(user)

#If the chooses to exit the program, then the user is asked if they a sure. If user enters 'y' then the program terminates.
def task_ex(user): 
    ex = input('Are you sure you want to exit the program?(type y) ')  
    if ex == 'y':   
        print('GOODBYE')
        exit(user)
    else:
        menu(user)       
login()
