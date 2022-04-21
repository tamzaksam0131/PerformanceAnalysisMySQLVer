import pymysql
from prettytable.prettytable import from_db_cursor
import yaml
from prettytable import PrettyTable

def sql_test():
    
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    con = pymysql.connect (host='10.203.1.84',
                            port = 31730, 
                            user ='root', 
                            password ='passwd',
                            database ='test') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    for i in range(len(a['table view'])):

        sql_sentence = 'SELECT' + ' ' +  a['wanted data view'] + ' ' + 'From' + ' ' + a['table view'][i]

        cur.execute(sql_sentence)
        
        x = from_db_cursor(cur)

        print (a['table view'][i])
        print (x)

    cur.close()
    con.commit()
    con.close()


if __name__ == '__main__':
    sql_test()