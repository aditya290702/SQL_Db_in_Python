import sqlite3
import pandas as pd
conn = sqlite3.connect('brain.db')
curs = conn.cursor()

df_data=pd.read_csv('brain_size.csv', sep=';', na_values='.')
df_data.to_sql('brain_size.csv',conn, if_exists='replace', index=False)

curs.execute('SELECT * from brain_size ORDER BY FSIQ')
rows = curs.fetchall()
print(rows)

conn.commit()
curs.close()
conn.close()