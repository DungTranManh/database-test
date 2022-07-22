import sqlite3
import json
import time
from tracemalloc import start
import psutil

ram1 = psutil.virtual_memory()[3]
f = open('convertcsv1M.json')
# start_time = time.time()
data = json.load(f)

# database
connection = sqlite3.connect('data1.db')
cursor = connection.cursor()
# cursor.execute("create table name_table (id INTEGER PRIMARY KEY AUTOINCREMENT ,name text, age INTERGER, gender text, city text)")

# for i in range (len(data)):
#     tmp = data[i]
#     cursor.execute('insert into name_table (name,age,gender,city) VALUES (?,?,?,?)',(tmp.get('first'),tmp.get('age'),tmp.get('gender'),tmp.get('city')))

#   update phần tử có giá trị đặc biệt (giá trị duy nhất có trong bảng)
# cursor.execute("UPDATE name_table SET name = ? WHERE id = 750345", ("Minh",))
# cursor.execute("UPDATE name_table SET name = ? WHERE id = 1000000", ("Linh",))

start_time = time.time()
#testing
#   Phan tu dau database
# cursor.execute("SELECT * FROM name_table WHERE name = 'Mary'")
# print(cursor.fetchone())

#   Phan tu nam giua database
# cursor.execute("SELECT * FROM name_table WHERE name = 'Dung'")
# print(cursor.fetchall())

#   Phan tu nam cuoi database
cursor.execute("SELECT * FROM name_table WHERE id = 1000000")
print(cursor.fetchall())
print("---------Time: %s seconds---------" % (time.time() - start_time))
# connection.commit()
connection.close()

# hien thi time run code

#hien thi cpu usage
# print(psutil.cpu_percent(time.time() - start_time))
#hien thi ram usage
# print((psutil.virtual_memory()[3]-ram1)/1e6)
