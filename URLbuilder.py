import requests
requests.packages.urllib3.disable_warnings()
from pprint import pprint
URL = "https://localhost/"

r = requests.get(URL,verify=False,allow_redirects = False)
#f = urllib.request.urlopen(URL)
print(r.status_code)
pprint(r.headers["Location"])



