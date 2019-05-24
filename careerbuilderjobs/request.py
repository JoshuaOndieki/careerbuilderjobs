from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import time
from bs4 import BeautifulSoup as bs


class SeleniumDriver:
    """
        Selenium Driver used to be used in scraping.
    """
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)


# # Direct request using Requests
# rstart = time.time()
# res = requests.get('https://www.careerbuilder.com/job/JD70RJ6FFHF8RDVJGHT')
# soup = bs(res.content, 'html.parser')
# summary = soup.find('div', class_='small-12 columns item')
# print(summary.text)
# rend = time.time()
# print('REQUESTS: ', rend - rstart)
#
#
# Direct request using Selenium
driver = SeleniumDriver().driver

sstart = time.time()
driver.get('https://www.careerbuilder.com/job/JD70RJ6FFHF8RDVJGHT')
send = time.time()
print('SELENIUM: ', send - sstart)
driver.close()

# # Explicit request using Selenium
# driver = SeleniumDriver().driver
# driver.get('https://google.com')
# esstart = time.time()
# driver.get('https://www.careerbuilder.com/job/JD70RJ6FFHF8RDVJGHT')
# WebDriverWait(driver, 2).until(
#     EC.presence_of_element_located((By.CLASS_NAME, 'with-padding'))
# )
# esend = time.time()
# print('EXPLICIT WAIT SELENIUM: ', esend - esstart)
# driver.close()
