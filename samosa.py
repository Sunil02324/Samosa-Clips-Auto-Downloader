import requests
import json
import urllib
import urllib2
import pynotify
from time import sleep
from random import randint


a = []
b = []
i = 0

def popup(title, message):
    pynotify.init("Test")
    pop = pynotify.Notification(title, message)
    pop.show()
    return

def samosa():
	global i
	#Using more URLs to download maximum clips from the requests
	b.append('https://the-tasty-samosa.appspot.com/_ah/api/samosa/v1/expressions/popular')
	b.append('https://the-tasty-samosa.appspot.com/_ah/api/samosa/v1/expressions/recent')
	b.append('https://the-tasty-samosa.appspot.com/_ah/api/samosa/v1/expressions/recent')
	b.append('https://the-tasty-samosa.appspot.com/_ah/api/samosa/v1/expressions/popular')
	#Got the headers from the browser
	headers = {
	    'x-goog-encode-response-if-executable': 'base64',
	    'accept-encoding': 'gzip, deflate, sdch',
	    'x-origin': 'http://getsamosa.com',
	    'x-clientdetails': 'appVersion=5.0%20(X11%3B%20Linux%20x86_64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F48.0.2564.109%20Safari%2F537.36&platform=Linux%20x86_64&userAgent=Mozilla%2F5.0%20(X11%3B%20Linux%20x86_64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F48.0.2564.109%20Safari%2F537.36',
	    'accept-language': 'en-US,en;q=0.8',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
	    'accept': '*/*',
	    'referer': 'https://the-tasty-samosa.appspot.com/_ah/api/static/proxy.html?jsh=m%3B%2F_%2Fscs%2Fapps-static%2F_%2Fjs%2Fk%3Doz.gapi.en.a_H8_1L9VPo.O%2Fm%3D__features__%2Fam%3DAQ%2Frt%3Dj%2Fd%3D1%2Ft%3Dzcms%2Frs%3DAGLTcCO6g8LzWY4Tnes3mZRHS682lN-HKQ',
	    'authority': 'the-tasty-samosa.appspot.com',
	    'cookie': '_ga=GA1.3.1633115093.1455397169',
	    'x-javascript-user-agent': 'google-api-javascript-client/1.1.0-beta',
	    'x-referer': 'http://getsamosa.com',
	}

	# We have proxy enabled in our institute. If you are using direct connections comment the below lines
	http_proxy  = "http://10.3.100.207:8080"
	https_proxy = "https://10.3.100.207:8080"
	proxyDict = { 
	              "http"  : http_proxy, 
	              "https" : https_proxy
	            }

	url = str(b[randint(0,3)])
	joke_txt = requests.get(url, headers=headers, proxies=proxyDict).content
	joke_text = json.loads(joke_txt.decode())
	for joke in joke_text['voices']:
		#Checking if the clip is already downloaded
		if joke['key'] in a:
			continue
		else:
			a.append(joke['key'])
			mpurl = joke['mp3_url']
			try:
				urllib.urlretrieve(joke['mp3_url'], joke['transcript'] + '.mp3')
				i = i + 1
				print str(i) + '. ' + joke['transcript']
			#Because of proxy, I was facing Sockets error and Connection errors. Below lines are for handling those exceptions and errors
			except IOError as e:
				print "Socket error. Sleeping for 5 seconds"
				sleep(5)
				continue
			except requests.exceptions.ConnectionError as e:
				print "Proxy Error. Stopping the script for 5 seconds"
    			sleep(5)
    			continue
	popup("Total Downloaded :-", str(i)) #Notify the total number of downloads
	sleep(5) #sleep for 5 secs

if __name__ == "__main__":
	while True:
		samosa()
