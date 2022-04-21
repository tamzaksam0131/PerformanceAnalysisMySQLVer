import pymysql

def sql_test():
    
    # a_yaml_file = open('sql_config.yml')
    # a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    con = pymysql.connect (host='10.203.1.84',
                            port = 31730, 
                            user ='root', 
                            password ='passwd',
                            database ='test') # create connection object and database file

    cursor = con.cursor()
 
    sql_sentence = '''SELECT h.Text_Table_Name, h.DRBD_Type, h.IOPS \
    FROM a_123_drbd AS h \
    JOIN Index_table AS in ON in.Text_Table_Name =a _123_drbd.table_name' \
    WHERE Readwrite_type = "randwrite"\
    AND Number_of_Job = "8" \
    AND IOdepth = "8" \
    AND blocksize = "1M" '''

    print(sql_sentence)
    
    cursor.execute(sql_sentence)

    for x in cursor:
        print(x)
 
    # 关闭数据库连接
    con.close()

if __name__ == '__main__':
    sql_test()