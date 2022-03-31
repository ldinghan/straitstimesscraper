from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from collections import defaultdict

chrome_options = Options()
chrome_options.add_argument('--headless')
url = "https://www.straitstimes.com/"
s = Service("C:/Users/user/.wdm/drivers/chromedriver/win32/99.0.4844.51/chromedriver.exe")

driver = webdriver.Chrome(service=s, options = chrome_options)
driver.get(url)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

all_news = soup.find_all("h5", class_="card-title")
news_data = defaultdict(list)


for item in all_news:
	item_string = str(item)
	if "<span" not in item_string:
		item_string = item_string[34:]
		category = item_string[:item_string.index('/')]
		news = item.get_text().strip('\n')
		news_data[category].append(news)


for category in news_data:
	print(category.upper())
	for headline in news_data[category]:
		print(headline)
	print('\n')