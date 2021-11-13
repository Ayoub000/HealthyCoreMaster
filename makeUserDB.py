import sqlite3, hashlib

con = sqlite3.connect('hcore.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE users
               (id integer primary key autoincrement, username text, password text)''')

# Insert a row of data
passwordA = hashlib.sha3_512(''.encode()).hexdigest()
passwordY = hashlib.sha3_512(''.encode()).hexdigest()

cur.execute("INSERT INTO users (username,password) VALUES ('', '"+ passwordA + "')")
cur.execute("INSERT INTO users (username,password) VALUES ('', '"+ passwordY + "')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()