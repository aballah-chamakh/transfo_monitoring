import datetime
import sqlite3

conn = sqlite3.connect('test_db.db')
worker = conn.cursor()
worker.execute(""" CREATE TABLE IF NOT EXISTS pression (
time text,
any text,
ano text
) 

""")
worker.execute(""" CREATE TABLE IF NOT EXISTS gaz (
time text
) 

""")
conn.commit()

currentDate = str(datetime.datetime.now())
table = 'pression'
#worker.execute("INSERT INTO "+table+" VALUES (:time,:any,:ano)",{'time':currentDate,'any':'any','ano':'anoo'})
#conn.commit()
worker.execute("UPDATE pression SET time =(:time),ano =(:ano) WHERE any='any' ",{'time':'10H','ano':'anooaazzz'})
worker.execute("SELECT * FROM pression")
data = worker.fetchall()
conn.commit()
for i,item in enumerate(data):
    print(item)

