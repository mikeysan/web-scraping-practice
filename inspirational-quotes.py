# This is a simple script to extract quotes from Goodreads.com
# It was inspired by https://github.com/tintindas/goodreads-quote-scraper
# which is a Javascript version (some what)
# I wanted to see if I could do something similar in Python.
# It has massive room for improvement, but I am happy with it for now.

import requests
from bs4 import BeautifulSoup
import random

url = "https://www.goodreads.com/quotes/tag/inspirational"
response = requests.get(url)

soup = BeautifulSoup(response.content, features="html.parser")
result = soup.find('div', class_='leftContainer')

# allQuotes = result.find_all('div', class_='quote mediumText')
# print(allQuotes)
# print()


quotes = result.find_all('div', class_='quoteText')

# My attempt to exclude the author span when we go through each item later
# It didn't work. Maybe someone can tell me why later or
# I'll figure it out at some point
unwanted = result.find('span', class_='authorOrTitle')

# I would like to hold the results in a list so I can use them later
holdMyQuote = []

# Using a for loop to iterate through the 'quoteText' class to get all the entries
# We then add ech entry to the 'holdMyQuote' list we created above
for item in quotes:
    unwanted.extract()
    quoteTxt = item.text.strip()
    holdMyQuote.append(quoteTxt.strip('\n'))

print("-" * 60)
# print(holdMyQuote[29])

# I am adding this to print one random quote each time we run this
x = random.randint(0, 30)
print(holdMyQuote[x])