from flask import Flask, request #import main Flask class and request object

import mysql.connector

from mysql.connector import Error

## TODO get rid of hard coded credentials, etc.

def output(records):
    linehead='<H2>'
    linetail='</H2>'
    output = '<H1>Your Data</H1>\n'
    output = output + '<table style="width:100%">\n'
    for record in records:
        ln = '<TR>\n\t<TD>' + str(record[0]) + '</TD>\n\t <TD>' + record[1] + '</TD></TR>'
        output = output + ln
    output = output + '</table">'
    return output


def calldb(s):
    ## This is a simple select with no variables, but variables are easy to put into a call.
    selectStmt = 'select id, path from books2 limit 10'
    retlist = []
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
            ## for record in records:
            ##     id=record[0]
            ##     otherstuff=record[1]
            ##     print('insde the records loop: {} record size = {}'.format(record, len(record)))
            ##     strn = '<H1>' + str(id) + ' ' + str(otherstuff) + '</H1>'
            ##     retlist.append(strn)
            html_out = output(records)
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
    return html_out



app = Flask(__name__)

@app.route('/')

def hello_world():
    output = calldb('')
    return str(output)

@app.route('/query-one-arg')
def query_example():
    print('In the query_example method.')
    language = request.args.get('language') #if key doesn't exist, returns None


    return '''<h1>The language is: {}</h1>'''.format(language)

@app.route('/query-two-args')
def query_two_example():
    print('In the query_example method.')
    language = request.args.get('language') #if key doesn't exist, returns None
    framework = request.args.get('framework') #if key doesn't exist, returns None
    return '''<h1>The language is: {}</h1><h1>The framework is: {}</h1>'''.format(language,framework)

# @app.route('/fetchdata', methods=['GET'])
# def print_square():
#     recieved_value = int(request.get_json(force=True))
#     return_value = received_value + 3
#     print('Flask GET fetch received request {} and responds with {}'.format(recieved_value))
#     return str(return_value)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
