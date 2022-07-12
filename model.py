class library:
    def __init__(self, _id=0, Bname='',Bstatus=None, Bissuedate=""):
        self.bookid=_id
        self.bookname= Bname
        self.bookstatus= Bstatus
        self.bookissuedate= Bissuedate




    def __repr__(self):
        return f'library[{self.bookid}, {self.bookname}, {self.bookstatus} , {self.bookissuedate}]'

#Create table Query
'''
create table Library (bookid int primary key auto_increment,
                       bookname varchar(50),
                       bookstatus varchar(100),
                       
                       bookissuedate varchar(50)
                       );
                       808104624684 MAVI ka no.

'''
