import sqlite3 as cs
import sys

def exit():
    """Function to exit the application with a thank you message."""
    print("\tTHANK YOU FOR VISITING OUR SITE...")
    print("\tVISIT AGAIN...")
    sys.exit(0)

def initialize_db():
    """Create necessary tables if they do not exist."""
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS accounts (
                        name TEXT PRIMARY KEY,
                        pass INT
                    );''')
        
        cur.execute('''CREATE TABLE IF NOT EXISTS tests_available (
                        s_no INT PRIMARY KEY,
                        test_name TEXT
                    );''')

        print("Database initialized.")
    except cs.Error as e:
        print(f"Error Code 1000: Failed to initialize the database. {e}")
        sys.exit(1)

try:
    # Connect to SQLite database
    conn = cs.connect('quiz.db')  # SQLite uses a file-based database
    print("Successfully connected")
except cs.Error as e:
    print(f"Error Code 1001: Failed to connect to the database. {e}")
    sys.exit(1)

# Initialize cursor for executing SQL commands
cur = conn.cursor()

# Initialize database
initialize_db()

print("******************** WELCOME TO TEST MANAGEMENT SYSTEM**")

# Display the main menu options
print("\t1. CREATE ACCOUNT")
print("\t2. LOGIN")
print("\t3. EXIT")

# Global variables to track user information
XZ2 = 0
y1 = ""

def table_existance():
    """Check for existing tables in the database.

    Returns:
        list: A list of all table names in the database.
    """
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        fair = cur.fetchall()
        return [t[0] for t in fair]
    except cs.Error as e:
        print(f"Error Code 1002: Failed to check table existence. {e}")
        return []

def create_test():
    """Create a new test in the system, including questions and answers."""
    global XZ2
    d = str(input("ENTER YOUR TEST NAME:"))
    tup100 = (d,)

    if tup100 in [(table[0],) for table in table_existance()]:
        print(">>>Test name already exists, please enter another name!!!...")
        create_test()
    
    try:
        e = XZ2 + 1
        f = "INSERT INTO tests_available(s_no, test_name) VALUES(?, ?)"
        cur.execute(f, (e, d))
        conn.commit()
        
        g = f"CREATE TABLE IF NOT EXISTS {d}(Q_no INT, quest TEXT, o1 TEXT, o2 TEXT, o3 TEXT, o4 TEXT, correct_ansr INT);"
        cur.execute(g)
        
        h = int(input("ENTER NO OF QUESTIONS: "))
        for i in range(1, h + 1):
            a10 = input("QUESTION: ")
            a20 = input("Option 1: ")
            a30 = input("Option 2: ")
            a40 = input("Option 3: ")
            a50 = input("Option 4: ")
            c10 = int(input("ENTER CORRECT OPTION NO (1, 2, 3, OR 4): "))
            cur.execute(f"INSERT INTO {d}(Q_no, quest, o1, o2, o3, o4, correct_ansr) VALUES(?, ?, ?, ?, ?, ?, ?);",
                        (i, a10, a20, a30, a40, a50, c10))
            conn.commit()
        
        print("\t*!!!TEST CREATED!!!*")
    
    except cs.Error as e:
        print(f"Error Code 1003: Failed to create the test. {e}")

def answer_test():
    """Allow a student to answer questions from an existing test."""
    tst_nm = input("Enter test name from the above list: ")
    jk = tst_nm.lower() + "_ans"
    nm = (jk,)

    try:
        # Check if the test table exists
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tst_nm}';")
        table_exists = cur.fetchone()
        
        if not table_exists:
            print(f"Error Code 1004: The table for the test '{tst_nm}' does not exist. Please check the test name.")
            return
        
        # Proceed with answering the test
        cur.execute(f"SELECT * FROM {tst_nm};")
        DEF = cur.fetchall()
        HIJ = len(DEF)
        
        # Check if the answers table exists
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{jk}';")
        answers_table_exists = cur.fetchone()
        
        if answers_table_exists:
            cur.execute(f"SELECT std_nm FROM {jk};")
            ggf = cur.fetchall()
            jjk = (y1,)
            
            if jjk in ggf:
                print("\nYou have already answered this test, You cannot re-answer the test.")
                yy = input("Do you want to exit: (Y/N): ")
                if yy.lower() == "n":
                    answer_test()
                else:
                    return
            
            marks = 0
            for i in range(HIJ):
                print(DEF[i][0], ') ', DEF[i][1])
                print('\t1) ', DEF[i][2])
                print('\t2) ', DEF[i][3])
                print('\t3) ', DEF[i][4])
                print('\t4) ', DEF[i][5])
                CH3 = int(input("ENTER CORRECT OPTION (1 OR 2 OR 3 OR 4): "))
                if CH3 == DEF[i][6]:
                    marks += 1
            
            cur.execute(f"INSERT INTO {jk}(std_nm, marks) VALUES(?, ?);", (y1, marks))
            conn.commit()
            print("\tYour marks:", marks)
        
        else:
            cur.execute(f"CREATE TABLE {jk}(std_nm TEXT, marks INT);")
            marks = 0
            
            for i in range(HIJ):
                print(DEF[i][0], ') ', DEF[i][1])
                print('\t1) ', DEF[i][2])
                print('\t2) ', DEF[i][3])
                print('\t3) ', DEF[i][4])
                print('\t4) ', DEF[i][5])
                CH3 = int(input("ENTER CORRECT OPTION (1 OR 2 OR 3 OR 4): "))
                if CH3 == DEF[i][6]:
                    marks += 1
            
            cur.execute(f"INSERT INTO {jk}(std_nm, marks) VALUES(?, ?);", (y1, marks))
            conn.commit()
            print("\tYour marks:", marks)
        
        print("Thank you for answering our test...")
    
    except cs.Error as e:
        print(f"Error Code 1004: Failed to answer the test. {e}")


def login():
    """Handle user login and provide options for teachers and students."""
    global XZ2, y1

    print("LOGIN TO YOUR ACCOUNT...")
    print('''\t1. AS A TEACHER
              \t2. AS A STUDENT''')
    ch2 = int(input("ENTER YOUR CHOICE: "))
    
    if ch2 == 1:
        y1 = input("\tENTER YOUR ID: ")
        z1 = int(input("\tENTER YOUR PASSWORD: "))
        try:
            cur.execute("SELECT * FROM tests_available;")
            XZ1 = cur.fetchall()
            XZ2 = len(XZ1)
            
            if y1 == "admin" and z1 == 2022:
                print("Tests available...")
                for i in range(XZ2):
                    print("\t", i + 1, ")  ", XZ1[i][1])
                
                print("Create tests...")
                create_test()
            else:
                print("Invalid Credentials!!")
                login()
        
        except cs.Error as e:
            print(f"Error Code 1005: Failed to process teacher login. {e}")
    
    elif ch2 == 2:
        y1 = input("\tENTER YOUR NAME: ")
        z1 = int(input("\tENTER YOUR PASSWORD: "))
        try:
            cur.execute("SELECT * FROM tests_available;")
            XZ1 = cur.fetchall()
            XZ2 = len(XZ1)
            cur.execute("SELECT * FROM accounts;")
            x1 = cur.fetchall()
            tup = (y1, z1)
            
            if tup in x1:
                for i in range(XZ2):
                    print("\t", i + 1, ")  ", XZ1[i][1])
                answer_test()
            else:
                print("Invalid details!!")
                login()
        
        except cs.Error as e:
            print(f"Error Code 1006: Failed to process student login. {e}")
    else:
        print("Invalid Input!!")
        login()

def existed_account():
    """Check if the account already exists in the database.

    Returns:
        list: A list of tuples containing existing account details.
    """
    try:
        cur.execute("SELECT * FROM accounts;")
        ex = cur.fetchall()
        return ex
    except cs.Error as e:
        print(f"Error Code 1007: Failed to check existing accounts. {e}")
        return []

def create():
    """Create a new user account and prompt the user to log in."""
    print("CREATE ACCOUNT")
    y = input("\tENTER YOUR NAME: ")
    z = int(input("\tENTER PASSWORD:"))

    if (y, z) in existed_account():
        print("THIS ACCOUNT ALREADY EXISTS...")
        login()
    else:
        try:
            cur.execute("INSERT INTO accounts(name, pass) VALUES(?, ?);", (y, z))
            conn.commit()
            print("YOU HAVE CREATED YOUR ACCOUNT...\nLogin to your Account\n")

            y1 = input("\tENTER YOUR NAME: ")
            z1 = int(input("\tENTER YOUR PASSWORD: "))
            cur.execute("SELECT * FROM tests_available;")
            XZ1 = cur.fetchall()
            XZ2 = len(XZ1)
            cur.execute("SELECT * FROM accounts;")
            x1 = cur.fetchall()
            tup = (y1, z1)
            
            if tup in x1:
                for i in range(XZ2):
                    print("\t", XZ1[i][0], ")  ", XZ1[i][1])
                answer_test()
        
        except cs.Error as e:
            print(f"Error Code 1008: Failed to create an account. {e}")

# Main program starts here
try:
    ch = int(input("ENTER YOUR CHOICE: "))
    if ch == 1:
        create()
    elif ch == 2:
        login()
    elif ch == 3:
        exit()
    else:
        print("Invalid Input!!!")
        exit()
except cs.Error as e:
    print(f"Error Code 1009: Failed during main program execution. {e}")
