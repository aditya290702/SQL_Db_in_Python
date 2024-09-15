import sqlite3

conn = sqlite3.connect('FRIENDS.db')
curs = conn.cursor()
curs.execute('''
                CREATE TABLE NAME
                (
                    ID VARCHAR(20),
                    NAME VARCHAR(20)
                )
            ''')

curs.execute('''
                CREATE TABLE FOOD
                (
                    ID VARCHAR(20),
                    NAME VARCHAR(20)
                )
            ''')
print("lets gets you logged in")
ID = input()
NAME = input()

curs.execute('INSERT INTO NAME VALUES("01","JOEY")')
curs.execute('INSERT INTO NAME VALUES("02","CHANDLER")')
curs.execute('INSERT INTO NAME VALUES(?,?)', (ID,NAME))


curs.execute('INSERT INTO FOOD VALUES("01","PIZZA")')
curs.execute('INSERT INTO FOOD VALUES("02","TOMATOES")')


print("DONE")

rows = curs.fetchall()
print(rows)

conn.commit()
curs.close()
conn.close()
