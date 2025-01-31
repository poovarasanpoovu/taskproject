import time
from datetime import datetime as d
import os,time
import mysql.connector

import mysql.connector

db_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb"
)
cur = db_connect.cursor()
def table_tasks():
 insert_task = '''
    CREATE TABLE IF NOT EXISTS taskinsert(
      tasks_name VARCHAR(20)

    )'''
 cur.execute(insert_task)
#table_tasks()


date = d.now()
start=time.time()

BLUE = "\033[0;34m"
RED = '\033[91m'
PURPLE = "\033[0;35m"
NEGATIVE = "\033[7m"
RESET = '\033[0m'

BOLD = "\033[1m"
ITALIC = "\033[3m"

smile_emoji='\U0001F60A'
verify_emoji ='\U0001F914'
success_emoji='\U0001F60E'
thanks_emoji='\U0001F64F'
hand_emoji='\U0001F44D'
heart_emoji='\U00002764'

print(BOLD,ITALIC,f"Task Program{smile_emoji}".center(30,"*"))
print("\rDate & time : ",date.strftime("%d/%m/%Y; %H:%M:%S %p"))

user = ''
passwords = ''

information =[]
remove_list = []
def add_task():
   try:
       print(BOLD,ITALIC)
       number = int(input("How many task's will added : "))

   except Exception:
       print(NEGATIVE,"Only Numeric!!!",RESET,verify_emoji)
       add_task()
   else:
       for i in range(1, number + 1):
           task = input(f"Enter the task {i}: ")
           information.append(task)
           insert_task_query="INSERT INTO taskinsert VALUES (%s)"
           cur.execute(insert_task_query,(task,))
           db_connect.commit()
       print("Task's added Successfully!!",smile_emoji)
       cur.close()
       db_connect.close()
       task_start=time.time()
       time.sleep(2)

def view_task():
    print(BOLD,ITALIC)
    if not information:
        print(NEGATIVE,"No Task's Found!!!",RESET,hand_emoji)
        time.sleep(2)
    else:
       count=1
       for j in information:
          print(f"{count}: {j}".title())
          count+=1
       time.sleep(2)
def update_task():
    print(BOLD,ITALIC)
    if not information:
        print(NEGATIVE,"No Task's Found!!!",RESET,hand_emoji)
        time.sleep(2)
        #main(user)
    else:
        try:
          num= int(input("How many task's updated : "))
        except Exception:
            print("Only Numeric!!!",verify_emoji)
            time.sleep(2)
            update_task()
        else:
          if num<=(len(information)):
            for i in range(0,num):
              choose = input("Please Enter task : ")
              if choose in information:
                  remove = information.remove(choose)
                  remove_list.append(choose)
                  print("\n Updated Successfully!!!",smile_emoji)
                  time.sleep(2)
              else:
                  print(NEGATIVE,BOLD,ITALIC,"Task Not Matched!!!",RESET,hand_emoji)
                  print("Pending Task Is : ",end = " ")
                  view_task()
                  time.sleep(2)


          else:
              print(f"Please enter number is : less than ''{len(information)}'' or equal to ''{len(information)}'' ")
              time.sleep(2)
              update_task()

def complete_task():
    print(BOLD,ITALIC)
    if not information:
        if remove_list:
            for i in remove_list:
                print(f"completed task is : {i} completed")
            time.sleep(2)
        print(NEGATIVE,"No Task's Found!!!",RESET,hand_emoji)
        time.sleep(2)
        #main(user)

    else:
        print(NEGATIVE,"Task's Pending!!!",RESET)
        view_task()
        for i in remove_list:
          print(f"completed task is : ''{i}''".title())

def main(user):
    count=0
    print(f"Hi! welcome '{RED+user+heart_emoji+RESET}'")
    time.sleep(2)
    while True:
     print(BOLD,ITALIC)
     print(BLUE,"Menu's".center(30,"*"))
     print("1.Add Task")
     print("2.View Task")
     print("3.Update Task ")
     print("4.Complete Task ")
     print("5.Sign out",RESET)

     try:
        count += 1
        print(PURPLE)
        task = int(input("Enter the option(1/2/3/4/5): "))
        print(RESET)

     except Exception:
         print(NEGATIVE,"Only Numeric!!!",RESET,verify_emoji)
     else:
        if task == 1:
          add_task()
        elif task == 2:
          view_task()
        elif task == 3:
          update_task()
        elif task == 4:
          complete_task()
        elif task==5:
          print(BOLD,ITALIC)
          print("Thanks for coming!!!",smile_emoji)
          print("Using of no.of entry's this Portal count : ",count)
          with open("taskapp.py", "r") as a:
              count = 0
              for i in a:
                  count += 1
              print(f"Total lines : {count}")

          if os.path.exists("taskapp.py"):
              end = time.time()
              result_time = end - start
              size = os.path.getsize("taskapp.py") / 1024
              print("File size : {:.2f}KB".format(size))
              print("Execution Time : ",result_time)
              break

        else:
            print(BOLD,ITALIC,NEGATIVE,"''If would like to continue this task please choose (1 To 4) numbers!!!''",RESET)
            time.sleep(2)

