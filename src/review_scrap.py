import requests
import progress_bar
from lxml import html

def get_reviews(review_tab) :

	page = requests.get(review_tab)

	tree = html.fromstring(page.content)

	all_reviews = tree.xpath("//a[@class='a-link-normal a-color-base a-text-normal']")[0].get("href")

	review_list = []

	if(all_reviews.find('#') != -1):
		i = len(all_reviews) - 1
		while(all_reviews[i] != '#'):
			all_reviews = all_reviews[:-1]
			i-=1
		all_reviews = all_reviews[:-1]

	start = "https://www.amazon.in/"

	all_reviews = start + all_reviews
	all_reviews = all_reviews.replace("_dp_", "_arp_")
	all_reviews = all_reviews.replace("ttl?", "paging_btm_1?")
	all_reviews += "&pageNumber=1"

	print("\nFetching reviews...")
	count = 0

	review_pages = 20
	adder = 100/review_pages
	while(review_pages > 0):
		count += adder
		if count == 100: 
			progress_bar.progress(100.0, 100, True)
		else:
			progress_bar.progress(count, 100)

		num = all_reviews.find("recent&pageNumber=")
		num += 17
		pipe = ""

		for i in range(0, num+1):
			pipe += all_reviews[i]

		curr = int(all_reviews[num+1 : len(all_reviews)])
		curr += 1
		pipe += str(curr)
		all_reviews = pipe

		review_pages -= 1

		page = requests.get(all_reviews)

		tree = html.fromstring(page.content)

		data = ""

		data = tree.xpath("//*[@id='cm_cr-review_list']/div/span/text()")

		if(len(data) == 1 and data[0] == "Sorry, no reviews match your current selections."):
			break

		data = tree.xpath("//div[@class = 'a-row review-data']/span[@class = 'a-size-base review-text']/text()")

		saviour = []

		for i in range(0, len(data)):
			review_list.append(data[i])

	return review_list
