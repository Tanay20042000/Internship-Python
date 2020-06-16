import sqlite3

class Contact:

    def __init__(self,db1,name,call):
        self.name = name
        self.call = call
        self.db1 = db1
        pass
    
    def add(db1,name,call):
        db1.execute('insert into phone values(?,?)', (name, call))
        pass
    
    def delete(db1,name):
        db1.execute('delete from phone where name = (?)', (name))
        pass
    
    def view(db1):
        db1.execute('select * from phone')
        cts = db1.fetchall()
        return cts
    
    def edit1(db1,name,call):
        db1.execute('update phone set name = (?) where ph_no = (?)', (name, call))
        pass
    
    def edit2(db1,name,call):
        db1.execute('update phone set ph_no = (?) where name = (?)', (call, name))
        pass
    
    def search1(db1,names):
        db1.execute("SELECT * FROM phone WHERE name = ?",(names,))
        row1 = db1.fetchall()
        for i in row1:
            print(i)
        pass
    
    def search2(db1,calls):
        db1.execute("SELECT * FROM phone WHERE ph_no = ?",(calls,))
        row1 = db1.fetchall()
        for i in row1:
            print(i)
        pass