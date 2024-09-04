import mysql.connector as cs

# Connect to MySQL database
conn = cs.connect(host='localhost', user='root', password='password', database='quiz')
if conn.is_connected():
    print("successfully connected")

print("******************** WELCOME TO TEST MANAGEMENT SYSTEM**")

# Initialize cursor for executing SQL commands
cur = conn.cursor()

# Display the main menu options
print("\t1.CREATE ACCOUNT")
print("\t2.LOGIN")
print("\t3.EXIT")

# Global variables to track user information
XZ2 = 0
y1 = ""

def exit():
    """Function to exit the application with a thank you message."""
    print("\tTHANK YOU FOR VISITING OUR SITE...")
    print("\tVISIT AGAIN...")

def table_existance():
    """Check for existing tables in the database.

    Returns:
        list: A list of all table names in the database.
    """
    cur.execute("SHOW TABLES;")
    fair = cur.fetchall()
    return fair

def create_test():
    """Create a new test in the system, including questions and answers."""
    d = str(input("ENTER YOUR TEST NAME:"))
    tup100 = (d,)
    
    # Check if the test name already exists
    if tup100 in table_existance():
        print(">>>Test name already existed, please enter another name!!!...")
        create_test()
    
    # Insert the new test into the tests_available table
    e = XZ2 + 1
    f = "INSERT INTO tests_available(s_no, test_name) VALUES({}, '{}')".format(e, d)
    cur.execute(f)
    conn.commit()
    
    # Create a new table for the test questions
    g = "CREATE TABLE " + d + "(Q_no INT, quest VARCHAR(200), o1 VARCHAR(150), o2 VARCHAR(150), o3 VARCHAR(150), o4 VARCHAR(150), correct_ansr INT);"    
    cur.execute(g)
    
    # Add questions to the test
    h = int(input("ENTER NO OF QUESTIONS: "))
    for i in range(1, h + 1):
        a10 = input("QUESTION: ")
        a20 = input("Option 1: ")
        a30 = input("Option 2: ")
        a40 = input("Option 3: ")
        a50 = input("Option 4: ")
        c10 = int(input("ENTER CORRECT OPTION NO (1, 2, 3, OR 4): "))
        
        # Insert the question and its options into the test table
        cur.execute("INSERT INTO " + d + "(Q_no, quest, o1, o2, o3, o4, correct_ansr) VALUES({}, '{}', '{}', '{}', '{}', '{}', {});".format(i, a10, a20, a30, a40, a50, c10))
        conn.commit()
    
    print("\t*!!!TEST CREATED!!!*")

def answer_test():
    """Allow a student to answer questions from an existing test."""
    tst_nm = input("Enter test name from the above list: ")
    jk = tst_nm.lower() + "_ans"
    nm = (jk,)
    
    # Fetch the questions from the test table
    ABC = "SELECT * FROM " + tst_nm + ";"
    cur.execute(ABC)
    DEF = cur.fetchall()
    HIJ = cur.rowcount
 
    # Check if the student has already answered the test
    if nm in table_existance():
        gg = "SELECT std_nm FROM " + tst_nm + "_ans"
        cur.execute(gg)
        ggf = cur.fetchall()
        jjk = (y1,)
        
        if jjk in ggf:
            print("\nYou have already answered this test, You cannot re-answer the test.")
            print("Do you want to exit: (Y/N):")
            yy = input()
            if yy.lower() == "n":
                answer_test()
            else:
                return
        
        # Initialize marks and begin the test
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
        
        # Store the student's marks in the database
        abcd = "INSERT INTO " + tst_nm + "_ans(std_nm, marks) VALUES('{}', {});".format(y1, marks)
        cur.execute(abcd)
        conn.commit()
        print("\tYour marks:", marks)
    
    else:
        # Create a new table for storing student answers and marks
        ans = "CREATE TABLE " + tst_nm + "_ans(std_nm CHAR(100), marks INT);"
        cur.execute(ans)
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
        
        # Store the student's marks in the newly created table
        abcd = "INSERT INTO " + tst_nm + "_ans(std_nm, marks) VALUES('{}', {});".format(y1, marks)
        cur.execute(abcd)
        conn.commit()
        print("\tYour marks:", marks)
    
    print("Thank you for answering our test...")

def login():
    """Handle user login and provide options for teachers and students."""
    global XZ2, y1

    print("LOGIN TO YOUR ACCOUNT...")
    print('''\t1. AS A TEACHER
              \t2. AS A STUDENT''')
    ch2 = int(input("ENTER YOUR CHOICE: "))
    
    if ch2 == 1:
        # Teacher login
        y1 = input("\tENTER YOUR ID: ")
        z1 = int(input("\tENTER YOUR PASSWORD: "))
        cur.execute("SELECT * FROM tests_available")
        XZ1 = cur.fetchall()
        XZ2 = cur.rowcount
        
        # Verify admin credentials
        if y1 == "admin" and z1 == 2022:
            print("Tests available...")
            for i in range(XZ2):
                a1 = XZ1[i][0]
                b1 = XZ1[i][1]
                print("\t", i + 1, ")  ", b1)
            
            print("Create tests...")
            create_test()
        else:
            print("Invalid Credentials!!")
            login()
    
    elif ch2 == 2:
        # Student login
        y1 = input("\tENTER YOUR NAME: ")
        z1 = int(input("\tENTER YOUR PASSWORD: "))
        cur.execute("SELECT * FROM tests_available")
        XZ1 = cur.fetchall()
        XZ2 = cur.rowcount
        cur.execute("SELECT * FROM accounts")
        x1 = cur.fetchall()
        x2 = cur.rowcount
        tup = (y1, z1)
        
        # Verify student credentials
        if tup in x1:
            for i in range(XZ2):
                a1 = XZ1[i][0]
                b1 = XZ1[i][1]
                print("\t", i + 1, ")  ", b1)
            answer_test()
        else:
            print("Invalid details!!")
            login()
    else:
        print("Invalid Input!!")
        login()
    

def existed_account():
    """Check if the account already exists in the database.

    Returns:
        list: A list of tuples containing existing account details.
    """
    cur.execute("SELECT * FROM accounts;")
    ex = cur.fetchall()
    return ex
   
def create():
    """Create a new user account and prompt the user to log in."""
    print("CREATE ACCOUNT")
    y = input("\tENTER YOUR NAME: ")
    z = int(input("\tENTER PASSWORD:"))
    
    # Check if the account already exists
    if (y, z) in existed_account():
        print("THIS ACCOUNT IS ALREADY EXISTED...")
        login()
    else:
        # Insert the new account into the accounts table
        a = "INSERT INTO accounts(name, pass) VALUES('{}', {});".format(y, z)
        cur.execute(a)
        conn.commit()
        print("YOU HAVE CREATED YOUR ACCOUNT...\nLogin to your Account\n")

        y1 = input("\tENTER YOUR NAME: ")
        z1 = int(input("\tENTER YOUR PASSWORD: "))
        cur.execute("SELECT * FROM tests_available")
        XZ1 = cur.fetchall()
        XZ2 = cur.rowcount
        cur.execute("SELECT * FROM accounts")
        x1 = cur.fetchall()
        x2 = cur.rowcount
        tup = (y1, z1)
        
        # Verify credentials after account creation
        if tup in x1:
            for i in range(XZ2):
                a1 = XZ1[i][0]
                b1 = XZ1[i][1]
                print("\t", a1, ")  ", b1)
            answer_test()

# Main program starts here
ch = int(input("ENTER YOUR CHOICE:"))
if ch == 1:
    create()
elif ch == 2:
    login()
elif ch == 3:
    exit()
else:
    print("Invalid Input!!!")
    exit()
