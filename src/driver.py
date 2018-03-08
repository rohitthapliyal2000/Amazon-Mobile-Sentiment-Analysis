import search
import training_module
import reviews
import sys

info = input("\nEnter info : ")

review_tab = search.get_first_from_search(info)

if (review_tab == ""):
	print("Error while scraping\nPossible errors : Incorrect input or connectivity problem\n")
	sys.exit(0)

review_list = reviews.get_reviews(review_tab)

training_module.sentiment_analysis(review_list)
