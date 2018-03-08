# Amazon-Mobile-Sentiment-Analysis

### Desciption :

*This project works by scraping Amazon reviews for the user-desired mobile phone.
The first part includes searching the phone and scraping the reviews using infinite scrolling.
The second part includes training of NaiveBayesClassifier model on dataset and classifying the product reviews.*

### Tasks :

*Searching the mobile phone on Amazon search bar*

*Finding the desired product i.e. 64GB, 128GB*

*Scraping the first 20(default, can be changed) pages of customer reviews sorted from new to old using infinite scrolling*

*Training the NaiveBayesClassifier algorithm on dataset*

*Classifying the reviews*

### Packages/tools used :

*lxml library to use HTML element API*

*XML parser to parse the URL data into XML file*

*requests library to send HTTP request to Amazon webpage*

*NLTK library to use NaiveBayesAlgorithm and other features like bag-of-words, word-tokenizing*

### Requirements :

*pip(Python Package Index) :*
	
	$ sudo apt-get install python3-pip
		
*requests package :*
	
	$ pip3 install requests
		
*lxml package :*
	
	$ sudo apt-get install libxml2-dev libxslt1-dev python-dev

	$ pip install lxml

*NLTK :*
	
	$ pip install nltk
	
*To download nltk data, run following command on Python :*

	import nltk

*Select ALL from the pop-up GUI*
