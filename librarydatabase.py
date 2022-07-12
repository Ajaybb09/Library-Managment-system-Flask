from logging import exception
import pymysql as pm
from model import library
con = pm.connect(host='localhost',user='root',
                    passwd='',db='library')
print('Connected with Database Successfully ..')
cursor = con.cursor()

 
def savebook(book):
    try:
        sqlQuery = "insert into library (bookname,bookstatus,date) values(%s,%s,%s)"
        cursor.execute(sqlQuery, (book.bookname , book.bookstatus, book.bookissuedate))
        con.commit()
    except Exception as e:
            print("error", e)

def getbooklist():
    booklist = []
    try:
        sqlQuery = 'select * from library'
        cursor.execute(sqlQuery)
        rows = cursor.fetchall() 
        con.commit()
        for row in rows:
            # create the object each of table library.
            book = library(row[0],row[1],row[2],row[3])
            booklist.append(book)
        else:
            return booklist  
    except Exception as e:
        print("-"*5,'Error',"-"*5)
        print(e)

def  deletebook(_id):
    try:
        sqlQuery = 'delete from library where bookid = %s'
        cursor.execute(sqlQuery,(_id))
        con.commit()
    except Exception as e:
        print("-"*5,'Error',"-"*5)
        print(e)

def updatebookstatus(_id,book):
    try:
        sqlQuery = 'update library set bookstatus= %s , bookname= %s , date=%s where bookid = %s'
        cursor.execute(sqlQuery,(book.bookstatus, book.bookname,book.bookissuedate ,_id))
        con.commit()
    except Exception as e:
        print("-"*5,'Error',"-"*5)
        print(e)


def getbookbyId(_id):
    try:
        sqlQuery = 'select * from library where bookid=%s'
        cursor.execute(sqlQuery,(_id))
        row = cursor.fetchone()
        book = library(row[0],row[1],row[2], row[3])
        con.commit
        return book
    except exception as e:
        print("error", e)



def searchbook(query):
    booklist = []
    try:
        sqlQuery = 'select * from library where bookid=%s or bookname=%s'
        cursor.execute(sqlQuery,(query,query))
        rows = cursor.fetchall() 
        con.commit()
        for row in rows:
            # create the object each of table library.
            book = library(row[0],row[1],row[2],row[3])
            booklist.append(book)
        else:
            return booklist  
    except Exception as e:
        print("-"*5,'Error',"-"*5)
        print(e)




def closeconnection():
    con.close()     
    print("database connection is closed")  