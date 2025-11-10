import mysql.connector

# connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",   # change if needed
    database="schooldb"
)

cur = db.cursor()

# Function 1 - Add student
def add_student():
    r = int(input("Enter Roll No: "))
    n = input("Enter Name: ")
    p = int(input("Enter Physics Marks: "))
    c = int(input("Enter Chemistry Marks: "))
    m = int(input("Enter Maths Marks: "))

    cur.execute("INSERT INTO marks VALUES (%s,%s,%s,%s,%s)", (r, n, p, c, m))
    db.commit()
    print("Student Added!\n")

# Function 2 - Show all students
def show_all():
    cur.execute("SELECT * FROM marks")
    data = cur.fetchall()
    print("\n--- All Students ---")
    for i in data:
        print("Roll:", i[0], "| Name:", i[1], "| Phy:", i[2], "| Chem:", i[3], "| Maths:", i[4])

# Function 3 - Search student
def search():
    r = int(input("Enter Roll No to search: "))
    cur.execute("SELECT * FROM marks WHERE rollno=%s", (r,))
    s = cur.fetchone()
    if s:
        print("Roll:", s[0], "| Name:", s[1], "| Phy:", s[2], "| Chem:", s[3], "| Maths:", s[4])
    else:
        print("No record found!")

# Function 4 - Update marks
def update_marks():
    r = int(input("Enter Roll No to update: "))
    p = int(input("Enter new Physics Marks: "))
    c = int(input("Enter new Chemistry Marks: "))
    m = int(input("Enter new Maths Marks: "))
    cur.execute("UPDATE marks SET physics=%s, chemistry=%s, maths=%s WHERE rollno=%s", (p, c, m, r))
    db.commit()
    print("Marks Updated!\n")

# Function 5 - Delete student
def delete_student():
    r = int(input("Enter Roll No to delete: "))
    cur.execute("DELETE FROM marks WHERE rollno=%s", (r,))
    db.commit()
    print("Student Deleted!\n")

# Main Menu Loop
while True:
    print("\n===== SCHOOL MARKS MENU =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        add_student()
    elif ch == '2':
        show_all()
    elif ch == '3':
        search()
    elif ch == '4':
        update_marks()
    elif ch == '5':
        delete_student()
    elif ch == '6':
        print("Bye! Have a great day!")
        break
    else:
        print("Please enter a number from 1 to 6")
