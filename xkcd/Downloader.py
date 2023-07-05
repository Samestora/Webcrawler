import urllib.request
import Scrapper

def IMG_Download(url, filepath):
	urllib.request.urlretrieve(url, filepath)
	
IMG_Download(Scrapper.Scrape(), 'Downloads/' + str(input('filename? : ')) + '.jpg')