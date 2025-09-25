# Web-Scraper
Web Scraper for News Headlines.


To build a Python-based web scraper that automatically extracts top news headlines from a public news website (e.g., BBC News) and saves them into a .txt file. This project demonstrates web automation, data parsing, and file handling — useful skills for data collection and monitoring.

How It Works:

Send HTTP Request: The script uses requests to fetch the HTML content of the news website (e.g., https://www.bbc.com/news).

Parse HTML: It uses BeautifulSoup to parse the HTML and find all headline elements, typically located in <h2> or <h3> tags with specific classes.

Extract Headlines: The script extracts the text content of each headline.

Save to File: All extracted headlines are written to a local text file (headlines.txt), each on a new line and numbered for clarity.
