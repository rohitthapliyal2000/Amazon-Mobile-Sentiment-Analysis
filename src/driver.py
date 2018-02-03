import search
import reviews

info = input("Enter info : ")

review_tab = search.get_first_from_search(info)

review_info = reviews.get_reviews(review_tab)
