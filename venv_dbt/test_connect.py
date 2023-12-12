import pyodbc
import sys
import os

con = pyodbc.connect('DSN=snowflake_trial_account;UID=SM;PWD=To2!JestBardzoTrudneHasloDoSniezynki')

con.setencoding(encoding='utf-8')
con.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
cursor=con.cursor()
cursor.execute("SELECT * from REGION")

while True:
        row=cursor.fetchone()                                                                                                                                               
        if not row:                                                                                                                                                         
                break                                                                                                                                                       
        print(row)