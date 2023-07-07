import urllib.request
from bs4 import BeautifulSoup

# To Scrape
def Scrape():
	user = str(input('Type the desired page number : '))
	url = 'https://xkcd.com/' + user + '/'
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
	header = {'User-Agent' : user_agent} 

	#Request the URL and open it
	requesting = urllib.request.Request(url, None ,header)

	with urllib.request.urlopen(requesting) as resp:
		read = resp.read()

	# Parse the HTML
	soup_read = BeautifulSoup(read, 'html.parser')
	url_list = []

	# Find all the URLs to get the desired URL
	for link in soup_read.find_all('a'):
		url_list.append(link.get('href'))

	return url_list[26] # This is the desired URL

# Downloader
def IMG_Download(url, filepath):
	urllib.request.urlretrieve(url, filepath)

# Execution
IMG_Download(Scrape(), 'Downloads/' + str(input('filename? : ')) + '.jpg')