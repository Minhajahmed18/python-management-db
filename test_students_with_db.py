import pyodbc



'''
conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=USER-PC;"
    "Database=python_db;"
    "Trusted_Connection=yes;"
)

cursor=conn.cursor()
cursor.execute('insert into courses1(course_id,course_name,course_fees,course_duration_month,std_id,fees_paid_by_student) values(?,?,?,?,?,?)',(
    '1',"Accounting","4000","3","1","2000"
))
cursor.commit()



'''


name='Minhaj'
print(str(name))
