from model import library
from flask import Flask, render_template, redirect, request, url_for
import librarydatabase as db

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Booklist')
def Booklist():
    booklist= db.getbooklist()
    return render_template('Booklist.html',booklist=booklist)

@app.route('/AddBook')
def AddBook():
    book = library()
    return render_template('AddBook.html', book=book ,action='Add')

@app.route('/deletebook/<int:bookid>')
def deletebook(bookid):
    db.deletebook(bookid)
    return redirect('/Booklist') 


@app.route('/editbook/<int:bookid>')
def editbook(bookid):
    book = db.getbookbyId(bookid)
    return render_template('AddBook.html', book=book, action='Edit')

@app.route("/updatebook", methods=['POST'])
def updatebook():

    _id = request.form['bookid']   
    Bname = request.form['bookname']
    Bstatus = request.form['bookstatus']
    Bissuedate= request.form['bookissuedate']
    book = library(_id,Bname,Bstatus,Bissuedate=Bissuedate)

    db.updatebookstatus(_id, book)
    return redirect (url_for('Booklist'))
    

@app.route("/savebook",methods=['POST'] )
def savebook(): 
    Bname = request.form['bookname']
    Bstatus = request.form['bookstatus']
    Bissuedate= request.form['bookissuedate']
    book = library(Bname=Bname,Bstatus=Bstatus,Bissuedate=Bissuedate)

    db.savebook(book)
    return redirect (url_for('Booklist'))


@app.route("/searchbookbyIdorname", methods=['GET'] )
def searchbookbyIdorname():
    query = request.args.get('Searchbook')
    booklist=db.searchbook(query)
    #booklist= db.getbooklist()
    #booklist= list(filter(lambda book: str(book.bookid)==query or book.bookname.startswith(query), booklist) )
    return render_template('Booklist.html',booklist=booklist)
    

#select * from library where bookid=%s or bookname=%s

if __name__ == '__main__':
    #app.run()
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(debug=True)


    
