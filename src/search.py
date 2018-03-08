import requests
import sys
from lxml import html

def get_first_from_search(info) :

	splitter = info.split()

	url = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Delectronics&field-keywords='

	for i in range(0, len(splitter)):
		if(i == 0):
			url = url + splitter[i]
		else:
			url = url + '+' + splitter[i]

	url += "&rh=n%3A976419031%2Ck%3A"

	for i in range(0, len(splitter)):
		if(i == 0):
			url = url + splitter[i]
		else:
			url = url + '+' + splitter[i]

	page = requests.get(url)

	tree = html.fromstring(page.content)

	name = tree.xpath('//*[@id="result_0"]/div/div[3]/div[1]/a/h2/text()')

	if len(name) == 0:
		print("\nError\nPossible errors : Incorrect input/Connectivity problem/Product irrelevant\n")
		sys.exit(0)
	
	print("\nShowing results for", name[0])

	data = tree.xpath("//a[@class='a-size-small a-link-normal a-text-normal']")

	ans = ""

	for i in range(0, len(data)):
		data[i] = data[i].get("href")
		if(data[i].find("#customerReviews") != -1):
			ans = data[i]
			break

	return ans
