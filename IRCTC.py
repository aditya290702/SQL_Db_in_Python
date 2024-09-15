import sqlite3

conn = sqlite3.connect('IRCTC.db')
curs = conn.cursor()
curs.execute('''
                CREATE TABLE USER
                (
                    ID VARCHAR(20),
                    NAME VARCHAR(20),
                    EMAIL VARCHAR(20),
                    PHONENO INT(10),
                    PWD VARCHAR(20)
                )             
            ''')
print("Let's get you logged in . . . ")
print("Please Input your ID")
Id = input()
print("Please Input your Name")
name = input()
print("Please Input your EMAIL")
Email = input()
print("Please Input your PhoneNo")
Phone = input()
print("Please Input your Pwd")
pwd = input()




curs.execute('INSERT INTO USER VALUES(  "JOEYYYYY", "JOEY TRIBBIAI","JOEY@Gmail.com","7972682173","****")')
curs.execute('INSERT INTO USER VALUES(  "ROSSSS", "ROSS GELLER","Dinosaours@Gmail.com","8237111104","****")')
curs.execute('INSERT INTO USER VALUES(  "BINGGGG", "CHANDLER BING","BingBing@Gmail.com","8237029702","****")')
curs.execute('INSERT INTO USER VALUES ( ?, ?, ?, ?, ?)', (Id, name, Email, Phone, pwd))

print("YOu have logged in succesfully , WELCOME TO IRCTC !!!!")
curs.execute('''
                CREATE TABLE TRAIN
                (
                    Train_ID VARCHAR(20),
                    Train_NAME VARCHAR(20),
                    Starting_FROM VARCHAR(20),
                    Derparture_Station_ID VARCHAR(20),
                    Reaching_Till VARCHAR(20),
                    Arrival_Station_ID VARCHAR(20)
                )
            ''')
curs.execute('INSERT INTO TRAIN VALUES("KEXP", "KOYNA EXPRESS","PUNE","PNQ","MUMBAI","BOM")')
curs.execute('INSERT INTO TRAIN VALUES("SHEXP", "SHATABDI EXPRESS","BENGALURU","BLR","PUNE","PNQ")')
curs.execute('INSERT INTO TRAIN VALUES("RJEXP", "RAJDHANI EXPRESS","VELLORE","VLR","MUMBAI","BOM")')
curs.execute('''
                CREATE TABLE BOOKING
                (
                    Boking_ID VARCHAR(20),
                    User_ID VARCHAR(20),
                    Travel_Date VARCHAR(20)
                )
            ''')
curs.execute('INSERT INTO BOOKING VALUES("BK001", "JOEYYYY","1DEC")')
curs.execute('INSERT INTO BOOKING VALUES("BK002", "ROSSSS","2DEC")')
curs.execute('INSERT INTO BOOKING VALUES("BK003", "BINGGGG","3DEC")')

curs.execute('SELECT * FROM USER')
curs.execute('SELECT * FROM TRAIN')
curs.execute('SELECT * FROM BOOKING')
rows = curs.fetchall()
print(rows)

conn.commit()
curs.close()
conn.close()

