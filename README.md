# Web Scraping Project with Python

This project provides Python scripts for web scraping product information from Amazon. The project consists of two main scripts:

1. `scrape.py`: This script scrapes product details, such as product titles and prices, from Amazon search results and saves the data to an Excel file.

2. `brand.py`: This script extends the functionality of the previous script by scraping additional information, specifically the brand of each product, and adds it to a new Excel file.

## Features

- User-Agent Rotation: The scripts rotate through a list of user-agent strings to mimic different browsers, making the scraping process more like human behavior.

- Random Delay: A random delay is introduced between requests to avoid overloading the server with too many requests in a short time.

## Prerequisites

Before running the scripts, ensure you have the following prerequisites:

- Python 3.x (Python 3.3 or later is recommended)
- `virtualenv` (optional but recommended for managing dependencies)

__Create a virtual environment (Optional):__
- `python -m venv venv`

- Activate the virtual environment:

   __On Windows:__
  `venv\Scripts\activate`

  __On macOS and Linux:__
  `source venv/bin/activate`

## Install project dependencies:
- `pip install requests beautifulsoup4 openpyxl pandas`

-  Or to install the dependencies from the requirements.txt file, you can use the following command:
 `pip install -r requirements.txt`

## Run the scripts as needed:

1. To run scrape.py, use:
-  `python scrape.py`

_This script scrapes product titles and prices from Amazon search results and saves the data to an Excel file named amazon_products.xlsx._

2. To run brand.py, use:
- `python brand.py`

_This script extends the functionality by scraping brand information and adding it to the existing Excel file (amazon_products_with_brand.xlsx)._

## Deactivate the virtual environment when you're done:
- `deactivate`

## Project Structure
1. scrape.py: The main Python script for scraping product titles and prices.
2. numprod.py: The script for scraping brand information and updating the Excel file.
3. README.md: This documentation file.

## Acknowledgments
1. Requests - For making HTTP requests.
2. Beautiful Soup - For parsing HTML content.
3. openpyxl - For working with Excel files.
4. pandas - For data manipulation and handling DataFrames.
