import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

reviews_list = []

url = "https://www.airlinequality.com/airline-reviews/british-airways/page/1/"

# Browser jaisa header (important)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

try:
    print("Connecting to website...")

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
        print("Connected successfully!")

        soup = BeautifulSoup(response.text, "html.parser")

        reviews = soup.find_all("div", class_="text_content")

        for review in reviews:
            reviews_list.append(review.text.strip())

        df = pd.DataFrame(reviews_list, columns=["review"])

        df.to_csv("data/reviews.csv", index=False)

        print("Reviews saved successfully!")

    else:
        print("Failed to fetch page. Status:", response.status_code)

except Exception as e:
    print("Error:", e)
