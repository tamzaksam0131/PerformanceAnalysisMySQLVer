import pymysql
from prettytable.prettytable import from_db_cursor

def sql_print_index():
    con = pymysql.connect (host='10.203.1.84',
                            port = 31730, 
                            user ='root', 
                            password ='passwd',
                            database ='test') # create connection object and database file

    cur = con.cursor() # create a cursor for connection object

    cur.execute('SELECT * From Index_Table')
        
    x = from_db_cursor(cur)
    print (x)

    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
    sql_print_index()