from fileinput import filename
from pickle import TRUE
import requests
requests.packages.urllib3.disable_warnings()
import argparse
from netaddr import *
import uuid

#Defining the positional and optional arguments
parser = argparse.ArgumentParser(description='Program to build a list of IPs / URL based on a network address or file')
parser.add_argument("input", help="[IP/Network Address|File]")
parser.add_argument("--output", help="Your resulting file",type=str)
parser.add_argument("--noslash", help="Specify this parameter if you don't want slash at the end of URL",action="store_false")
parser.add_argument("--noredirect", help="Specify this parameter if you don't want to add redirect URLs to the list",action="store_false")
args = parser.parse_args()

#Defining vars to give color to some of the text when printing
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'
FAIL = '\033[91m'
redirects = [301,302,303,307,308]
slash = ''
protocol = 'http://'

# No slash works only with original requests, redirects will include regardless of this value
if args.noslash: 
    slash = '/'
if args.output:
# IF FILE EXISTS CONTENT WILL !!! OVERWRITE !!! YOUR FILE
# Removed the append option to avoid messy and duplicated hosts, I might introduce this option later
    fileName = args.output  
else:
    fileName = str(uuid.uuid4())  + ".txt" # I am giving a random filename with default txt extension 
f = open(fileName,"w")
def inputValidation(input):
    try:
        fp = open(input, 'r')
    except FileNotFoundError:
        print(f'{WARNING} [-] {ENDC}' + "Wrong file or file path, will check if is valid host")
        return 'S'
    for host in fp:
       inputRequest(protocol+host.rstrip()+slash)
    f.close() 
    quit()

def inputRequest(URL):
    try:
        r = requests.get(URL,verify=False,allow_redirects = False,timeout=3)
        if r.status_code == 200:       
            print(f'{OKGREEN} [+] HTTP ' + str(r.status_code) + f'{ENDC}' +  ': ' + URL)
            f.write(URL+"\n")
        if r.status_code in redirects:
            f.write(URL+"\n")
            print(f'{WARNING} [+] HTTP ' + str(r.status_code) + ' Location: ' +  f'{ENDC}' +r.headers["Location"])
            if args.noredirect:
                h = r.headers["Location"]
                inputRequest(h.rstrip())

    except requests.exceptions.ConnectionError as e:  #To avoid to long error trace, just will respond with no conn msg 
    # the FAIL var give red color to text and ENDC will give you back your terminal color
        print(f'{FAIL} [-] {ENDC}' + 'No connection has been established for host/IP ' + f'{FAIL}' + URL + f'{ENDC}')
    except requests.exceptions.InvalidURL: 
        print(f'{FAIL} [-] {ENDC}' + "Invalid URL: " + URL)
    except requests.exceptions.ReadTimeout:
        print(f'{FAIL} [-] {ENDC}' + "Request timeout for URL: " + f'{FAIL}' + URL + f'{ENDC}')

f = open(fileName,"w")
inputType = inputValidation(args.input)
try:
    for host in IPNetwork(args.input):
        inputRequest(protocol+str(host)+slash)
except AddrFormatError:
    print(f'{WARNING} [-] {ENDC}' + 'Not valid IP or network address, will check if is valid domain')
    inputRequest(protocol+args.input.rstrip()+slash)

f.close()
