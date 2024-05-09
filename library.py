from tkinter import *
import tkinter as Tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('library3.db')  #connecting to the sqlite database
cursor = conn.cursor() #creating a cursor

#cursor.execute(''' CREATE TABLE IF NOT EXISTS admin1 (Admin_Code)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS admin2 (Admin_Code)''')

# cursor.execute("insert into admin2 values(:admin)",
#         {
#             'admin':'nikhil123'
#         })

# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B6',1, 1, '001A03')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B6',2, 1, '001A03')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B6',3, 1, '001A03')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B6',3, 2, '001A03')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B6',2, 1, '001A03')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B6',6, 1, '001A03')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B7',1, 4, '001A04')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B7',2, 4, '001A04')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B7',1, 5, '001A04')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B7',2, 5, '001A04')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B7',3, 5, '001B01')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B7',1, 1, '001B01')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B7',1, 3, '001B02')")

# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',1, 1, '501A32')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',2, 1, '124A79')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',3, 1, '760A15')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',4, 1, '302A44')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',5, 1, '618A81')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',6, 1, '905A23')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',7, 1, '432A60')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',8, 1, '215A99')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',9, 1, '701A12')")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B8',10, 1, '843A67')")

# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 1, '2023-01-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 2, '2023-02-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 3, '2023-03-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 4, '2023-04-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 5, '2023-05-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 6, '2023-06-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 7, '2023-07-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 8, '2023-08-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 9, '2023-09-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 1, 'B8', 10, '2023-10-01 13:45:00')")

# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 1, '2023-01-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 2, '2023-02-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 3, '2023-03-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 4, '2023-04-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 5, '2023-05-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 6, '2023-06-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 7, '2023-07-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 8, '2023-08-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 9, '2023-09-01 13:45:00')")
# cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES ('R10', 2, 'B8', 10, '2023-10-01 13:45:00')")


# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B9', 10, 4, '001C05');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B9', 1, 4, '001C05');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B9', 1, 5, '001D01');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B9', 3, 5, '001D01');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B9', 3, 4, '001D01');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B9', 4, 2, '001D01');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B9', 5, 5, '001E01');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B10', 1, 1, '001E01');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B10', 2, 1, '001E01');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B10', 1, 2, '001A10');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B10', 2, 3, '001A10');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B10', 3, 2, '001A10');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B10', 4, 3, '001A10');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B10', 5, 4, '001A10');")
# cursor.execute("INSERT INTO copy (docid,copyno,bid,position) VALUES ('B10', 6, 4, '001A10');")

#cursor.execute("INSERT INTO publisher (Publisherid, Pubname, Address) VALUES (71205, 'Donall Linskey', '85 Crownhardt Place')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (87373, 'Maddi Leah', '55 Sauthoff Street')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (26915, 'Ernest Poulsom', '4421 Morningstar Hill')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (47438, 'Eleonora Ruthen', '9 Gina Trail')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (25064, 'Buck Gunstone', '21916 Sutteridge Place')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (21148, 'Averil Harroll', '90615 Truax Way')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (68241, 'Randene Thow', '302 Towne Plaza')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (79166, 'Marcela Beddow', '66 Upham Circle')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (75158, 'Westleigh Filyakov', '9679 6th Trail')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (21515, 'Ruddy Yeskov', '4326 Marquette Avenue')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (29511, 'Verla Spada', '9 5th Pass')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (41257, 'Calv Fearnside', '898 Northwestern Point')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (22217, 'Christie Pretious', '72 Lighthouse Bay Alley')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (37433, 'Beverie Budgen', '6 Gulseth Circle')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (94273, 'Biron Carslake', '9692 Menomonie Trail')")
# cursor.execute("INSERT INTO publisher (publisherid, pubname, address) VALUES (12275, 'Dacie Ridge', '6 Waxwing Point')")

from datetime import datetime



#cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES (?, ?, ?, ?, ?)", ('R10', 2, 'B6', 3, '2014-05-01 13:45:00'))
#cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES (?, ?, ?, ?, ?)", ('R10', 2, 'B6', 1, '2014-05-01 13:45:00'))



cursor.execute("""CREATE TABLE if not exists logins_readers (Fullname,ID,orgphonenumber)""")
cursor.execute("""CREATE TABLE if not exists logins_admin (Fullname,SSN,orgphonenumber,emailid,password)""")
cursor.execute("""CREATE TABLE if not exists Book (DocID,ISBN)""")
cursor.execute(''' CREATE TABLE IF NOT EXISTS Branch (BID,LName,Location)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS JournalVolume (DocID, VolumeNo, IssueNo, Editor, GId, Scope)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Proceeding  (DocID, CDate , CLocation, CChair)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Publisher (PublisherID, PubName, Address)''')
#cursor.execute(''' CREATE TABLE IF NOT EXISTS Borrowing2 (RDTime,RID,BID,DocID,CopyNo)''')
#cursor.execute('''ALTER TABLE Borrowing2 ADD COLUMN RDTime DATE;''')

cursor.execute("""CREATE TABLE IF NOT EXISTS Reservation2 (
                    RID TEXT,
                    BID TEXT,
                    DocID TEXT,
                    CopyNo TEXT,
                    RTime DATETIME,
                    PRIMARY KEY (RID, DocID, CopyNo, BID),
                    FOREIGN KEY (RID) REFERENCES Reader (RID),
                    FOREIGN KEY (DocID, CopyNo, BID) REFERENCES Copy (DocID, CopyNo, BID)
                )""")

cursor.execute('''CREATE TABLE IF NOT EXISTS Borrowing2 (
    RID TEXT,
    BID INTEGER,
    DocID TEXT,
    CopyNo INTEGER,
    BDTime DATETIME,
    PRIMARY KEY (RID, BID, DocID, CopyNo),
    FOREIGN KEY (RID) REFERENCES logins_readers(ID),
    FOREIGN KEY (BID) REFERENCES Branch(BID),
    FOREIGN KEY (DocID, CopyNo) REFERENCES Copy(DocID, CopyNo)
);
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Returning2 (
    RID TEXT,
    CopyNo INTEGER,
    DocID TEXT,
    BID INTEGER,
    RDateTime TEXT,
    PRIMARY KEY (RID, CopyNo, DocID, BID),
    FOREIGN KEY (RID) REFERENCES logins_readers(ID),
    FOREIGN KEY (DocID, CopyNo, BID) REFERENCES Copy(DocID, CopyNo, BID)
);
''')


# Execute the SQL query to delete the table
# cursor.execute("DROP TABLE IF EXISTS Borrowing2")
# cursor.execute("DROP TABLE IF EXISTS Returning2")

def print_borrowing2():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the Borrowing2 table
    cursor.execute("SELECT * FROM Borrowing2")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    conn.close()



# print_b2

# Call the function to print the Borrowing2 values
print_borrowing2()

cursor.execute('select * from admin2')
r=cursor.fetchall()
print(r)
root = Tk.Tk()
root.title('Library')
root.geometry('400x600')



def adminstrator_page():
    global root1
    root1 = Toplevel(root)
    global adminstrator_password_entry 
    global adminstrator_username_entry
    adminstrator_label = Tk.Label(root1, text="Type Administrator details")
    adminstrator_label.pack()
    adminstrator_username_label = Tk.Label(root1, text="Login ID")
    adminstrator_username_entry = Tk.Entry(root1)
    adminstrator_password_label = Tk.Label(root1, text="Password")
    adminstrator_password_entry = Tk.Entry(root1, show="*")
    adminstrator_login_button = Tk.Button(root1, text="Login", command=lambda:admin_login(adminstrator_username_entry.get(), adminstrator_password_entry.get()))
    adminstrator_label1 = Tk.Label(root1, text="Are you a new user?")
    adminstrator_button1 = Tk.Button(root1, text="Create an account", command=checkadmin)

    adminstrator_username_label.pack()
    adminstrator_username_entry.pack()
    adminstrator_password_label.pack()
    adminstrator_password_entry.pack()
    adminstrator_login_button.pack()
    adminstrator_label1.pack()
    adminstrator_button1.pack()

def admin_login(username, password):
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Perform a query to check if the username and password match a record in the database
    cursor.execute("SELECT * FROM logins_admin WHERE emailid = ? AND password = ?", (username, password))
    row = cursor.fetchone()

    if row:
        admin_submenu()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

    conn.close()

def reader_page():
    global root1
    root1=Toplevel(root)
    reader_label = Tk.Label(root1, text = "Type Reader details")
    reader_label.pack()
    reader_cardnumber_label = Tk.Label(root1, text ="Card Number")
    reader_cardnumber_entry = Tk.Entry(root1)
    reader_login_button = Tk.Button(root1, text = "Login", command=lambda: reader_login(reader_cardnumber_entry.get()))
    reader_cardnumber_label.pack()
    reader_cardnumber_entry.pack()
    reader_login_button.pack()

def reader_login(ID):
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Perform a query to check if the username and password match a record in the database
    cursor.execute("SELECT * FROM logins_readers WHERE ID = ?", (ID,))
    row = cursor.fetchone()

    if row:
        reader_submenu()
    else:
        messagebox.showerror("Login Failed", "Invalid ID")

    conn.close()

def admin_submenu():
    global root2
    root1.withdraw()
    # root.withdraw()
    root2= Toplevel(root1)
    admin_button1 = Tk.Button(root2, text = "Add a Document Copy", command = Document1)
    admin_button1.pack()
    admin_button2 = Tk.Button(root2, text = "Search a Document Copy", command = search_document_copy)
    admin_button2.pack()
    admin_button3 = Tk.Button(root2, text = "Add a reader", command=create_reader)
    admin_button3.pack()
    admin_button4 = Tk.Button(root2, text = "Print Branch Info", command= print_branch_info1)
    admin_button4.pack()
    admin_button5 = Tk.Button(root2, text = "Get Borrowers Info per Branch", command = get_top_borrowers_per_branch)
    admin_button5.pack()
    admin_button6 = Tk.Button(root2, text = "Get N most frequent borrowers", command = get_top_borrowers_all_branches)
    admin_button6.pack()
    admin_button7 = Tk.Button(root2, text = "Get N most borrowed books per branch", command = get_most_borrowed_books_per_branch)
    admin_button7.pack()
    admin_button8 = Tk.Button(root2, text = "Get N most borrowed books", command = get_most_borrowed_books)
    admin_button8.pack()
    admin_button9 = Tk.Button(root2, text = "Get top 10 books per year", command = get_top_books_per_year)
    admin_button9.pack()
    admin_button10 = Tk.Button(root2, text = "Get Avg Fine per branch per time")#, command = avg_fine)
    admin_button10.pack()
    admin_button11 = Tk.Button(root2, text = "Quit", command=Quit)
    admin_button11.pack()
    admin_button12 = Tk.Button(root2, text = "Add a copy", command = Create_copy)
    admin_button12.pack()
    admin_button13 = Tk.Button(root2, text = "Add Document Details", command = Create_doc_details)
    admin_button13.pack()
    admin_button14 = Tk.Button(root2, text = "Add Publisher Details", command = Create_pub_details)
    admin_button14.pack()

from tkinter import simpledialog


# def get_top_books_per_year():
#     year_input = simpledialog.askstring("Input", "Enter the year:")
#     if year_input:
#         try:
#             year = int(year_input)
#             conn = sqlite3.connect('library3.db')
#             cursor = conn.cursor()

#             # Query to get the top 10 most borrowed books of the given year
#             cursor.execute("""
#                 SELECT DocID, COUNT(*) AS BorrowCount
#                 FROM Borrowing2
#                 WHERE strftime('%Y', BDTime) = ?
#                 GROUP BY DocID
#                 ORDER BY BorrowCount DESC
#                 LIMIT 10
#             """, (str(year),))
#             top_books = cursor.fetchall()

#             if top_books:
#                 print(f"Top 10 books for the year {year}:")
#                 for i, book in enumerate(top_books, start=1):
#                     print(f"{i}. DocID: {book[0]}, Borrow Count: {book[1]}")
#             else:
#                 print("No books found for the given year.")

#             conn.close()
#         except ValueError:
#             messagebox.showerror("Error", "Invalid input. Please enter a valid year.")


def get_top_books_per_year():
    # Function to get the top 10 most popular books of a given year in the library
    year_input = simpledialog.askstring("Input", "Enter the year:")
    if year_input is not None:
        try:
            year = int(year_input)
            conn = sqlite3.connect('library3.db')
            cursor = conn.cursor()

            # Get the top 10 most borrowed books for the given year
            query = """
            SELECT DocID, COUNT(*) AS BorrowCount
            FROM Borrowing2
            WHERE strftime('%Y', BDTime) = ?
            GROUP BY DocID
            ORDER BY BorrowCount DESC
            LIMIT 10
            """
            cursor.execute(query, (str(year),))
            books = cursor.fetchall()

            if books:
                print("Top 10 most popular books in", year, ":")
                for i, book in enumerate(books, 1):
                    print(f"{i}. DocID: {book[0]}, Borrow Count: {book[1]}")
            else:
                print("No data found for the given year.")

            conn.close()
        except ValueError:
            print("Invalid input. Please enter a valid year.")
    else:
        print("No year entered.")


def get_most_borrowed_books_per_branch():
        n = int(input("Enter the number of books: "))
        branch_number = int(input("Enter the branch number: "))

        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()

        cursor.execute("SELECT DocID, COUNT(*) as BorrowCount FROM Borrowing2 WHERE BID = ? GROUP BY DocID ORDER BY BorrowCount DESC LIMIT ?", (branch_number, n))
        books = cursor.fetchall()

        for book in books:
            print(f"Document ID: {book[0]}, Number of Borrows: {book[1]}")

        conn.close()

def get_most_borrowed_books():
        n = int(input("Enter the number of books: "))

        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()

        cursor.execute("SELECT DocID, COUNT(*) as BorrowCount FROM Borrowing2 GROUP BY DocID ORDER BY BorrowCount DESC LIMIT ?", (n,))
        books = cursor.fetchall()

        for book in books:
            print(f"Document ID: {book[0]}, Number of Borrows: {book[1]}")

        conn.close()



def get_top_borrowers_per_branch():
    global root3
    root2.withdraw()
    root3 = Toplevel(root2)
    root3.title("Top N Borrowers per Branch")

    Label(root3, text="Enter Branch Number:").pack()
    branch_number_entry = Entry(root3)
    branch_number_entry.pack()

    Label(root3, text="Enter N:").pack()
    n_entry = Entry(root3)
    n_entry.pack()

    def display_top_borrowers():
        branch_number = branch_number_entry.get()
        n = int(n_entry.get())

        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()

        # Check if branch exists
        cursor.execute("SELECT * FROM Branch WHERE BID = ?", (branch_number,))
        branch_exists = cursor.fetchone()

        if not branch_exists:
            conn.close()
            messagebox.showerror("No branch found", f"No branch with ID {branch_number} found")
            return

        # Query to get top N borrowers in a branch
        cursor.execute("SELECT B.RID, L.Fullname, COUNT(*) AS num_borrowed FROM Borrowing2 B JOIN logins_readers L ON B.RID = L.ID WHERE B.BID = ? GROUP BY B.RID ORDER BY num_borrowed DESC LIMIT ?", (branch_number, n))
        top_borrowers = cursor.fetchall()

        conn.close()

        # Display top borrowers using treeview
        top_borrowers_window = Toplevel(root3)
        top_borrowers_window.title("Top Borrowers")

        tree = ttk.Treeview(top_borrowers_window, columns=("Reader ID", "Name", "Books Borrowed"), show='headings')
        tree.heading("Reader ID", text="Reader ID")
        tree.heading("Name", text="Name")
        tree.heading("Books Borrowed", text="Books Borrowed")

        for borrower in top_borrowers:
            tree.insert("", "end", values=(borrower[0], borrower[1], borrower[2]))

        tree.pack()

    display_button = Button(root3, text="Display", command=display_top_borrowers)
    display_button.pack()

def get_top_borrowers_all_branches():
    global root3
    root2.withdraw()
    root3 = Toplevel(root2)
    root3.title("Top N Most Frequent Borrowers")

    Label(root3, text="Enter N:").pack()
    n_entry = Entry(root3)
    n_entry.pack()

    def display_top_borrowers():
        n = int(n_entry.get())

        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()

        # Query to get top N borrowers across all branches
        cursor.execute("SELECT B.RID, L.Fullname, COUNT(*) AS num_borrowed FROM Borrowing2 B JOIN logins_readers L ON B.RID = L.ID GROUP BY B.RID ORDER BY num_borrowed DESC LIMIT ?", (n,))
        top_borrowers = cursor.fetchall()

        conn.close()

        # Display top borrowers using treeview
        top_borrowers_window = Toplevel(root3)
        top_borrowers_window.title("Top Borrowers")

        tree = ttk.Treeview(top_borrowers_window, columns=("Reader ID", "Name", "Books Borrowed"), show='headings')
        tree.heading("Reader ID", text="Reader ID")
        tree.heading("Name", text="Name")
        tree.heading("Books Borrowed", text="Books Borrowed")

        for borrower in top_borrowers:
            tree.insert("", "end", values=(borrower[0], borrower[1], borrower[2]))

        tree.pack()

    display_button = Button(root3, text="Display", command=display_top_borrowers)
    display_button.pack()


# def search_document_copy():
#     global search_window
#     search_window = Toplevel(root2)
#     search_window.title("Search Document Copy")

#     Label(search_window, text="Document ID:").pack()
#     doc_id_entry = Entry(search_window)
#     doc_id_entry.pack()

#     tree = ttk.Treeview(search_window)
#     tree["columns"] = ("Copy Number", "Status")
#     tree.column("#0", width=0, stretch=NO)
#     tree.column("Copy Number", anchor=W, width=100)
#     tree.column("Status", anchor=W, width=100)

#     tree.heading("#0", text="", anchor=W)
#     tree.heading("Copy Number", text="Copy Number", anchor=W)
#     tree.heading("Status", text="Status", anchor=W)

#     def search_copy_status():
#         doc_id = doc_id_entry.get()

#         # Clear the tree view
#         for item in tree.get_children():
#             tree.delete(item)

#         conn = sqlite3.connect('library3.db')
#         cursor = conn.cursor()

#         # Fetch all copies of the document
#         cursor.execute("SELECT CopyNo FROM Copy WHERE DocID = ?", (doc_id,))
#         copies = cursor.fetchall()

#         for copy_number in copies:
#             copy_number = copy_number[0]
#             # Check if the document copy is borrowed or reserved
#             cursor.execute("SELECT * FROM Borrowing2 WHERE DocID = ? AND CopyNo = ?", (doc_id, copy_number))
#             borrowed_record = cursor.fetchone()

#             cursor.execute("SELECT * FROM Reservation2 WHERE DocID = ? AND CopyNo = ?", (doc_id, copy_number))
#             reserved_record = cursor.fetchone()

#             if borrowed_record:
#                 status = "Checked Out"
#             elif reserved_record:
#                 status = "Reserved"
#             else:
#                 status = "Available"

#             tree.insert("", "end", values=(copy_number, status))

#         conn.close()

#     search_button = Button(search_window, text="Search", command=search_copy_status)
#     search_button.pack()

#     tree.pack()

#     search_window.mainloop()

def search_document_copy():
    global search_window
    search_window = Toplevel(root2)
    search_window.title("Search Document Copy")

    Label(search_window, text="Document ID:").pack()
    doc_id_entry = Entry(search_window)
    doc_id_entry.pack()

    tree = ttk.Treeview(search_window)
    tree["columns"] = ("Copy Number", "Branch ID", "Status")
    tree.column("#0", width=0, stretch=NO)
    tree.column("Copy Number", anchor=W, width=100)
    tree.column("Branch ID", anchor=W, width=100)
    tree.column("Status", anchor=W, width=100)

    tree.heading("#0", text="", anchor=W)
    tree.heading("Copy Number", text="Copy Number", anchor=W)
    tree.heading("Branch ID", text="Branch ID", anchor=W)
    tree.heading("Status", text="Status", anchor=W)

    def search_copy_status():
        doc_id = doc_id_entry.get()

        # Clear the tree view
        for item in tree.get_children():
            tree.delete(item)

        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()

        # Fetch all copies of the document
        cursor.execute("SELECT CopyNo, BID FROM Copy WHERE DocID = ?", (doc_id,))
        copies = cursor.fetchall()

        for copy_number, branch_id in copies:
            # Check if the document copy is borrowed or reserved
            cursor.execute("SELECT * FROM Borrowing2 WHERE DocID = ? AND CopyNo = ?", (doc_id, copy_number))
            borrowed_record = cursor.fetchone()

            cursor.execute("SELECT * FROM Reservation2 WHERE DocID = ? AND CopyNo = ?", (doc_id, copy_number))
            reserved_record = cursor.fetchone()

            if borrowed_record:
                status = "Checked Out"
            elif reserved_record:
                status = "Reserved"
            else:
                status = "Available"

            tree.insert("", "end", values=(copy_number, branch_id, status))

        conn.close()

    search_button = Button(search_window, text="Search", command=search_copy_status)
    search_button.pack()

    tree.pack()

    search_window.mainloop()


def Document1():
    global root3
    root3 = Toplevel(root2)
    DLabel1 = Tk.Label(root3, text = "Add a document")
    DLabel1.pack()
    DButton1 = Tk.Button(root3, text = "Add a book", command= Book1)
    DButton2 = Tk.Button(root3, text = "Add a Journal Volume", command= JournalVolume1)
    DButton3 = Tk.Button(root3, text = "Add a Proceeding", command= Proceeding1)
    DButton1.pack()
    DButton2.pack()
    DButton3.pack()

def Book1():
    global root4
    root4 = Toplevel(root3)
    global ISBN
    global DocID
    DocID = StringVar()
    ISBN = StringVar()
    BLabel1 = Tk.Label(root4, text="Add a book")
    BLabel1.pack()
    BLabel2 = Tk.Label(root4, text="DocID")
    BEntry1 = Tk.Entry(root4, textvariable=DocID)
    BLabel3 = Tk.Label(root4, text="ISBN")
    BEntry2 = Tk.Entry(root4, textvariable=ISBN)
    BButton1 = Tk.Button(root4, text="Add", command=Book2)
    BLabel2.pack()
    BEntry1.pack()
    BLabel3.pack()
    BEntry2.pack()
    
    
    BButton1.pack()

def Book2():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DocID FROM Book WHERE DocID = ?", (DocID.get(),))
    existing_docid = cursor.fetchone()

    if existing_docid:
        messagebox.showerror("Adding Book Failed", "DocID already present")
    else:
        cursor.execute("INSERT INTO Book (DocID, ISBN) VALUES (?, ?)", (DocID.get(), ISBN.get()))
        messagebox.showinfo(title="Your book", message='Your book has been added',)
        root4.withdraw()
        root3.withdraw()

    conn.commit()
    conn.close()


def print_Book():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the book table
    cursor.execute("SELECT DocID, ISBN FROM Book")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print("DocID:", row[0], ", ISBN:", row[1])

    conn.close()

# Call the function to print the book values
print_Book()


def JournalVolume1():
    global root4
    root4 = Toplevel(root3)
    global DocID_JV
    global VolumeNo
    global IssueNo
    global Editor
    global GId
    global Scope
    DocID_JV = StringVar()
    VolumeNo = StringVar()
    IssueNo = StringVar()
    Editor = StringVar()
    GId = StringVar()
    Scope = StringVar()

    JVLabel1 = Tk.Label(root4, text="Add a Journal Volume")
    JVLabel1.pack()
    JVLabel2 = Tk.Label(root4, text="DocID")
    JVEntry1 = Tk.Entry(root4, textvariable=DocID_JV)
    JVLabel3 = Tk.Label(root4, text="Volume No")
    JVEntry2 = Tk.Entry(root4, textvariable=VolumeNo)
    JVLabel4 = Tk.Label(root4, text="Issue No")
    JVEntry3 = Tk.Entry(root4, textvariable=IssueNo)
    JVLabel5 = Tk.Label(root4, text="Editor")
    JVEntry4 = Tk.Entry(root4, textvariable=Editor)
    JVLabel6 = Tk.Label(root4, text="GId")
    JVEntry5 = Tk.Entry(root4, textvariable=GId)
    JVLabel7 = Tk.Label(root4, text="Scope")
    JVEntry6 = Tk.Entry(root4, textvariable=Scope)
    JVButton1 = Tk.Button(root4, text="Add", command=JournalVolume2)

    JVLabel2.pack()
    JVEntry1.pack()
    JVLabel3.pack()
    JVEntry2.pack()
    JVLabel4.pack()
    JVEntry3.pack()
    JVLabel5.pack()
    JVEntry4.pack()
    JVLabel6.pack()
    JVEntry5.pack()
    JVLabel7.pack()
    JVEntry6.pack()
    JVButton1.pack()

def JournalVolume2():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Check if DocID exists in the Book table
    cursor.execute("SELECT DocID FROM Book WHERE DocID = ?", (DocID_JV.get(),))
    existing_docid = cursor.fetchone()

    # Check if DocID exists in the JournalVolume table
    cursor.execute("SELECT DocID FROM JournalVolume WHERE DocID = ?", (DocID_JV.get(),))
    existing_docid_jv = cursor.fetchone()

    if existing_docid or existing_docid_jv:
        messagebox.showerror("Adding Journal Volume Failed", "DocID already present in Book or JournalVolume")
    else:
        cursor.execute("INSERT INTO JournalVolume (DocID, VolumeNo, IssueNo, Editor, GId, Scope) "
                       "VALUES (?, ?, ?, ?, ?, ?)", (DocID_JV.get(), VolumeNo.get(), IssueNo.get(),
                                                     Editor.get(), GId.get(), Scope.get()))
        messagebox.showinfo(title="Journal Volume Added", message='Journal Volume has been added')
        root4.withdraw()
        root3.withdraw()

    conn.commit()
    conn.close()


def print_JournalVolume():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the JournalVolume table
    cursor.execute("SELECT DocID, VolumeNo, IssueNo, Editor, GId, Scope FROM JournalVolume")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print("DocID:", row[0], ", VolumeNo:", row[1], ", IssueNo:", row[2], ", Editor:", row[3], ", GId:", row[4], ", Scope:", row[5])

    conn.close()

# Call the function to print the journal volume values
print_JournalVolume()


def Proceeding1():
    global root5
    root5 = Toplevel(root3)
    global DocID_P
    global CDate
    global CLocation
    global CChair
    DocID_P = StringVar()
    CDate = StringVar()
    CLocation = StringVar()
    CChair = StringVar()

    PLabel1 = Tk.Label(root5, text="Add a Proceeding")
    PLabel1.pack()
    PLabel2 = Tk.Label(root5, text="DocID")
    PEntry1 = Tk.Entry(root5, textvariable=DocID_P)
    PLabel3 = Tk.Label(root5, text="Date")
    PEntry2 = Tk.Entry(root5, textvariable=CDate)
    PLabel4 = Tk.Label(root5, text="Location")
    PEntry3 = Tk.Entry(root5, textvariable=CLocation)
    PLabel5 = Tk.Label(root5, text="Chair")
    PEntry4 = Tk.Entry(root5, textvariable=CChair)
    PButton1 = Tk.Button(root5, text="Add", command=Proceeding2)

    PLabel2.pack()
    PEntry1.pack()
    PLabel3.pack()
    PEntry2.pack()
    PLabel4.pack()
    PEntry3.pack()
    PLabel5.pack()
    PEntry4.pack()
    PButton1.pack()

def Proceeding2():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Check if DocID exists in the Book table
    cursor.execute("SELECT DocID FROM Book WHERE DocID = ?", (DocID_P.get(),))
    existing_docid = cursor.fetchone()

    # Check if DocID exists in the Proceeding table
    cursor.execute("SELECT DocID FROM Proceeding WHERE DocID = ?", (DocID_P.get(),))
    existing_docid_p = cursor.fetchone()

    if existing_docid or existing_docid_p:
        messagebox.showerror("Adding Proceeding Failed", "DocID already present in Book or Proceeding")
    else:
        cursor.execute("INSERT INTO Proceeding (DocID, CDate, CLocation, CChair) "
                       "VALUES (?, ?, ?, ?)", (DocID_P.get(), CDate.get(), CLocation.get(), CChair.get()))
        messagebox.showinfo(title="Proceeding Added", message='Proceeding has been added')
        root5.withdraw()
        root3.withdraw()

    conn.commit()
    conn.close()


def print_Proceeding():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the Proceeding table
    cursor.execute("SELECT DocID, CDate, CLocation, CChair FROM Proceeding")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print("DocID:", row[0], ", CDate:", row[1], ", CLocation:", row[2], ", CChair:", row[3])

    conn.close()

# Call the function to print the proceeding values
print_Proceeding()




def print_branch_info1():
    global root3
    root3 = Toplevel(root2)
    global BID 
    BID = StringVar()
    BrL1 = Tk.Label(root3, text = "Branch Info")
    BrL1.pack()
    BrL2 = Tk.Label(root3, text="Enter Branch ID")
    BrE2 = Tk.Entry(root3, textvariable=BID)
    BrB1 = Tk.Button(root3, text = "Print Branch Info", command=print_branch_info)
    BrL2.pack()
    BrE2.pack()
    BrB2 = Tk.Button(root3, text = "Add a branch", command= create_Branch)
    BrB1.pack()
    BrB2.pack()





def print_branch_info():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch branch info based on the given branch ID
    cursor.execute("SELECT LName, Location FROM Branch WHERE BID = ?", (BID.get(),))
    row = cursor.fetchone()

    if row:
        branch_info = {'Branch Name': row[0], 'Location': row[1]}
        show_tree_view(branch_info)
    else:
        messagebox.showerror("Invalid Branch ID", "Branch ID not found")

    conn.close()

def show_tree_view(branch_info):
    root4 = Toplevel(root3)
    root4.title('Branch Info')
    tree = ttk.Treeview(root4)
    tree["columns"] = ("1", "2")
    tree.heading("#0", text="Fields", anchor="w")
    tree.heading("1", text="Value", anchor="w")

    # Insert branch information into the tree view
    i = 0
    for key, value in branch_info.items():
        tree.insert("", i, text=key, values=(value,))
        i += 1

    tree.pack(expand=True, fill="both")

def create_Branch():
    global root3
    root3 = Toplevel(root2)
    global BranchID
    global BranchName
    global BranchLocation
    BranchID = StringVar()
    BranchName = StringVar()
    BranchLocation = StringVar()

    BrL1 = Tk.Label(root3, text="Create a Branch")
    BrL1.pack()
    BrL2 = Tk.Label(root3, text="Branch ID")
    BrE2 = Tk.Entry(root3, textvariable=BranchID)
    BrL3 = Tk.Label(root3, text="Branch Name")
    BrE3 = Tk.Entry(root3, textvariable=BranchName)
    BrL4 = Tk.Label(root3, text="Branch Location")
    BrE4 = Tk.Entry(root3, textvariable=BranchLocation)
    BrB1 = Tk.Button(root3, text="Create Branch", command=add_branch)
    BrL2.pack()
    BrE2.pack()
    BrL3.pack()
    BrE3.pack()
    BrL4.pack()
    BrE4.pack()
    BrB1.pack()

def add_branch():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Branch (BID, LName, Location) VALUES (?, ?, ?)",
                   (BranchID.get(), BranchName.get(), BranchLocation.get()))
    conn.commit()

    messagebox.showinfo("Branch Created", "Branch added successfully")

    conn.close()


def print_branches():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the Branch table
    cursor.execute("SELECT BID, LName, Location FROM Branch")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print("BID:", row[0], ", Branch Name:", row[1], ", Location:", row[2])

    conn.close()

# Call the function to print the branch values
print_branches()


def Create_copy():
    global root4
    root3 = Toplevel(root2)
    global CCopy_No
    global CDocID
    global CBID
    global CPosition
    CDocID = StringVar()
    CCopy_No = StringVar()
    CBID = StringVar()
    CPosition = StringVar()  # Corrected variable name
    CLabel1 = Tk.Label(root3, text="Create a copy")
    CLabel1.pack()
    CLabel2 = Tk.Label(root3, text="DocID")
    CEntry2 = Tk.Entry(root3, textvariable=CDocID)
    CLabel3 = Tk.Label(root3, text="Copy No")
    CEntry3 = Tk.Entry(root3, textvariable=CCopy_No)
    CLabel4 = Tk.Label(root3, text="BID")
    CEntry4 = Tk.Entry(root3, textvariable=CBID)
    CLabel5 = Tk.Label(root3, text="Position")
    CEntry5 = Tk.Entry(root3, textvariable=CPosition)

    CLabel2.pack()
    CEntry2.pack()
    CLabel3.pack()
    CEntry3.pack()
    CLabel4.pack()
    CEntry4.pack()
    CLabel5.pack()
    CEntry5.pack()

    CButton1 = Tk.Button(root3, text="Add Copy", command=add_copy)
    CButton1.pack()

def add_copy():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Check if DocID exists in the Book table
    cursor.execute("SELECT * FROM Book WHERE DocID = ?", (CDocID.get(),))
    row = cursor.fetchone()
    if not row:
        # Check if DocID exists in the JournalVolume table
        cursor.execute("SELECT * FROM JournalVolume WHERE DocID = ?", (CDocID.get(),))
        row = cursor.fetchone()
        if not row:
            # Check if DocID exists in the Proceeding table
            cursor.execute("SELECT * FROM Proceeding WHERE DocID = ?", (CDocID.get(),))
            row = cursor.fetchone()
            if not row:
                messagebox.showerror("Error", "DocID does not exist in the Book, JournalVolume, or Proceeding table")
                conn.close()
                return

    # Check if BID exists in the Branch table
    cursor.execute("SELECT * FROM Branch WHERE BID = ?", (CBID.get(),))
    row = cursor.fetchone()
    if not row:
        messagebox.showerror("Error", "BID does not exist in the Branch table")
        conn.close()
        return

    # Check if the combination of DocID, CopyNo, and BID already exists in the Copy table
    cursor.execute("SELECT * FROM Copy WHERE DocID = ? AND CopyNo = ? AND BID = ?",
                   (CDocID.get(), CCopy_No.get(), CBID.get()))
    row = cursor.fetchone()
    if row:
        messagebox.showerror("Error", "Combination of DocID, CopyNo, and BID already exists in the Copy table")
        conn.close()
        return

    # Add copy to Copy table if all conditions are met
    cursor.execute("INSERT INTO Copy (DocID, CopyNo, BID, Position) VALUES (?, ?, ?, ?)",
                   (CDocID.get(), CCopy_No.get(), CBID.get(), CPosition.get()))
    messagebox.showinfo("Success", "Copy added successfully")
    
    conn.commit()
    conn.close()

def print_copy():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the Copy table
    cursor.execute("SELECT * FROM Copy")
    rows = cursor.fetchall()
 
    # Print the rows
    for row in rows:
        print("DocID:", row[1], ", CopyNo:", row[2], ", BID:", row[0], ", Position:", row[3])

    conn.close()

# Call the function to print the copy values
print_copy()


def Create_doc_details():
    global root5
    root5 = Toplevel(root2)
    global DocID_doc_details
    DocID_doc_details = StringVar()
    DocID_label = Label(root5, text="Enter DocID:")
    DocID_entry = Entry(root5, textvariable=DocID_doc_details)
    DocID_label.pack()
    DocID_entry.pack()
    check_button = Button(root5, text="Check DocID", command=check_docid)
    check_button.pack()


def check_docid():
    docid = DocID_doc_details.get()
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()
    
    # Check if the DocID exists in the Document table
    cursor.execute("SELECT * FROM Document WHERE DocID = ?", (docid,))
    existing_doc = cursor.fetchone()
    
    conn.close()
    
    if existing_doc:
        messagebox.showerror("DocID Already Exists", "Details already created for this DocID")
    else:
        # Check if the DocID exists in any of the other tables
        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Book WHERE DocID = ?", (docid,))
        book_row = cursor.fetchone()
        cursor.execute("SELECT * FROM JournalVolume WHERE DocID = ?", (docid,))
        journal_row = cursor.fetchone()
        cursor.execute("SELECT * FROM Proceeding WHERE DocID = ?", (docid,))
        proceeding_row = cursor.fetchone()
        conn.close()
        
        if book_row or journal_row or proceeding_row:
            add_details_form(docid)
        else:
            messagebox.showerror("Invalid DocID", "DocID not found in any table")


def add_details_form(docid):
    global root6
    root6 = Toplevel(root5)
    Title_label = Label(root6, text="Title:")
    Title_entry = Entry(root6)
    Pdate_label = Label(root6, text="Pdate:")
    Pdate_entry = Entry(root6)
    Publisher_label = Label(root6, text="Publisher ID:")
    Publisher_entry = Entry(root6)
    save_button = Button(root6, text="Save Details", command=lambda: save_doc_details(docid, Title_entry.get(), Pdate_entry.get(), Publisher_entry.get()))
    Title_label.pack()
    Title_entry.pack()
    Pdate_label.pack()
    Pdate_entry.pack()
    Publisher_label.pack()
    Publisher_entry.pack()
    save_button.pack()

def save_doc_details(docid, title, pdate, publisher_id):
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()
    # Insert details into the document table
    cursor.execute("INSERT INTO Document (DocID, Title, Pdate, PublisherID) VALUES (?, ?, ?, ?)",
                   (docid, title, pdate, publisher_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Document details added successfully")
    root6.destroy()
    root5.destroy()


def print_Document():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the Document table
    cursor.execute("SELECT * FROM Document")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print("DocID:", row[0], ", Title:", row[1], ", Pdate:", row[2], ", PublisherID:", row[3])

    conn.close()

# Call the function to print the Document values
print_Document()

def Create_pub_details():
    global root6
    root6 = Toplevel(root2)
    global PublisherID_pub_details, PubName_pub_details, Address_pub_details
    PublisherID_pub_details = StringVar()
    PubName_pub_details = StringVar()
    Address_pub_details = StringVar()
    
    pl1 = Label(root6, text="Enter Publisher ID:")
    pe1 = Entry(root6, textvariable=PublisherID_pub_details)
    pl2 = Label(root6, text="Enter Publisher Name:")
    pe2 = Entry(root6, textvariable=PubName_pub_details)
    pl3 = Label(root6, text="Enter Address:")
    pe3 = Entry(root6, textvariable=Address_pub_details)
    pb1 = Button(root6, text="Save Details", command=save_pub_details)
    
    pl1.pack()
    pe1.pack()
    pl2.pack()
    pe2.pack()
    pl3.pack()
    pe3.pack()
    pb1.pack()

def save_pub_details():
    publisher_id = PublisherID_pub_details.get()
    pub_name = PubName_pub_details.get()
    address = Address_pub_details.get()
    
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Check if the PublisherID exists in the Publisher table
    cursor.execute("SELECT * FROM Publisher WHERE PublisherID = ?", (publisher_id,))
    existing_publisher = cursor.fetchone()
    if existing_publisher:
        messagebox.showerror("Publisher Details", "Details already entered")
    else:
        # Insert details into the Publisher table
        cursor.execute("INSERT INTO Publisher (PublisherID, PubName, Address) VALUES (?, ?, ?)", (publisher_id, pub_name, address))
        messagebox.showinfo("Publisher Details", "Details added successfully")
    
    conn.commit()
    conn.close()
    root6.destroy()

def print_publisher():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the Publisher table
    cursor.execute("SELECT PublisherID, PubName, Address FROM Publisher")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print("PublisherID:", row[0], ", PubName:", row[1], ", Address:", row[2])

    conn.close()

# Call the function to print the publisher values
print_publisher()





# emptying book table
# def empty_book_table():
#     try:
#         conn = sqlite3.connect('library3.db')
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM Book")
#         conn.commit()
#         conn.close()
#         print("Book table emptied successfully.")
#     except sqlite3.Error as e:
#         print(f"Error emptying Book table: {e}")

# # Call the function to empty the Book table
# empty_book_table()

# def delete_book_by_docid(docid):
#     conn = sqlite3.connect('library3.db')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM Book WHERE ISBN = ?", (docid,))
#     conn.commit()
#     conn.close()

# delete_book_by_docid("")

# def delete_books_with_empty_docid():
#     conn = sqlite3.connect('library3.db')
#     cursor = conn.cursor()
#     #cursor.execute("DELETE FROM Book WHERE TRIM(DocID) = ''")
#     cursor.execute("DELETE FROM Book WHERE TRIM(DocID) = ?", ('B1',))


#     conn.commit()
#     conn.close()

# delete_books_with_empty_docid()

# def print_Book():
#     conn = sqlite3.connect('library3.db')
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM Book")
#     rows = cursor.fetchall()

#     for row in rows:
#         print(row)

#     conn.close()


def Quit():
    root2.withdraw()
    root1.deiconify()



def reader_submenu():
    global root2
    root2= Toplevel(root1)
    reader_label1 = Tk.Label(root2, text ="Main Menu")
    reader_button1 = Tk.Button(root2, text = "Search Document", command = search_document)
    reader_button2 = Tk.Button(root2, text = "Checkout Document", command = document_checkout)
    reader_button3 = Tk.Button(root2, text = "Return Document", command = return_document)
    reader_button4 = Tk.Button(root2, text = "Reserve Document", command = document_reserve)
    reader_button5 = Tk.Button(root2, text = "Documents List", command = print_reserved_documents)
    reader_button6 = Tk.Button(root2, text = "Check by Publisher", command = print_documents_by_publisher)
    reader_button7 = Tk.Button(root2, text = "Fine", command = compute_fine)
    reader_button8 = Tk.Button(root2, text = "Quit")
    reader_label1.pack()
    reader_button1.pack()
    reader_button2.pack()
    reader_button3.pack()
    reader_button4.pack()
    reader_button5.pack()
    reader_button6.pack()
    reader_button7.pack()
    reader_button8.pack()
#*********************************************experiment********************************************************
from datetime import datetime

# def document_checkout():
#     global checkout_window
#     checkout_window = Toplevel(root2)
#     checkout_window.title("Document Checkout")
    
#     Label(checkout_window, text="Reader ID:").pack()
#     reader_id_entry = Entry(checkout_window)
#     reader_id_entry.pack()

#     Label(checkout_window, text="Document ID:").pack()
#     doc_id_entry = Entry(checkout_window)
#     doc_id_entry.pack()

#     Label(checkout_window, text="Branch Number:").pack()
#     branch_number_entry = Entry(checkout_window)
#     branch_number_entry.pack()

#     def select_copy_number():
#         # Get the entered values
#         reader_id = reader_id_entry.get()
#         doc_id = doc_id_entry.get()
#         branch_number = branch_number_entry.get()

#         # Check if the document exists
#         conn = sqlite3.connect('library3.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT CopyNo FROM Copy WHERE DocID = ? AND BID = ?", (doc_id, branch_number))
#         copies = cursor.fetchall()

#         if copies:
#             conn.close()

#             # Create a new window for copy selection
#             copy_selection_window = Toplevel(checkout_window)
#             copy_selection_window.title("Copy Selection")

#             Label(copy_selection_window, text="Select Copy Number:").pack()
#             copy_number_var = IntVar()
#             copy_number_var.set(copies[0][0])  # Default to the first copy
#             for copy in copies:
#                 Radiobutton(copy_selection_window, text=f"Copy Number: {copy[0]}", variable=copy_number_var, value=copy[0]).pack()

#             def checkout_document():
#                 selected_copy_number = copy_number_var.get()

#                 # Check if the copy is available
#                 conn = sqlite3.connect('library3.db')
#                 cursor = conn.cursor()

#                 cursor.execute("SELECT * FROM Borrowing2 WHERE DocID = ? AND CopyNo = ? AND BID = ?", (doc_id, selected_copy_number, branch_number))
#                 already_borrowed = cursor.fetchone()

#                 if not already_borrowed:
#                     # Insert a new row into the Borrowing2 table
#                     cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo) VALUES (?, ?, ?, ?)", (reader_id, branch_number, doc_id, selected_copy_number))

#                     conn.commit()
#                     conn.close()

#                     messagebox.showinfo("Document Checkout", "Document checked out successfully")
#                     checkout_window.destroy()
#                     copy_selection_window.destroy()
#                 else:
#                     conn.close()
#                     messagebox.showerror("Document Checkout", "Copy already borrowed")

#             checkout_button = Button(copy_selection_window, text="Checkout", command=checkout_document)
#             checkout_button.pack()

#         else:
#             conn.close()
#             messagebox.showerror("Document Checkout", "Document not found or no copies available")

#     select_copy_button = Button(checkout_window, text="Select Copy Number", command=select_copy_number)
#     select_copy_button.pack()

#     checkout_window.mainloop()
def document_checkout():
    global checkout_window
    checkout_window = Toplevel(root2)
    checkout_window.title("Document Checkout")
    
    Label(checkout_window, text="Reader ID:").pack()
    reader_id_entry = Entry(checkout_window)
    reader_id_entry.pack()

    Label(checkout_window, text="Document ID:").pack()
    doc_id_entry = Entry(checkout_window)
    doc_id_entry.pack()

    Label(checkout_window, text="Branch Number:").pack()
    branch_number_entry = Entry(checkout_window)
    branch_number_entry.pack()

    def select_copy_number():
        # Get the entered values
        reader_id = reader_id_entry.get()
        doc_id = doc_id_entry.get()
        branch_number = branch_number_entry.get()

        # Check if the document exists
        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()
        cursor.execute("SELECT CopyNo FROM Copy WHERE DocID = ? AND BID = ?", (doc_id, branch_number))
        copies = cursor.fetchall()

        if copies:
            conn.close()

            # Create a new window for copy selection
            copy_selection_window = Toplevel(checkout_window)
            copy_selection_window.title("Copy Selection")

            Label(copy_selection_window, text="Select Copy Number:").pack()
            copy_number_var = IntVar()
            copy_number_var.set(copies[0][0])  # Default to the first copy
            for copy in copies:
                Radiobutton(copy_selection_window, text=f"Copy Number: {copy[0]}", variable=copy_number_var, value=copy[0]).pack()

            def checkout_document():
                selected_copy_number = copy_number_var.get()

                # Check if the copy is available
                conn = sqlite3.connect('library3.db')
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM Borrowing2 WHERE DocID = ? AND CopyNo = ? AND BID = ?", (doc_id, selected_copy_number, branch_number))
                already_borrowed = cursor.fetchone()

                if not already_borrowed:
                    # Insert a new row into the Borrowing2 table
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute("INSERT INTO Borrowing2 (RID, BID, DocID, CopyNo, BDTime) VALUES (?, ?, ?, ?, ?)", (reader_id, branch_number, doc_id, selected_copy_number, current_time))

                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Document Checkout", "Document checked out successfully")
                    checkout_window.destroy()
                    copy_selection_window.destroy()
                else:
                    conn.close()
                    messagebox.showerror("Document Checkout", "Copy already borrowed")

            checkout_button = Button(copy_selection_window, text="Checkout", command=checkout_document)
            checkout_button.pack()

        else:
            conn.close()
            messagebox.showerror("Document Checkout", "Document not found or no copies available")

    select_copy_button = Button(checkout_window, text="Select Copy Number", command=select_copy_number)
    select_copy_button.pack()

    checkout_window.mainloop()

def return_document():
    global root7
    root7 = Toplevel(root2)
    global RID_return, CopyNo_return, DocID_return
    RID_return = StringVar()
    CopyNo_return = StringVar()
    DocID_return = StringVar()

    rdl1 = Label(root7, text="Enter Reader ID:")
    rde1 = Entry(root7, textvariable=RID_return)
    rdl2 = Label(root7, text="Enter Copy Number:")
    rde2 = Entry(root7, textvariable=CopyNo_return)
    rdl3 = Label(root7, text="Enter Document ID:")
    rde3 = Entry(root7, textvariable=DocID_return)
    rdb1 = Button(root7, text="Return Document", command=return_doc)

    rdl1.pack()
    rde1.pack()
    rdl2.pack()
    rde2.pack()
    rdl3.pack()
    rde3.pack()
    rdb1.pack()

def return_doc():
    rid = RID_return.get()
    copy_no = CopyNo_return.get()
    doc_id = DocID_return.get()

    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Check if the borrowing record exists
    cursor.execute("SELECT * FROM Borrowing2 WHERE RID = ? AND CopyNo = ? AND DocID = ?", (rid, copy_no, doc_id))
    borrowing2_record = cursor.fetchone()
    if not borrowing2_record:
        messagebox.showerror("Return Document", "Borrowing record not found")
        conn.close()
        return

    # Check if the return record already exists in Returning2 table
    cursor.execute("SELECT * FROM Returning2 WHERE RID = ? AND CopyNo = ? AND DocID = ? AND BID = ?", (rid, copy_no, doc_id, borrowing2_record[1]))
    returning2_record = cursor.fetchone()
    if returning2_record:
        # Update the existing record
        update_query = "UPDATE Returning2 SET RDateTime = ? WHERE RID = ? AND CopyNo = ? AND DocID = ? AND BID = ?"
        update_values = (datetime.now(), rid, copy_no, doc_id, borrowing2_record[1])
        cursor.execute(update_query, update_values)
    else:
        # Insert a new record into the Returning2 table
        return_query = "INSERT INTO Returning2 (RID, BID, DocID, CopyNo, RDateTime) VALUES (?, ?, ?, ?, ?)"
        return_values = (rid, borrowing2_record[1], doc_id, copy_no, datetime.now())
        cursor.execute(return_query, return_values)

    # Remove the row from Borrowing2 table
    delete_query = "DELETE FROM Borrowing2 WHERE RID = ? AND CopyNo = ? AND DocID = ?"
    delete_values = (rid, copy_no, doc_id)
    cursor.execute(delete_query, delete_values)

    conn.commit()
    conn.close()
    messagebox.showinfo("Return Document", "Document returned successfully")  # Notify user of successful return
    root7.destroy()

#######



def document_reserve():
    global reserve_window
    reserve_window = Toplevel(root2)
    reserve_window.title("Document Reserve")
    
    Label(reserve_window, text="Reader ID:").pack()
    reader_id_entry = Entry(reserve_window)
    reader_id_entry.pack()

    Label(reserve_window, text="Document ID:").pack()
    doc_id_entry = Entry(reserve_window)
    doc_id_entry.pack()

    Label(reserve_window, text="Copy Number:").pack()
    copy_number_entry = Entry(reserve_window)
    copy_number_entry.pack()

    Label(reserve_window, text="Branch Number:").pack()
    branch_number_entry = Entry(reserve_window)
    branch_number_entry.pack()

    def reserve_document():
        reader_id = reader_id_entry.get()
        doc_id = doc_id_entry.get()
        copy_number = copy_number_entry.get()
        branch_number = branch_number_entry.get()

        # Check if the copy is available
        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()

        # Check if the copy is available in the Copy table
        cursor.execute("SELECT * FROM Copy WHERE DocID = ? AND CopyNo = ? AND BID = ?", (doc_id, copy_number, branch_number))
        copy_available = cursor.fetchone()

        if copy_available:
            # Check if the copy is not already reserved
            cursor.execute("SELECT * FROM Reservation2 WHERE DocID = ? AND CopyNo = ? AND BID = ?", (doc_id, copy_number, branch_number))
            already_reserved = cursor.fetchone()

            if not already_reserved:
                # Insert a new row into the ReservatioN2 table
                cursor.execute("INSERT INTO Reservation2 (RID, BID, DocID, CopyNo, RTime) VALUES (?, ?, ?, ?, ?)",
                               (reader_id, branch_number, doc_id, copy_number, datetime.now()))

                conn.commit()
                conn.close()

                messagebox.showinfo("Document Reserve", "Document reserved successfully")
                reserve_window.destroy()
            else:
                conn.close()
                messagebox.showerror("Document Reserve", "Copy already reserved")
        else:
            conn.close()
            messagebox.showerror("Document Reserve", "Copy not available for reservation")

    reserve_button = Button(reserve_window, text="Reserve", command=reserve_document)
    reserve_button.pack()

    reserve_window.mainloop()


from datetime import datetime, timedelta

def compute_fine():
    global fine_window
    fine_window = Toplevel(root2)
    fine_window.title("Compute Fine")

    Label(fine_window, text="Reader ID:").pack()
    reader_id_entry = Entry(fine_window)
    reader_id_entry.pack()

    Label(fine_window, text="Document ID:").pack()
    doc_id_entry = Entry(fine_window)
    doc_id_entry.pack()

    Label(fine_window, text="Branch Number:").pack()
    branch_number_entry = Entry(fine_window)
    branch_number_entry.pack()

    def calculate_fine():
        reader_id = reader_id_entry.get()
        doc_id = doc_id_entry.get()
        branch_number = branch_number_entry.get()

        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()

        # Get the borrowing date for the document copy
        cursor.execute("SELECT BDTime FROM Borrowing2 WHERE RID = ? AND DocID = ? AND BID = ?", (reader_id, doc_id, branch_number))
        borrowing_time = cursor.fetchone()

        if borrowing_time:
            borrowing_datetime = datetime.strptime(borrowing_time[0], '%Y-%m-%d %H:%M:%S')
            current_datetime = datetime.now()
            difference = current_datetime - borrowing_datetime
            days = difference.days
            fine_amount = days * 0.50  # Assuming fine is 50 cents per day
            messagebox.showinfo("Fine Calculation", f"Fine for this document copy is: ${fine_amount}")
        else:
            messagebox.showerror("Fine Calculation", "Borrowing record not found")

        conn.close()

    calculate_button = Button(fine_window, text="Calculate Fine", command=calculate_fine)
    calculate_button.pack()

    fine_window.mainloop()

from tkinter import ttk

def print_reserved_documents():
    global print_reserved_window
    print_reserved_window = Toplevel(root2)
    print_reserved_window.title("Print Reserved Documents")

    Label(print_reserved_window, text="Reader ID:").pack()
    reader_id_entry = Entry(print_reserved_window)
    reader_id_entry.pack()

    tree = ttk.Treeview(print_reserved_window, columns=("DocID", "CopyNo", "Branch"), show="headings")
    tree.heading("DocID", text="DocID")
    tree.heading("CopyNo", text="CopyNo")
    tree.heading("Branch", text="Branch")
    tree.pack()

    def print_documents():
        reader_id = reader_id_entry.get()

        # Retrieve reserved documents for the reader
        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()

        cursor.execute("SELECT DocID, CopyNo, BID FROM Reservation2 WHERE RID = ?", (reader_id,))
        reserved_documents = cursor.fetchall()

        # Clear previous entries
        for row in tree.get_children():
            tree.delete(row)

        if reserved_documents:
            # Display reserved documents and their status
            for doc_id, copy_no, bid in reserved_documents:
                tree.insert("", "end", values=(doc_id, copy_no, bid))
        else:
            messagebox.showinfo("Reserved Documents", "No documents reserved by this reader")

        conn.close()

    print_button = Button(print_reserved_window, text="Print", command=print_documents)
    print_button.pack()

    print_reserved_window.mainloop()

def print_documents_by_publisher():
    global print_publisher_window
    print_publisher_window = Toplevel(root2)
    print_publisher_window.title("Print Documents by Publisher")

    Label(print_publisher_window, text="Publisher ID:").pack()
    publisher_id_entry = Entry(print_publisher_window)
    publisher_id_entry.pack()

    tree = ttk.Treeview(print_publisher_window, columns=("DocID", "Title"), show="headings")
    tree.heading("DocID", text="DocID")
    tree.heading("Title", text="Title")
    tree.pack()

    def print_documents():
        publisher_id = publisher_id_entry.get()

        # Retrieve documents published by the publisher
        conn = sqlite3.connect('library3.db')
        cursor = conn.cursor()

        cursor.execute("SELECT DocID, Title FROM Document WHERE PublisherID = ?", (publisher_id,))
        published_documents = cursor.fetchall()

        # Clear previous entries
        for row in tree.get_children():
            tree.delete(row)

        if published_documents:
            # Display document ID and titles
            for doc_id, title in published_documents:
                tree.insert("", "end", values=(doc_id, title))
        else:
            messagebox.showinfo("Published Documents", "No documents published by this publisher")

        conn.close()

    print_button = Button(print_publisher_window, text="Print", command=print_documents)
    print_button.pack()

    print_publisher_window.mainloop()

#*********************************************experiment********************************************************

def search_document():
    global root3
    root3 = Toplevel(root2)
    sdl1 = Tk.Label(root3, text = "Search Document By")
    sdl1.pack()
    sdb1 = Tk.Button(root3, text = "DOCID", command = search_by_docid)
    sdb1.pack()
    sdb2 = Tk.Button(root3, text = "Title", command = search_by_title)
    sdb2.pack()
    sdb3 = Tk.Button(root3, text = "Publisher Name", command = search_by_pubname)
    sdb3.pack()

def search_by_docid():
    global root4
    root4 = Toplevel(root3)
    global DocID_search
    DocID_search = StringVar()
    sdl2 = Tk.Label(root4, text="Enter DocID")
    sde1 = Tk.Entry(root4, textvariable=DocID_search)
    sdb2 = Tk.Button(root4, text="Search", command=search_docid_details)
    
    sdl2.pack()
    sde1.pack()
    sdb2.pack()

def search_docid_details():
    docid = DocID_search.get()
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Search in Book table
    cursor.execute("SELECT * FROM Book WHERE DocID = ?", (docid,))
    book_row = cursor.fetchone()

    # Search in JournalVolume table
    cursor.execute("SELECT * FROM JournalVolume WHERE DocID = ?", (docid,))
    journal_row = cursor.fetchone()

    # Search in Proceeding table
    cursor.execute("SELECT * FROM Proceeding WHERE DocID = ?", (docid,))
    proceeding_row = cursor.fetchone()

    conn.close()

    if book_row:
        show_document_details("Book", book_row)
    elif journal_row:
        show_document_details("JournalVolume", journal_row)
    elif proceeding_row:
        show_document_details("Proceeding", proceeding_row)
    else:
        messagebox.showerror("Document Not Found", "DocID not found in any table")

def show_document_details(doc_type, row):
    global root5
    root5 = Toplevel(root4)
    sdl3 = Tk.Label(root5, text=f"{doc_type} Details")
    sdl3.pack()
    
    tree = ttk.Treeview(root5)
    tree["columns"] = ("1", "2")
    tree.heading("#0", text="Attribute")
    tree.heading("1", text="Value")
    
    if doc_type == "Book":
        tree.insert("", 1, text="ISBN", values=(row[1],))
        tree.insert("", 0, text="DocID", values=(row[0],))
        
    elif doc_type == "JournalVolume":
        tree.insert("", 0, text="DocID", values=(row[0],))
        tree.insert("", 1, text="VolumeNo", values=(row[1],))
        tree.insert("", 2, text="IssueNo", values=(row[2],))
        tree.insert("", 3, text="Editor", values=(row[3],))
        tree.insert("", 4, text="GId", values=(row[4],))
        tree.insert("", 5, text="Scope", values=(row[5],))
    elif doc_type == "Proceeding":
        tree.insert("", 0, text="DocID", values=(row[0],))
        tree.insert("", 1, text="CDate", values=(row[1],))
        tree.insert("", 2, text="CLocation", values=(row[2],))
        tree.insert("", 3, text="CChair", values=(row[3],))
    
    tree.pack()


def search_by_title():
    global root4
    root4 = Toplevel(root3)
    global Title_search
    Title_search = StringVar()
    sdl2 = Tk.Label(root4, text="Enter Title")
    sde1 = Tk.Entry(root4, textvariable=Title_search)
    sdb2 = Tk.Button(root4, text="Search", command=search_title_details)
    
    sdl2.pack()
    sde1.pack()
    sdb2.pack()

def search_title_details():
    title = Title_search.get()
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Search for DocID using Title from Document table
    cursor.execute("SELECT DocID FROM Document WHERE Title = ?", (title,))
    docid_row = cursor.fetchone()
    if not docid_row:
        messagebox.showerror("Title Not Found", "Title not found in Document table")
        conn.close()
        return

    docid = docid_row[0]

    # Search in Book table
    cursor.execute("SELECT * FROM Book WHERE DocID = ?", (docid,))
    book_row = cursor.fetchone()

    # Search in JournalVolume table
    cursor.execute("SELECT * FROM JournalVolume WHERE DocID = ?", (docid,))
    journal_row = cursor.fetchone()

    # Search in Proceeding table
    cursor.execute("SELECT * FROM Proceeding WHERE DocID = ?", (docid,))
    proceeding_row = cursor.fetchone()

    conn.close()

    if book_row:
        show_document_details("Book", book_row)
    elif journal_row:
        show_document_details("JournalVolume", journal_row)
    elif proceeding_row:
        show_document_details("Proceeding", proceeding_row)
    else:
        messagebox.showerror("Document Not Found", "DocID not found in any table")

def show_document_details(doc_type, row):
    global root5
    root5 = Toplevel(root4)
    sdl3 = Tk.Label(root5, text=f"{doc_type} Details")
    sdl3.pack()
    
    tree = ttk.Treeview(root5)
    tree["columns"] = ("1", "2")
    tree.heading("#0", text="Attribute")
    tree.heading("1", text="Value")
    
    if doc_type == "Book":
        tree.insert("", 0, text="DocID", values=(row[0],))
        tree.insert("", 1, text="ISBN", values=(row[1],))
    elif doc_type == "JournalVolume":
        tree.insert("", 0, text="DocID", values=(row[0],))
        tree.insert("", 1, text="VolumeNo", values=(row[1],))
        tree.insert("", 2, text="IssueNo", values=(row[2],))
        tree.insert("", 3, text="Editor", values=(row[3],))
        tree.insert("", 4, text="GId", values=(row[4],))
        tree.insert("", 5, text="Scope", values=(row[5],))
    elif doc_type == "Proceeding":
        tree.insert("", 0, text="DocID", values=(row[0],))
        tree.insert("", 1, text="CDate", values=(row[1],))
        tree.insert("", 2, text="CLocation", values=(row[2],))
        tree.insert("", 3, text="CChair", values=(row[3],))
    
    tree.pack()

def search_by_pubname():
    global root4
    root4 = Toplevel(root3)
    global PubName_search
    PubName_search = StringVar()
    sdl2 = Tk.Label(root4, text="Enter Publisher Name")
    sde1 = Tk.Entry(root4, textvariable=PubName_search)
    sdb2 = Tk.Button(root4, text="Search", command=search_pubname_details)

    sdl2.pack()
    sde1.pack()
    sdb2.pack()

def search_pubname_details():
    pubname = PubName_search.get()
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Search for PublisherID based on Publisher Name
    cursor.execute("SELECT PublisherID FROM Publisher WHERE PubName = ?", (pubname,))
    publisher_id_row = cursor.fetchone()
    if not publisher_id_row:
        messagebox.showerror("Publisher Not Found", "Publisher Name not found in Publisher table")
        return

    publisher_id = publisher_id_row[0]

    # Search in Document table for DocID based on PublisherID
    cursor.execute("SELECT DocID FROM Document WHERE PublisherID = ?", (publisher_id,))
    docid_row = cursor.fetchone()
    if not docid_row:
        messagebox.showerror("Document Not Found", "No documents found for the given Publisher")
        return

    docid = docid_row[0]

    # Search in Book table
    cursor.execute("SELECT * FROM Book WHERE DocID = ?", (docid,))
    book_row = cursor.fetchone()

    # Search in JournalVolume table
    cursor.execute("SELECT * FROM JournalVolume WHERE DocID = ?", (docid,))
    journal_row = cursor.fetchone()

    # Search in Proceeding table
    cursor.execute("SELECT * FROM Proceeding WHERE DocID = ?", (docid,))
    proceeding_row = cursor.fetchone()

    conn.close()

    if book_row:
        show_document_details("Book", book_row)
    elif journal_row:
        show_document_details("JournalVolume", journal_row)
    elif proceeding_row:
        show_document_details("Proceeding", proceeding_row)
    else:
        messagebox.showerror("Document Not Found", "DocID not found in any table")

def show_document_details(doc_type, row):
    global root5
    root5 = Toplevel(root4)
    sdl3 = Tk.Label(root5, text=f"{doc_type} Details")
    sdl3.pack()

    tree = ttk.Treeview(root5)
    tree["columns"] = ("1", "2")
    tree.heading("#0", text="Attribute")
    tree.heading("1", text="Value")

    if doc_type == "Book":
        tree.insert("", 0, text="DocID", values=(row[0],))
        tree.insert("", 1, text="ISBN", values=(row[1],))
    elif doc_type == "JournalVolume":
        tree.insert("", 0, text="DocID", values=(row[0],))
        tree.insert("", 1, text="VolumeNo", values=(row[1],))
        tree.insert("", 2, text="IssueNo", values=(row[2],))
        tree.insert("", 3, text="Editor", values=(row[3],))
        tree.insert("", 4, text="GId", values=(row[4],))
        tree.insert("", 5, text="Scope", values=(row[5],))
    elif doc_type == "Proceeding":
        tree.insert("", 0, text="DocID", values=(row[0],))
        tree.insert("", 1, text="CDate", values=(row[1],))
        tree.insert("", 2, text="CLocation", values=(row[2],))
        tree.insert("", 3, text="CChair", values=(row[3],))

    tree.pack()


def print_admin_logins():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the logins_admin table
    cursor.execute("SELECT * FROM logins_admin")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    conn.close()

# Call the function to print the logins_admin values
print_admin_logins()

def print_readers_logins():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the logins_admin table
    cursor.execute("SELECT * FROM logins_readers")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    conn.close()

# Call the function to print the logins_admin values
print_readers_logins()

def print_borrowing2():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the Borrowing2 table
    cursor.execute("SELECT * FROM Borrowing2")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    conn.close()

# Call the function to print the Borrowing2 values
print_borrowing2()

def print_returning2():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the Returning2 table
    cursor.execute("SELECT * FROM Returning2")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    conn.close()

# Call the function to print the Returning2 values
print_returning2()

def print_Reservation2():
    conn = sqlite3.connect('library3.db')
    cursor = conn.cursor()

    # Fetch all rows from the Reservation2 table
    cursor.execute("SELECT RID, BID, DocID, CopyNo, RTime FROM Reservation2")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print("RID:", row[0], ", BID:", row[1], ", DocID:", row[2], ", CopyNo:", row[3], ", RTIME:", row[4])

    conn.close()

# Call the function to print the Reservation2 values
print_Reservation2()


def checkadmin():
    global root2
    root2 = Toplevel(root1)
    global Admin_Code
    Admin_Code=StringVar()
    Label(root2,text="Type Admin Code").grid(row=1,column=3)
    Entry(root2,textvariable=Admin_Code).grid(row=1,column=5)
   
    Button(root2,text='ENTER',command=lambda:{create_admin()}).grid(row=6,column=5)
    Button(root2,text='Close',command=close1).grid(row=7,column=5)

def register_admin():
    sql=sqlite3.connect('library3.db')
    conn=sql.cursor()
    conn.execute('select SSN from logins_admin')
    records=conn.fetchall()
    print(records)
    c=0
    for i in range(len(records)):
        if SSN.get()==records[i][0]:
            c=c+1
    if c!=0:
        messagebox.showinfo(title="Invalid SSN", message='your SSN number is invalid',)   
    else:
        conn.execute("insert into logins_admin values(:Fullname,:SSN,:orgphonenumber,:loginid,:password)",
            {
                'Fullname':fullname.get(),
                'SSN':SSN.get(),
                'orgphonenumber':PhoneNum.get(),
                'loginid':loginid.get(),
                'password':password.get()
            })
        messagebox.showinfo(title="your account", message='your account has been created',)
        root2.withdraw()
    sql.commit()

def register_reader():
    sql=sqlite3.connect('library3.db')
    con=sql.cursor()
    con.execute('select ID from logins_readers')
    records=con.fetchall()
    print(records)
    c=0
    for i in range(len(records)):
        if ID.get()==records[i][0]:
            c=c+1
    if c!=0:
        messagebox.showinfo(title="Invalid ID", message='your ID number is already taken',)   
    else:
        con.execute("insert into logins_readers values(:Fullname,:ID_num,:Phonenumber)",
            {
                'Fullname':fullname.get(),
                'ID_num':ID.get(),
                'Phonenumber':rphoneNum.get(),
            })
        messagebox.showinfo(title="your account", message='your account has been created',)
        root2.withdraw()
    sql.commit()

def create_reader():
    global root3
    root3=Toplevel(root2)
    root3.geometry('400x500')
    global fullname
    global ID
    global rphoneNum
    fullname=StringVar()
    ID=StringVar()
    rphoneNum=StringVar()
    Label(root3,text="FullName").grid(row=1,column=3)
    Entry(root3,textvariable=fullname).grid(row=1,column=5)
    Label(root3,text="ID_num").grid(row=2,column=3)
    Entry(root3,textvariable=ID).grid(row=2,column=5)
    Label(root3,text="PhoneNumber").grid(row=3,column=3)
    Entry(root3,textvariable=rphoneNum).grid(row=3,column=5)
    Button(root3,text='Register',command=lambda:{register_reader()}).grid(row=6,column=5)
    #Button(root3,text='Close',command=close1?).grid(row=7,column=5)

def create_admin():
    print(r)
    if Admin_Code.get()==r[0][0]:
        global root3
        root3 = Toplevel(root2)
        global fullname
        global loginid
        global password
        global SSN
        global PhoneNum
        fullname=StringVar()
        loginid=StringVar()
        password=StringVar()
        SSN=StringVar()
        PhoneNum=StringVar()

        Label11 = Tk.Label(root3, text = "You're authorized to create admin logins")
        Label12 = Tk.Label(root3, text = "Enter Details")
        Label13 = Tk.Label(root3, text = "Full Name")
        Entry13 = Tk.Entry(root3, textvariable= fullname)
        Label16 = Tk.Label(root3,text="SSN")
        Entry16 = Tk.Entry(root3,textvariable=SSN)
        Label17 = Tk.Label(root3,text="PhoneNumber")
        Entry17 = Tk.Entry(root3,textvariable=PhoneNum)
        Label14 = Tk.Label(root3, text = "Login ID")
        Entry14 = Tk.Entry(root3, textvariable= loginid)
        Label15 = Tk.Label(root3, text = "Password")
        Entry15 = Tk.Entry(root3, textvariable= password)
        Button11= Tk.Button(root3, text = "Create", command = register_admin)
        # Button12= Tk.Button(root3,text='Close',command=close1).grid(row=7,column=5)
        Label11.pack()
        Label12.pack()
        Label13.pack()
        Entry13.pack()
        Label16.pack()
        Entry16.pack()
        Label17.pack()
        Entry17.pack()
        Label14.pack() 
        Entry14.pack() 
        Label15.pack() 
        Entry15.pack() 
        Button11.pack()
        # Button12.pack()
        root2.withdraw()
    else:
        messagebox.showinfo(title="Invalid Code", message='your code is invalid',)   
        

label1 = Tk.Label(root, text = "Library Login Page")
label2 = Tk.Label(root, text = "Are you a")
button1 = Tk.Button(root, text = "Adminstrator", command = adminstrator_page)
button2 = Tk.Button(root, text = "Reader", command = reader_page)
label1.pack()
label2.pack()
button1.pack()
button2.pack()



def close1():
    root2.withdraw()

#create table
#should we mention primary key, data types?
cursor.execute(''' CREATE TABLE IF NOT EXISTS Document (DOCId, Title , PDate , PublisherID)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Publisher (PublisherID, PubName, Address)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Book (ISBN,DocID)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Authors (PID, DocID)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Journal_Issue (DocID,IssueNo,Scope)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Journal_Volume (DocID,VolumeNo,Editor)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS GEdits (PID,DocID,IssueNo)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Proceedings (DocID,CDate,CLocation,CEditor)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Chairs (PID,DocID)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Person (PID,PName)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Copy (BID,DocID,CopyNo,Position)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Branch (BID,LName,Location)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Reserves (RID,DocID,ReservationNo,CopyNo,BID)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Reservation (ResNo,DTime)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Borrows (RID,BID,DocID,BorNo,CopyNo)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Borrowing1 (RDTime,BDTime,BorNo)''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS Reader (RID,RType,RName,RAddress,PhoneNo)''')

# cursor.execute('''INSERT INTO Document (DOCId, Title, PDate, PublisherID) VALUES (2, 'Another Title', '2024-04-26', 2)''')

conn.commit() #commit changes


# cursor.execute('SELECT * FROM admin2')
# rows = cursor.fetchall()
# for row in admin2:
#     print(row)



conn.close()
#close connection

root.mainloop()