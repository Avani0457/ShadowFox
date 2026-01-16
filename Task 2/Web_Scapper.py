import requests
from bs4 import BeautifulSoup

# STEP 1: Choose Website
URL = "https://www.shadowfox.org.in/"   # can be replaced with any text webpage

try:
    # STEP 2 & 3: Fetch Webpage Content
    response = requests.get(URL, timeout=5)

    # Handle Wrong Status Codes
    if response.status_code != 200:
        print("Error: Website returned status code", response.status_code)
        exit()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # STEP 4: Extract Data
    headings = [h.get_text(strip=True) for h in soup.find_all('h1')]
    paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # STEP 5: Store Data in Text File
    with open("web_scraped_data.txt", "w", encoding="utf-8") as file:
        file.write("SCRAPED DATA FROM SHADOWFOX WEBSITE\n")

        file.write("HEADINGS:\n")
        for h in headings:
            file.write("- " + h + "\n")

        file.write("\nPARAGRAPHS:\n")
        for p in paragraphs:
            file.write("- " + p + "\n")

        file.write("\nLINKS:\n")
        for link in links:
            file.write("- " + link + "\n")

    print("Scraping Completed! Data saved to web_scraped_data.txt")

# STEP 6: ERROR HANDLING
except requests.exceptions.Timeout:
    print("Error: Request Timed Out.")
except requests.exceptions.ConnectionError:
    print("Error: Unable to Connect to Website. Check Internet.")
except requests.exceptions.MissingSchema:
    print("Error: Invalid URL Format.")
except Exception as e:
    print("Unexpected Error:", e)
