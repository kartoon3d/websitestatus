import json
import requests
import sys

second_arg = sys.argv[2]

def get_url_status(urls):
    web_failed=0
    web_ok=0
      
    for url in urls:
        try:
            r = requests.get(url,  verify=False, timeout=10) # 10 second
            print(url + "\tStatus: " + str(r.status_code))
            web_ok = web_ok + 1
        except Exception as e:
            print(url + "\tNA FAILED \t" + str(e))
            web_failed = web_failed + 1
    print('Ok:'+ str(web_ok))
    print('Failed:'+ str(web_failed))

def read(file=second_arg):
 
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]
        get_url_status(lines)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
