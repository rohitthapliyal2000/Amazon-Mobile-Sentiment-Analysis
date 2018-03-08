import search
import opinion_mining_training_module
import review_scrap
import sys

info = input("\nEnter info : ")

review_tab = search.get_first_from_search(info)

if (review_tab == ""):
	print("\nError\nPossible errors : Incorrect input/Connectivity problem/Product irrelevant\n")
	sys.exit(0)

review_list = review_scrap.get_reviews(review_tab)

opinion_mining_training_module.sentiment_analysis(review_list)
