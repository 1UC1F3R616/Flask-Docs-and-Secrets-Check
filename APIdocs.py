import argparse
import datetime
import math
import re
import requests
import shutil
import stat
import sys
import tempfile


parser = argparse.ArgumentParser()
parser.add_argument("f")
args = parser.parse_args()
if args.f in [None, 0, '']:
    print('[!] Filename not given.\n[!] Rerun the application')

# Required File with Routes 

try:
    filename = args.f # just this input
    with open(filename, 'r') as f:
        text = f.read()
        test_str = (text)
except Exception as e:
    print(str(e))
    exit(1)

def ascii_art():
    print(r"""

    _        ____                    ____       U  ___ u    ____    ____     
U  /"\  u  U|  _"\ u      ___       |  _"\       \/"_ \/ U /"___|  / __"| u  
 \/ _ \/   \| |_) |/     |_"_|     /| | | |      | | | | \| | u   <\___ \/   
 / ___ \    |  __/        | |      U| |_| |\ .-,_| |_| |  | |/__   u___) |   
/_/   \_\   |_|         U/| |\u     |____/ u  \_)-\___/    \____|  |____/>>  
 \\    >>   ||>>_    .-,_|___|_,-.   |||_          \\     _// \\    )(  (__) 
(__)  (__) (__)__)    \_)-' '-(_/   (__)_)        (__)   (__)(__)  (__)      

""")


# Finding Possible Secrets

BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
HEX_CHARS = "1234567890abcdefABCDEF"

try:
	with open('wordlist.txt') as w:
		regexList = w.read().split('\n')
except:
	raise Exception('Cannot open wordlist.txt')


def shannon_entropy(data, iterator):
    if not data:
        return 0
    entropy = 0
    for x in (ord(c) for c in iterator):
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy


def get_strings_of_set(word, char_set, threshold=20):
    count = 0
    letters = ""
    strings = []
    for char in word:
        if char in char_set:
            letters += char
            count += 1
        else:
            if count > threshold:
                strings.append(letters)
            letters = ""
            count = 0
    if count > threshold:
        strings.append(letters)
    return strings


final_raw= test_str
for regex in regexList:
    matches = re.finditer(regex, final_raw, re.MULTILINE | re.IGNORECASE)
    for matchNum, match in enumerate(matches, start=1):
        print ("[+] Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        for groupNum in range(0, len(match.groups())):
            groupNum = (groupNum + 1)
            print ("[+] Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

words =[word for word in final_raw.split(' ')]
print("\n")
for word in words: 
    foundSomething = False
    base64_strings = get_strings_of_set(word, BASE64_CHARS)
    hex_strings = get_strings_of_set(word, HEX_CHARS)
    for string in base64_strings:
        b64Entropy = shannon_entropy(string, BASE64_CHARS)
        if b64Entropy > 4.5:
            foundSomething = True
            printableDiff = string
    for string in hex_strings:
        hexEntropy = shannon_entropy(string, HEX_CHARS)
        if hexEntropy > 3:
            foundSomething = True
            printableDiff = string
    if foundSomething:
        print('[!] Suspicious string: ',printableDiff)


ascii_art()

# Now Generating APIdocs
# MyFunctions

def clean(x):
    return int(x.replace('#', '').replace('.', ''))


# Generate Result in md file

def result_md(routes, payloads, routes_count):

    payload_count = 0

    f = open('DOCS.md', 'a+')
    f.write('# API DOCS\n\n')

    for i in range(len(routes)):
        payload_old = payload_count
        payload_count += routes_count[i]
        
        if routes[i]==0:
            f.write("## {}\n".format(routes[i]))
        else:
            f.write("## {}\n```\n".format(routes[i]))

        for x in payloads[payload_old:payload_count]:
            f.write("- {}\n\n".format(x))
        
        if routes[i]==0:
            f.write('\n\n')
        else:
            f.write('```\n\n')
        


# Finding Routes

regex = r"@app.route\(.*\)"
matches = re.finditer(regex, test_str, re.MULTILINE)

ROUTES = []
for matchNum, match in enumerate(matches, start=1):
    ROUTES.append("{match}".format(match = match.group()))


# Finding Inside PayLoads

regex = r"payLoad.*{.*\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*\s*}\s*.*\)"
matches = re.finditer(regex, test_str, re.MULTILINE)

PAYLOADS = []
for matchNum, match in enumerate(matches, start=1):
    PAYLOADS.append(match.group())


# Finding PayLoad Count: PayLoad which are not in used format are discarded | This is a bug

regex = r"#\.\d\."
matches = re.finditer(regex, test_str, re.MULTILINE)

ROUTES_COUNT = []
for matchNum, match in enumerate(matches, start=1):
    ROUTES_COUNT.append(clean(match.group()))


result_md(routes=ROUTES, payloads=PAYLOADS, routes_count=ROUTES_COUNT)