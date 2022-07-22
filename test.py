import sqlite3
import json
import time
from tracemalloc import start

f = open('convertcsv.json')
start_time = time.time()
data = json.load(f)

# database
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
# cursor.execute("create table name_table (id INTEGER PRIMARY KEY AUTOINCREMENT ,name text)")

# for i in range (len(data)):
#     tmp = data[i]
#     cursor.execute('insert into name_table (name) VALUES (?)',(tmp.get('name'),))

#   update phần tử có giá trị đặc biệt (giá trị duy nhất có trong bảng)
# cursor.execute("UPDATE name_table SET name = ? WHERE id = 50000", ("Dung",)) => done
# cursor.execute("UPDATE name_table SET name = ? WHERE id = 100000", ("Thanh",)) => done

#testing
#   Phan tu dau database
# cursor.execute("SELECT * FROM name_table WHERE name = 'Mary'")
# print(cursor.fetchone())

#   Phan tu nam giua database
cursor.execute("SELECT * FROM name_table WHERE name = 'Dung'")
print(cursor.fetchall())
#   Phan tu nam cuoi database
# cursor.execute("SELECT * FROM name_table WHERE name = 'Mary'")
# print(cursor.fetchone())

# connection.commit()
connection.close()

# hien thi time run code
print("---------Time: %s seconds---------" % (time.time() - start_time))


