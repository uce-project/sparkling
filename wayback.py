import requests
from bs4 import BeautifulSoup

def get_product_name(asin):
    url = f"https://amazon.com{asin}"
    # A User-Agent is required so Amazon doesn't block the request immediately
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the main product title element on the Amazon page
        title_element = soup.find("span", id="productTitle")
        if title_element:
            return title_element.get_text().strip()
    return "Name not found"

# Example usage
print(get_product_name("B007JFMH8M"))
