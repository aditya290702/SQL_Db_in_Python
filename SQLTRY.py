import sqlite3

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('''
                CREATE TABLE employees
                (
                    emp_id INT PRIMARY_KEY,
                    emp_name VARCHAR(20),
                    emp_email VARCHAR(20)
                )
            ''')
curs.execute('INSERT INTO employees VALUES(1, "Arum", "arun@gmail.com")')
curs.execute('INSERT INTO employees VALUES(2, "Adi", "Adi@gmail.com")')
curs.execute('INSERT INTO employees VALUES(3, "Joey", "Blublablablubleblbe@gmail.com")')
curs.execute('INSERT INTO employees VALUES(4, "Pheebs", "Pheebs@gmail.com")')

curs.execute('''
                UPDATE employees SET emp_email = "arunnew@gmail.com" WHERE emp_id = 1
            ''')

curs.execute('SELECT * FROM employees')
rows = curs.fetchall()
print(rows)

conn.commit()
curs.close()
conn.close()


