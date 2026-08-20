import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://quotes.toscrape.com/"

# Send request to website
response = requests.get(url)

# Check whether website opened successfully
if response.status_code == 200:

    # Read HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quotes
    quotes = soup.find_all("div", class_="quote")

    # Create CSV file
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Header
        writer.writerow(["Quote", "Author"])

        # Extract data
        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text

            print("Quote:", text)
            print("Author:", author)
            print("-" * 50)

            writer.writerow([text, author])

    print("✅ Data saved successfully in quotes.csv")

else:
    print("❌ Website could not be accessed.")