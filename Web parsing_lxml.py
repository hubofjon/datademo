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

    
    
