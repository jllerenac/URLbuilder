import requests
requests.packages.urllib3.disable_warnings()
from pprint import pprint
import argparse
parser = argparse.ArgumentParser(description='A test program.')
args = parser.parse_args()

URL = "http://localhost/"

r = requests.get(URL,verify=False,allow_redirects = False,timeout=5)
#f = urllib.request.urlopen(URL)
print(r.status_code)
if r.status_code == '200':
    pprint("[+]"+r.headers["Location"])


