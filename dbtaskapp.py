import mysql.connector
NEGATIVE = "\033[7m"
RESET = '\033[0m'
BOLD = "\033[1m"
ITALIC = "\033[3m"

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
name,password = "John","Person547@#$"
def insert_table(name,password):
        insert_query = "INSERT INTO taskapptable (user_name,user_password) VALUES (%s, %s)"
        insert_item = (name,password)
        cursors.execute(insert_query,insert_item)
        database_connection.commit()
        cursors.close()
        database_connection.close()


#insert_table(name,password)

def user_info():
    print(f"Welcome Details Session!!!")
def checking_table(name,passkey):
      cursors.execute("SELECT * FROM taskapptable")
      result = cursors.fetchall()
      for i in result:
          if (i[1] and i[2]) == (name and passkey):
              print(f"{ITALIC}{BOLD}Hi! {i[1]} Welcome{RESET}")
              break

      else:
              print(NEGATIVE,"Wrong User_name (or) Password!!!",RESET)

username=input("Name : ")
passkey = input("Password : ")
checking_table(name,passkey)

def user_info():
    print(f"Welcome Details Session!!!")