import cx_Oracle,os

un=os.environ.get('APP_USER')
pw=os.environ.get('APP_PASSWORD')
cs=os.environ.get('APP_CONNECTIONSTRING')
TNS=os.environ.get('TNS_ADMIN')
print('TNS Names is :',TNS)
#(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.ap-hyderabad-1.oraclecloud.com))(connect_data=(service_name=g18f56a071bf9cc_malandb_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)(ssl_server_cert_dn="CN=adb.ap-hyderabad-1.oraclecloud.com, OU=Oracle ADB HYDERABAD, O=Oracle Corporation, L=Redwood City, ST=California, C=US")))
print('1 un is =',un,'pw is =',pw,'cs is =',cs)
connection = cx_Oracle.connect(un, pw, cs)

cursor = connection.cursor()

# Create a table

cursor.execute("""begin
                     execute immediate 'drop table pytab';
                     exception when others then if sqlcode <> -942 then raise; end if;
                  end;""")
cursor.execute("create table pytab (id number, data varchar2(20),name  varchar2(20))")

# Insert some rows

rows = [ (1, "First",'Anand' ),
         (2, "Second",'Bala' ),
         (3, "Third" ,'Chari'),
         (4, "Fourth" ,'Thiru'),
         (5, "Fifth" , 'Pope'),
         (6, "Sixth" ,'Hari'),
         (7, "Seventh" ,'Otto') ]

cursor.executemany("insert into pytab(id, data,name) values (:1, :2,:3)", rows)
cursor.execute("insert into REG(NAME) values ('u8ig_hrf')")
connection.commit()  # uncomment to make data persistent

# Now query the rows back

for row in cursor.execute('select * from pytab'):
    print(row,row[0],row[2])