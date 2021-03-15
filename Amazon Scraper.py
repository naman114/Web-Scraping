import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://www.amazon.in/product-reviews/B07XG2PKVS/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&filterByStar=positive&reviewerType=all_reviews&pageNumber=1#reviews-filter-bar"

r = requests.get(url)
htmlContent = r.content

# print(htmlContent)

soup = bs(htmlContent, "html.parser")
# print(soup.prettify())

names = soup.find_all("span", class_="a-profile-name")
# print(names)

cust_name = []
for i in range(0, len(names)):
    cust_name.append(names[i].string)

# for elem in hset:
#     print(elem)

review_block = soup.find_all("a", class_="review-title-content")
# print(review_block)

review_heading = []

for i in range(0, len(review_block)):
    review_heading.append(review_block[i].get_text())

# print(review_heading)

review_heading[:] = [titles.lstrip("\n") for titles in review_heading]
review_heading[:] = [titles.rstrip("\n") for titles in review_heading]

# print(review_heading)

rating_block = soup.find_all("i", class_="review-rating")
# print(rating_block)

rating_values = []
for i in range(0, len(rating_block)):
    rating_values.append(rating_block[i].get_text())

# print(rating_values)


review_body_block = soup.find_all("span", class_="review-text-content")
# print(review_body_block)
review_body = []

for i in range(0, len(review_body_block)):
    review_body.append(review_body_block[i].get_text())

review_body[:] = [review.lstrip("\n\n ") for review in review_body]
review_body[:] = [review.rstrip("\n\n ") for review in review_body]

# print(review_body)

# To search by data hook or anything other than a class, you need a dictionary
# review = soup.find_all('span', {"data-hook":"review-body"})
# test = soup.find_all("span", {"data-hook": "review-body"})
# print(test)

# For dictionary make sure you use colon


# Converting this data to csv: comma separated value

print(len(cust_name))
print(len(review_heading))
print(len(rating_values))
print(len(review_body))
cust_name.pop(0)
cust_name.pop(0)
rating_values.pop(0)
rating_values.pop(0)

df = pd.DataFrame()
df["Customer Name"] = cust_name
df["Review Title"] = review_heading
df["Rating"] = rating_values
df["Review"] = review_body
print(df)

df.to_csv(
    r"d:\Users\sumit\Desktop\Naman\BeautifulSoup\amazonReviewData.csv", index=True
)
