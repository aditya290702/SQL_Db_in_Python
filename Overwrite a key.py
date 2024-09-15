import sqlite3

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('''
                UPDATE employees SET emp_email = "arunnew@gmail.com" WHERE emp_id = 1)
            ''')
conn.commit()
curs.close()
conn.close()