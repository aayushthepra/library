import pymysql
from datetime import date
pymysql.install_as_MySQLdb()
import MySQLdb


con=MySQLdb.connect(host="localhost",user="YOUR_DB_USERNAME",passwd="YOUR_DB_PASSWORD",database="library")
def addbook():
    code=input("Enter Book Code:")
    selectQuery = "select * from book where code='%s'"
    c = con.cursor()
    rows = c.execute(selectQuery % code)
    insertQuery="insert into book (name, subject, code, count) values (%s,%s,%s, %s)"
    updateQuery = "update book set count=%s where id=%s"
    if rows==0:
        bookName = input("Enter Book Name:")
        subject = input("Enter Subject:")
        insertQueryData = (bookName, subject, code, 1)
        c.execute(insertQuery, insertQueryData)
    else:
        book = c.fetchone()
        bookID = book[0]
        bookCount = book[-1]
        updateQueryData = (bookCount+1, bookID)
        c.execute(updateQuery,updateQueryData)
    con.commit()
    print("Added book Successfully")
    main()
def showbooks():
    selectAllquery = "select * from book"
    c = con.cursor()
    c.execute(selectAllquery)
    rows = c.fetchall()
    for i in rows:
        print(i)
    main()
def adduser():
    firstName=input("Enter First Name:")
    lastName=input("Enter Last Name:")
    identityNumber=input("Enter ID Number:")
    data=(firstName,lastName,identityNumber)
    sql="INSERT INTO user (firstName,lastName,identityNumber) VALUES (%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    main()

def issueb():
    code = input("Enter Book Code:")
    getBookQuery = "SELECT * from book where code='%s'"
    c = con.cursor()
    isbookTypeAvailable = c.execute(getBookQuery % code)
    # if book is available the proceed otherwise redirect to main menu
    if isbookTypeAvailable>0:
        pass
    else:
        print("books not available")
        main()
    book = c.fetchone();
    print(book);
    # Now check the count, if count>0 then only proceed otherwise redirect user to main menu
    if book[-1]>0:
        pass
    else:
        print("All books with entered code are already issued")
        main()

    id=input("Enter Your identity number:")
    today=date.today();
    issuedBookQuery = "insert into issuedbooks (userID,issueDate,bookCode) VALUES (%s,%s,%s)"
    data=(id, today, code)
    c=con.cursor()
    c.execute(issuedBookQuery,data)
    con.commit()
    print("Book Issued To:", id)
    bookup(code,-1)
def submitb():
    id=input("Enter your Reg No:")
    code=input("Enter Book Code:")
    today=date.today();
    selectQuery = "select id from issuedBooks where bookCode=%s and userID=%s and submitDate is null"
    data = (code, id)
    c = con.cursor()
    selectQueryRows = c.execute(selectQuery, data)
    if selectQueryRows == 0:
        print("book could not be submmited, either 'book Code' or 'Registration number' is incorrect")
        main()
    issuedBook = c.fetchone();
    issuedbookID = issuedBook[0]
    updateQuery="update issuedBooks set submitDate=%s where id=%s"
    updatedata=(today,issuedbookID)
    c.execute(updateQuery,updatedata)
    con.commit()
    print("Book Submitted From:", id)
    bookup(code,1)
def bookup(code,u):
    query1="select * from book where code='%s'"
    c=con.cursor()
    c.execute(query1 % code)
    book=c.fetchone()
    newBookCount=book[-1]+u
    print(newBookCount);
    query2="update book set count=%s where code=%s"
    data=(newBookCount, code)
    c.execute(query2,data)
    con.commit()
    main()
def main():
    print("""                                   
                                             LIBRARY MANAGER
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.ADD USER
    5.SHOW BOOKS
    6.EXIT
    """)
    choice=input("Enter Task No:")
    if(choice=='1'):
        addbook()
    if (choice=='2'):
        issueb()
    if (choice=='3'):
        submitb()
    if (choice=='4'):
        adduser()
    if (choice=='5'):
        showbooks()
    if (choice=='6'):
        print('Bye! Have a nice day.')
        exit()
    else:
        print("Wrong Choice.....")
        main()
def pswd():
    ps=input("Enter Password:")
    if ps=="SET_YOUR_PASSWORD_CAN_BE_ANYTHING":
        main()
    else:
        print("Wrong Password")
        pswd()
pswd()


