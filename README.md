# Automated Web Scraping with Selenium and BeautifulSoup

This repository contains a Python project that demonstrates automated web scraping using Selenium and BeautifulSoup libraries. The project aims to provide a streamlined solution for extracting data from websites in an automated manner.

## Features

- Automated web scraping using Selenium and BeautifulSoup
- Advanced search functionality to filter results
- Extracts movie details including title, year, duration, genre, and rating
- Saves the extracted data to a CSV file

## Prerequisites

To run the project locally, you need to have the following software installed:

- Python (version X.X.X)
- ChromeDriver (download from: https://sites.google.com/a/chromium.org/chromedriver/)

## Installation

1. Clone the repository:

- git clone https://github.com/CodeWithZalak/automated-web-scraping-selenium-bs4.git

2.Install the required Python dependencies:

 - pip install -r requirements.txt
  
3.Configure the ChromeDriver path:

 - Open the config.py file and update the CHROME_DRIVER_PATH variable with the path to your ChromeDriver executable.

## Usage
Run the Python script:

python main.py
This will launch the automated web scraping process.

Once the script completes, you will find the extracted movie data saved in a file named IDMB_Movies.csv.

## Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgements
Selenium - Web scraping and automation tool
BeautifulSoup - HTML parsing library
Requests - HTTP library for making requests
Pandas - Data manipulation and analysis tool
