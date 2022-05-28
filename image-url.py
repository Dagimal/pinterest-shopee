from bing_image_urls import bing_image_urls
import simple_image_download.simple_image_download as simp
import sys

def bing_image(keywords, lim):
	print(bing_image_urls(keywords, limit=lim))

def google_image(keywords, lim):
	response = simp.Downloader()
	response.search_urls(keywords, limit=int(lim))
	URL = response.get_urls()
	f = open(keywords, "w")
	print('\n'.join(URL), file=f)

"""
command variables
"""
searchEngine = sys.argv[1]
keyWord = sys.argv[2]
imgLimit = sys.argv[3]

if searchEngine == "bing":
	bing_image(keyWord, imgLimit)
elif searchEngine == "google":
	google_image(keyWord, imgLimit)
