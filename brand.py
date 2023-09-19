import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# User-Agent strings to mimic different browsers
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/86.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/88.0.705.63',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/50.0',

    'Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',

    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',

    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3',

    'Opera/9.80 (Windows NT 6.2; WOW64) Presto/2.12.388 Version/12.17',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Media Center PC',
    'Mozilla/4.08 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
]

# Function to send a request with random User-Agent and delay
def send_request(url):
    headers = {
        'User-Agent': random.choice(user_agents),
    }
    response = requests.get(url, headers=headers)
    time.sleep(random.uniform(0.5, 3))  # Add a random delay between 0.5 seconds to 3 second 
    return response

df = pd.read_excel('products.xlsx')

url_template = 'https://www.amazon.in/gp/product/{}/?th=1'

brand_list = []

# Iterate through each ASIN in the DataFrame
for asin in df['Data-ASIN']:
    # Construct the URL for the specific ASIN
    url = url_template.format(asin)

    # Try to send the request multiple times with different user agents
    for _ in range(3):
        response = send_request(url)
        if response.status_code == 200:
            break
        else:
            print("Failed to fetch the page for ASIN:", asin)
            brand_list.append("Brand not found on the page.")
            continue

    soup = BeautifulSoup(response.content, 'html.parser')

    brand_element = soup.find("span", {"class": "a-size-base po-break-word"})

    # Extract the brand from the element
    if brand_element:
        brand = brand_element.text.strip()
    else:
        brand = "Brand not found on the page."

    # Append the brand to the list
    brand_list.append(brand)

# Add the brand information as a new column in the DataFrame
df['Brand'] = brand_list

# Save the updated DataFrame to the Excel file
df.to_excel('final.xlsx', index=False)

print("Brand information has been successfully added and saved to final.xlsx")

