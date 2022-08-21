from pickle import TRUE
import requests
requests.packages.urllib3.disable_warnings()
import argparse
import ipaddress
import uuid

#Defining the positional and optional arguments
parser = argparse.ArgumentParser(description='Program to build a list of IPs / URL based on a network address or file')
parser.add_argument("input", help="[IP/Network Address|File]")
parser.add_argument("--output", help="Your resulting file",action="store_false")
parser.add_argument("--noslash", help="Specify this parameter if you don't want slash at the end of URL",action="store_false")
parser.add_argument("--noredirect", help="Specify this parameter if you don't want to add redirect URLs to the list",action="store_false")
args = parser.parse_args()

#Defining vars to give color to some of the text when printing
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'
FAIL = '\033[91m'
f = ''
if args.output:
    fileName = args.output
else:
    fileName = str(uuid.uuid4())

def inputValidation(input):
    try:
        fp = open(input, 'r')
    except FileNotFoundError:
        print(f'{FAIL} [-] {ENDC}' + "Wrong file or file path, will check if is valid host")
        return 'S'
    f = open(fileName,"a")
    for host in fp:
       inputRequest(host.rstrip())
    f.close() 
    quit()

def inputRequest(host):
    slash = ''
    if args.noslash:
        slash = '/'

    URL = 'http://'+ host + slash
    print(URL)
    try:
        r = requests.get(URL,verify=False,allow_redirects = False,timeout=5)
        print(r.status_code)
        if r.status_code == '200':             
            f.write(URL)
        if r.status_code == '302' and args.noredirect:
            f.write(URL)
            h = r.headers["Location"]
            inputRequest(h.rstrip())
            print("[+]"+r.headers["Location"])

    except requests.exceptions.ConnectionError as e:  #To avoid to long error trace, just will respond with no conn msg 
    # the FAIL var give red color to text and ENDC will give you back your terminal color
        print(f'{FAIL} [-] {ENDC}' + 'No connection has been established for host/IP ' + host + '\n')

inputType = inputValidation(args.input)
try:
    ipaddress.ip_network(args.input,strict=True)
    print(args.input)
    for host in ipaddress.IPv4Network('192.168.100.1/26'):
       print(host)
       # inputRequest(str(host.rstrip()))
except ValueError:
    print(f'{FAIL} [-] {ENDC}' + 'Not valid IP or network address, will check if is valid domain')
    inputRequest(args.input.rstrip())
