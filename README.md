# Crypto_webscraper
Uses BeautifulSoup to scrape data from a crypto website and then stores it in a MySQL database.

Overview
This Python script fetches information about the top cryptocurrencies from CoinMarketCap and stores it in a MySQL database. It uses BeautifulSoup for web scraping and MySQL Connector for database interaction.

Prerequisites
Python 3.x
BeautifulSoup
Requests
MySQL Connector

Setup
Clone the repository:
git clone https://github.com/yourusername/crypto-data-scraper.git
cd crypto-data-scraper

Install required libraries:
pip install beautifulsoup4 requests mysql-connector-python

Set up MySQL:
Install MySQL and create a database (e.g., DBMS_ass).
Update the script with your MySQL server details (host, user, password).

Usage
Run the script:
python crypto_scraper.py

The script will connect to CoinMarketCap, scrape data, and insert it into the MySQL table.

Check your MySQL database to view the stored cryptocurrency data.

MySQL Table Structure

CREATE TABLE crypto (
    short_name VARCHAR(30),
    name VARCHAR(30) PRIMARY KEY,
    value VARCHAR(15)
);

Important Note
Ensure your MySQL server is running and accessible.
Update script details with your MySQL server information.

Acknowledgments
This project demonstrates web scraping and database interaction for cryptocurrency data.
Feel free to modify and share this code!
