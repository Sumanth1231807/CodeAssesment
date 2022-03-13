import sqlite3 as sql
from prettytable import PrettyTable

connection = sql.connect("Employe.db")

listOfemp = connection.execute("select name from sqlite_master where type='table' AND name='employee'").fetchall()

if listOfemp != []:
    print("Table is already Created.")
else:
    connection.execute('''create table employee(

                              empCode integer,
                              name text,
                              phone integer,
                              email text,
                              designation text,
                              salary integer,
                              companyname text );''')
    print("Table Created Successfully.")