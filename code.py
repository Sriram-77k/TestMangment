import mysql.connector as cs
conn=cs.connect(host='localhost',user='root',password='aditya',database='quiz')
if conn.is_connected():
    print("successfully connected")


print("******************** WELCOME TO TEST MANAGEMENT SYSTEM**")
cur=conn.cursor()
print("\t1.CREATE ACCOUNT")
print("\t2.LOGIN")
print("\t3.EXIT")
XZ2=0
y1=""

def exit():
    print("\tTHANKYOU FOR VISITING OUR SITE...")
    print("\tVISIT AGAIN...")

def table_existance():
    cur.execute("show tables;")
    fair=cur.fetchall()
    return fair

def create_test():
    d=str(input("ENTER YOUR TEST NAME:"))
    tup100=(d,)
    if tup100 in table_existance():
        print(">>>Test name already existed please enter another name!!!...")
        create_test()
    e=XZ2+1
    f="insert into tests_available(s_no,test_name) values({},'{}')". format(e,d)
    cur.execute(f)
    conn.commit()
    g="create table "+d+"(Q_no int,quest varchar(200),o1 varchar(150),o2 varchar(150),o3 varchar(150),o4 varchar(150),correct_ansr int);"    
    cur.execute(g)
    h=int(input("ENTER NO OF QUESTION: "))
    for i in range(1,h+1):
        a10=input("QUESTION:")
        a20=input("Option1: ")
        a30=input("option2: ")
        a40=input("option3: ")
        a50=input("option4: ")
        c10=int(input("ENTER CORRECT OPTION NO(1,2,3,(OR)4): "))
        cur.execute("insert into "+d+"(Q_no,quest,o1,o2,o3,o4,correct_ansr) values({},'{}','{}','{}','{}','{}',{});".format(i,a10,a20,a30,a40,a50,c10))
        conn.commit()
    print("\t*!!!TEST CREATED!!!*")

def answer_test():
    tst_nm=input("Enter test name from above list: ")
    jk=tst_nm.lower()+"_ans"
    nm=(jk,)
    ABC="select * from "+tst_nm+";"
    cur.execute(ABC)
    DEF=cur.fetchall()
    HIJ=cur.rowcount
 
    if nm in  table_existance():
         gg="select std_nm from "+tst_nm+"_ans"
         cur.execute(gg)
         ggf=cur.fetchall()
         jjk=(y1,)
         if jjk in ggf:
             print("\nyou have already answered this test,You cannot re-answer the test")
             print("Do you want to exit:(Y/N):")
             yy=input()
             if(yy.lower()=="n"):
                 answer_test()
             else:
                 return
         marks=0
         for i in range(HIJ):
            print(DEF[i][0],') ',DEF[i][1])
            print('\t1)',DEF[i][2])
            print('\t2)',DEF[i][3])
            print('\t3)',DEF[i][4])
            print('\t4)',DEF[i][5])
            CH3=int(input("ENTER CORRECT OPTION(1 OR 2 OR 3 OR 4): "))
            if CH3==DEF[i][6]:
                marks+=1
         abcd="insert into "+tst_nm+"_ans(std_nm,marks) values('{}',{})".format(y1,marks)
         cur.execute(abcd)
         conn.commit()
         print("\tyour marks:",marks)
    else:
        ans="create table "+tst_nm+"_ans(std_nm char(100),marks int);"
        cur.execute(ans)
        marks=0
        for i in range(HIJ):
            print(DEF[i][0],') ',DEF[i][1])
            print('\t1)',DEF[i][2])
            print('\t2)',DEF[i][3])
            print('\t3)',DEF[i][4])
            print('\t4)',DEF[i][5])
            CH3=int(input("ENTER CORRECT OPTION(1 OR 2 OR 3 OR 4): "))
            if CH3==DEF[i][6]:
                marks+=1
        abcd="insert into "+tst_nm+"_ans(std_nm,marks) values('{}',{})".format(y1,marks)
        cur.execute(abcd)
        conn.commit()
        print("\tyour marks:",marks)
    print("Thankyou for answering our test.....")
         
def login():
    global XZ2 ,y1

    print("LOGIN TO YOUR ACCOUNT...")
    print('''\t1.AS A TEACHER
              \t2.AS A STUDENT''')
    ch2=int(input("ENTER YOUR CHOICE: "))
    if ch2==1:
        y1=input("\tENTER YOUR ID: ")
        z1=int(input("\tENTER YOUR PASSWORD: "))
        cur.execute("select * from tests_available")
        XZ1=cur.fetchall()
        XZ2=cur.rowcount
        if y1=="admin" and z1==2022:
            print("Tests available...")
            for i in range(XZ2):
                a1=XZ1[i][0]
                b1=XZ1[i][1]
                print("\t",i+1,")  ",b1)
            print("Create tests...")
            create_test()
        else:
            print("Invalid Credentials!!")
            login()
    elif ch2==2:
        y1=input("\tENTER YOUR name: ")
        z1=int(input("\tENTER YOUR PASSWORD: "))
        cur.execute("select * from tests_available")
        XZ1=cur.fetchall()
        XZ2=cur.rowcount
        cur.execute("select * from accounts")
        x1=cur.fetchall()
        x2=cur.rowcount
        tup=(y1,z1)
        if tup in x1:
            for i in range(XZ2):
                a1=XZ1[i][0]
                b1=XZ1[i][1]
                print("\t",i+1,")  ",b1)
            answer_test()
        else:
            print("Invalid details!!")
            login()
    else:
        print("Invalid Input!!")
        login()
    

    
       
def existed_account():
    cur.execute("select * from accounts;")
    ex=cur.fetchall()
    return ex
   
def create():
    print("CREATE ACCOUNT")
    y=input("\tENTER YOUR NAME: ")
    z=int(input("\tENTER PASSWORD:"))
    if (y,z) in existed_account():
        print("THIS ACCOUNT IS ALREADY EXISTED...")
        login()
    else:
        a="insert into accounts(name,pass)values('{}',{})".format(y,z)
        cur.execute(a)
        conn.commit()
        print("YOU HAVE CREATED YOUR ACCOUNT...\nLogin to ur Account\n")

        y1=input("\tENTER YOUR name: ")
        z1=int(input("\tENTER YOUR PASSWORD: "))
        cur.execute("select * from tests_available")
        XZ1=cur.fetchall()
        XZ2=cur.rowcount
        cur.execute("select * from accounts")
        x1=cur.fetchall()
        x2=cur.rowcount
        tup=(y1,z1)
        if tup in x1:
            for i in range(XZ2):
                a1=XZ1[i][0]
                b1=XZ1[i][1]
                print("\t",a1,")  ",b1)
            answer_test()
       
ch1=int(input("ENTER YOUR CHOICE: "))
if ch1==1:
    create()
if ch1==2:
    login()
else:
    exit()
