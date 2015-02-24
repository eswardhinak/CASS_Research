import requests
import urllib2, json
import ssl


url = "http://localhost:8000/"
#url = "http://www.quotefaces.com/"
try:
	res = requests.get(url)
except requests.exceptions.ConnectionError as e:
	print "Error."
information = {'value' : 1}
headers = {'Content-type': 'application/json'}

#print json.dumps(information)
#print headers
response = requests.post(url, data=json.dumps(information), headers=headers)
