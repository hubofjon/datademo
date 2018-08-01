# -*- coding: utf-8 -*-
"""
"""
import pandas as pd
import numpy as np
import cx_Oracle as CO
#ip = 'XX.XX.X.XXX'
#port = YYYY
##SID = 'DW'
#dsn_tns = cx_Oracle.makedsn(ip, port, SID)

#connection = cx_Oracle.connect('id', 'password', dsn_tns)


dev_str='server/port/servicename'
dev_id='id'
dev_pswd='pswd'


dsn_tns=CO.makedsn('server', 1535, 'servicename')
con_dev=CO.connect('id','pswd', dsn_tns)

query="SELECT * FROM ord where rownum<10 order by coa_to_date desc"
q#uery="SELECT * FROM ord_fx where rownum<10"
df = pd.read_sql(query, con=con_dev)

#dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'XE')
#print dsn_tns
#(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521)))
#(CONNECT_DATA=(SID=XE)))
