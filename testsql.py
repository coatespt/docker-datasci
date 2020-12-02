
import mysql.connector
from mysql.connector import Error

## This is a simple select with no variables, but variables are easy to put into a call.
selectStmt = 'select id, path from books2'

try:
# You get a connection
    connection = mysql.connector.connect(host='localhost', database='gutenberg', user='petercoates', password='aardvark1')
    if connection.is_connected():
        # I'm not doing anything with this--just an example
        db_Info = connection.get_server_info()

        # A cursor can pull back records in batches and tracks where you're at.
        cursor = connection.cursor()

        # Once you execute the cursor has access to the result set.
        cursor.execute(selectStmt)
        records = cursor.fetchall()

        ## Normal python to iterate the data set. For me, it's just to columns from one table
        ##
        for record in records:
            id=record[0]
            otherstuff=record[1]
            print('insde the records loop: {}'.format(record))
    else:
        ## You were unable to connect, but it failed correctly. Take appropriate action, e.g., warning, etc.
        pass
except Error as e:
    print()
        ## There was a blowup when attempting to connect. Take approprate action, e.g. warning, etc.
finally:
    ## This will run before you return no matter what, whether you had an exception or not.
    ##
    if (connection.is_connected()):
        cursor.close()
        connection.close()
