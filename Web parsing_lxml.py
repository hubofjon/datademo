#Author: JonQLi
#!python
import os, argparse
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from lxml import html

ma=wd+ss+pa
uid='qli1'
payload={
        'Username':uid,
        'Password':ma}

def get_url():
    url_howto="http://appsupport.sc/team_pages"

   
#    res=requests.get(url_rlnx)
    session_requests=requests.session()
#    result=session_requests.get(url_howto)
    result=session_requests.post(url_howto, data=payload,
        headers=dict(referer=url_howto))
#    tree=html.fromstring(result.text)
    
#    res=requests.get(url_howto, auth=HTTPDigestAuth(uid,ma))
    print(result.status_code)
    
    if result.status_code==requests.codes.ok:
        rtext=result.text
        return rtext
    else:
        print("err")
    return result
parser=argparse.ArgumentParser()
parser.add_argument("-ht", "--howto", help="search how do")
parser.add_argument("-pc", "--pc", help="search pc")
parser.add_argument("-s","--string", nargs="*", help="string to search")
args=parser.parse_args()
#if args.howto:
#    DIR="C:\\Users\\dev"
#    for str in args.string:
#        Filelist=os.listdir(DIR)
#        matched_filenames=[x for x in Filelist if str in x]
#      print ("string: %s found in :"%str, matched_filenames)
#if arg.pc:
#    DIR="C:\\Users\\BNS_tool"

#structured in class    
import requests
import pandas as pd
from bs4 import BeautifulSoup

class HTMLTableParser:
    def parse_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
#        return [(table,\
#                #(table['id'],
#                 self.parse_html_table(table))\
        for table in soup.find_all('table'):  
                    print(table)

    def parse_html_table(self, table):
        n_columns = 0
        n_rows=0
        column_names = []

        # Find number of rows and columns
        # we also find the column titles if we can
        if table['id']!="opt_unusal_volume":
            pass
        else:
            for row in table.find_all('tr'):
               
                # Determine the number of rows in the table
                td_tags = row.find_all('td')
                if len(td_tags) > 0:
                    n_rows+=1
                    if n_columns == 0:
                        # Set the number of columns for our table
                        n_columns = len(td_tags)
                print(len(td_tags))    
                # Handle column names if we find them
                th_tags = row.find_all('th') 
                if len(th_tags) > 0 and len(column_names) == 0:
                    for th in th_tags:
                        if th.get_text()=='string':
                            pass
                        else:
     #                       print(th.get_text())
                            column_names.append(th.get_text())
    
            # Safeguard on Column Titles
    #        if len(column_names) > 0 and len(column_names) != n_columns:
    #             print(n_columns, len(column_names))           
    #             raise Exception("Column titles do not match the number of columns")
    
            columns = column_names if len(column_names) > 0 else range(0,n_columns)
            df = pd.DataFrame(columns = columns,
                              index= range(0,n_rows))
            row_marker = 0
            for row in table.find_all('tr'):
                column_marker = 0
                columns = row.find_all('td')
                for column in columns:
                    df.iat[row_marker,column_marker] = column.get_text()
                    column_marker += 1
                if len(columns) > 0:
                    row_marker += 1
                    
            # Convert to float if possible
            for col in df:
                try:
                    df[col] = df[col].astype(float)
                except ValueError:
                    pass
            
        return df
        
