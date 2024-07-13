import mysql.connector
import taskapp
import time

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

database_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb"
)
cursors=database_connection.cursor()
def table_creation():

    table_create = '''
    CREATE TABLE IF NOT EXISTS taskapptable(
      user_id INT PRIMARY KEY AUTO_INCREMENT,
      user_name VARCHAR(30),
      user_password VARCHAR(30)
    )'''
    cursors.execute(table_create)
#table_creation()
username=''
passkey =''
name=''
password=''
def insert_table(name,password):
        detail_query = "SELECT * FROM taskapptable WHERE user_name = %s AND user_password = %s"
        cursors.execute(detail_query, (name, password))
        result = cursors.fetchall()
        if result:
            print("")
            print(NEGATIVE,"Already Available? Please try again!!!",RESET,verify_emoji)
            user_enter()
        else:
            insert_query = "INSERT INTO taskapptable (user_name,user_password) VALUES (%s, %s)"
            insert_item = (name,password)
            cursors.execute(insert_query,insert_item)
            database_connection.commit()
            print(BOLD,ITALIC,"\nAccount Successfully Created!!!",RESET,success_emoji)
            number=int(input(f"{BOLD}{ITALIC}If would you like to Signing Up now? Press (1) (or) Exit (2){RESET} {smile_emoji}:  "))
            if number == 1:
               checking_table(name,password)
            elif number == 2:
               print(f"\n{BOLD}{ITALIC}Thanks for using out Application {name}{RESET}{thanks_emoji}")
            else:
               print(NEGATIVE,"Choose Correct Number!!! Your sign out",RESET,hand_emoji)
        cursors.close()
        database_connection.close()


#insert_table(name,password)


def checking_table(name,passkey):
      detail_query="SELECT * FROM taskapptable WHERE user_name = %s AND user_password = %s"
      cursors.execute(detail_query,(name,passkey))
      result = cursors.fetchall()
      if result:
        taskapp.main(name)
      else:
          print(NEGATIVE,"User_name or Password wrong,Please try again!!!",RESET,verify_emoji)
          user_enter()
      cursors.close()
      database_connection.close()


def user_enter():
   print(BOLD,ITALIC)
   print("1.Create an account")
   print("2.Sign Up ")
   start = time.time()
   while True:
       if time.time()-start >5:
           print("Timeout reached. Program stopped.")
           break
       try:
          choose = int(input("Enter The Option (1/2) : "))
          print(RESET)
       except Exception:
           print("\n",NEGATIVE, "Only Numeric!!!", RESET, verify_emoji)
       else:
         if choose == 1:
          name = input("Name : ")
          password = input("Create password : ")
          insert_table(name,password)
         elif choose == 2:
           print(BOLD,ITALIC)
           username=input("Name : ")
           passkey = input("Password : ")
           print(RESET)
           checking_table(username,passkey)
         else:
           print(NEGATIVE,"Enter Correct Numbers!!!",RESET)
           user_enter()


user_enter()

def show_table():
    cursors.execute("SELECT * FROM taskapptable")
    result=cursors.fetchall()
    for i in result:
        print(i)
    cursors.close()
    database_connection.close()

#show_table()
