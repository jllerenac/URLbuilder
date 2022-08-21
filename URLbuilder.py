import requests
requests.packages.urllib3.disable_warnings()
from pprint import pprint
URL = "http://localhost/"

r = requests.get(URL,verify=False,allow_redirects = False)
#f = urllib.request.urlopen(URL)
print(r.status_code)
pprint(r.headers["Location"])


