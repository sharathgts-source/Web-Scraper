import requests
from bs4 import BeautifulSoup

# Target URL (You can replace this with any public news website)
URL = "https://www.bbc.com/news"  # Example: BBC News

# Send HTTP GET request
response = requests.get(URL)

# Check for successful response
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all headline elements (BBC uses h2 tags for many headlines)
    headlines = soup.find_all('h2')

    # Extract and clean the text
    cleaned_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

    # Remove duplicates
    unique_headlines = list(set(cleaned_headlines))

    # Save to a .txt file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for idx, title in enumerate(unique_headlines, start=1):
            file.write(f"{idx}. {title}\n")

    print(f"✅ {len(unique_headlines)} headlines saved to headlines.txt")
else:
    print("❌ Failed to retrieve the page. Status code:", response.status_code)
