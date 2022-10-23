import cx_Oracle

# This host name is for OCI-m7 on Ravichs
host_name = "10.1.62.10"
# This host name is for local machine
#host_name = 'localhost'
#For m7 on Ravichs
#cx_Oracle.init_oracle_client(lib_dir="/opt/oracle/instantclient_21_4")
#connection = cx_Oracle.connect(user="admin", password="Guttappan123", dsn="db202112131853_low")

print('Inside DB Services')


def get_db_conn():
   
   #For m7 on Ravichs
    
    cnx = cx_Oracle.connect(user="admin", password="Krishna12345", dsn="malandb_low")

   
   # cnx = mysql.connector.connect(user="raghuiy", passwd="@Krishna10",
#                              host=host_name,
 #                                 database="malan",
  #                                auth_plugin="mysql_native_password")

    return (cnx)


def write_to_choice_db(reg_id, color_choice):
    cnx = get_db_conn()
    cur = cnx.cursor()
    print('Reg is=', reg_id, 'Choice is:',color_choice)
    sql = "insert into  choice(regid,color)  values ( :reg_id, :color_choice)"
    #print('&&&&&&&&&&    Rec value is: ', choice_rec,'&&&&&&&&&&', type(choice_rec))
    cur.execute(sql, [reg_id,color_choice])
    #sql = "insert into  choice(regid,color)  values ( 25, 'Pink')"
    #cur.execute(sql)
    print('Last row inserted into CHOICE was : ', cur.lastrowid)
    cnx.commit()
    return cur.lastrowid


def write_to_reg_db(visitor_name):
    try:
        cnx = get_db_conn()
        cur = cnx.cursor()
        created_id=cur.var(cx_Oracle.NUMBER)
        sql = "insert into REG (NAME) values (:rec ) returning regid into :created_id"
        rec = [visitor_name,created_id]
        print('Rec val=', rec, 'and is of type: ', type(rec))
        cur.execute(sql, rec)
        
        cnx.commit()
        #What comes back is a list. You get the first element of that list, convert into a integer
        registrant_id=int((created_id.getvalue()[0]))
        #print('~~~~~~~Newly added id:',int((created_id.getvalue()[0])),'~~~~~~' )
        return (registrant_id)
    except:
        print('Caught some error and in Exception Block:',cur[sql])
    

def read_from_db(tbl_name, pWhr_Clause=""):
    try:
        cnx = get_db_conn()
        print('Table name=', tbl_name, ' Where clause= ', pWhr_Clause)
        fetch_cursor = cnx.cursor()
        print('This is the recd whr clause ' + pWhr_Clause)
        if (pWhr_Clause == "INNER_JOIN"):
            sql = 'select REG.regid,REG.name , color ' \
                  'from choice ' \
                  'inner join REG on choice.regid=REG.regid ' \
                  'order by REG.name'
        else:
            sql = "select * from " + tbl_name
            print('The sql was= ', sql)
        fetch_cursor.execute(sql)
        result = fetch_cursor.fetchall()
    #for row in result:
     #   print('Here is the printed row: ', row)
    except:
        print('Caught some error')
    finally:
        cnx.close()
        return result


print('Today is Fri 7-Jan-2022.This is DB services')
