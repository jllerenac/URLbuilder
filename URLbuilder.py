import requests
requests.packages.urllib3.disable_warnings()
from pprint import pprint
import argparse
parser = argparse.ArgumentParser(description='Program to build a list of IPs / URL based on a network address or file')
parser.add_argument("[IP/Network Address|File]", help="Provide the requested address or file")
parser.add_argument("--noslash", help="Specify this parameter if you don't want slash at the end of URL",action="store_false")
parser.add_argument("--noredirect", help="Specify this parameter if you don't want to add redirect URLs to the list",action="store_false")
args = parser.parse_args()

URL = "http://localhost/"

r = requests.get(URL,verify=False,allow_redirects = False,timeout=5)
#f = urllib.request.urlopen(URL)
print(r.status_code)
if r.status_code == '200':
    pprint("[+]"+r.headers["Location"])
print(args.noslash)
if args.noslash:
    print('verdad')
