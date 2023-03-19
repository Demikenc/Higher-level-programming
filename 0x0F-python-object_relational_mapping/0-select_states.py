#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    # take arguments from command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=mysql_user,
                         passwd=mysql_password,
                         db=db_name)

    # prepare a cursor object
    cursor = db.cursor()

    # execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # disconnect from server
    db.close()

