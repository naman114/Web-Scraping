import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

# 1. Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)


# 2. Parse the HTML
soup = BeautifulSoup(htmlContent, "html.parser")
# print(soup.prettify)


# 3. HTML Tree Traversal
title = soup.title
# print(title)              Prints title tag
# print(type(title))            title is a bs4.Element.Tag object
# print(type(title.string))   The object has many attributes e.g. string which prints the string in the title

# Commonly used types of objects
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment


# Webscraping

# Print all paras
# paras = soup.find_all("p")
# print(paras)

# anchor_tags = soup.find_all("a")
# print(anchor_tags)

# First occurence of the element
# print(soup.find("p"))

# Print class of that element
# print(soup.find("p")["class"])

# Find all elements with class lead
# print(soup.find_all("p", class_="lead"))

# Get text from tags/soup. Gives just the text and not the entire tag
# print(soup.find("p").get_text())
# print(soup.get_text())


# Fetching links

# anchors = soup.find_all("a")
# all_links = set()

# for link in anchors:
#     if link.get("href") != "#":
#         linkText = "https://codewithharry.com" + link.get("href")
#         all_links.add(linkText)

# print(all_links)


# Comments
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# To print the entire html
# print(soup2)
# To print just the p tag
# print(soup2.p)
# To print just the string of the p tag
# print(soup2.p.string)
# Comment object
# print(type(soup2.p.string))


navbarSupportedContent = soup.find(id="navbarSupportedContent")
# print(navbarSupportedContent.children)
# print(navbarSupportedContent.contents)
# Assume that the above 2 are same for the time being

# for elem in navbarSupportedContent.contents:
#     print(elem)

# for elem in navbarSupportedContent.strings:
#     print(elem)

# To arrange the data closely
# for elem in navbarSupportedContent.stripped_strings:
#     print(elem)

# Can print any element's parent tag
# print(navbarSupportedContent.parent)

# To get an iterable generator object for the parents of the current tag: use parents
# for elem in navbarSupportedContent.parents:
#     print(elem.name)

# Next and previous siblings: (Treats spaces as siblings)
# print(navbarSupportedContent.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)
