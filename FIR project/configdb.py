import sqlite3

class ConnectionDatabase:
# code below is for the creating a database name “complaintDb.db” and for the table name “complainTable”
    def __init__(self):
        self._db = sqlite3.connect('complaintDB.db')
        self._db.row_factory = sqlite3.Row
        self._db.execute('create table if not exists complaintTable(ID integer primary key autoincrement, FirstName varchar(255), LastName varchar(255), Address Text, Gender varchar(255), Comment text)')
        self._db.commit()
# Below function is to insert the values into the cells we created in the table.
# Using insert command
    def Add(self, firstname, lastname, address, gender, Comment):
        self._db.execute('insert into complaintTable (FirstName, LastName, Address, Gender, Comment) values (?,?,?,?,?)', (firstname, lastname, address, gender, Comment))
        self._db.commit()
        return 'Your complaint has been submitted.'
# Below function displays all the content in the Table.
    def ListRequest(self):
        cursor = self._db.execute('select * from complaintTable')
        return cursor