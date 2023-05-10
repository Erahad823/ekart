from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os
import chromedriver_autoinstaller
import csv
import time

class Scraper():
    def __init__(self):
        
        if os.path.exists('chromedriver'):
        
            self.chromedriver_path = chromedriver_autoinstaller.install(
                path=f"{os.getcwd()}/chromedriver")
        else:
            os.mkdir('chromedriver')
            self.chromedriver_path = chromedriver_autoinstaller.install(
                path=f"{os.getcwd()}/chromedriver")

        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--headless')
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-blink-features')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(service=ChromeService(self.chromedriver_path), options=self.options)


    def category(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "lxml")

        cat = []
        div = soup.find("div", attrs={"class": "footer-top-main-section"})
        for a in div.find_all("a"):
            href = a.get("href")
            cat.append(href)
        return cat
        
    def sub_cat(self,cat):
        ksh = []
        for c in cat:
            response = ("https://www.jiomart.com/" +  c)
            print(response)
            ksh.append(response)
        return ksh

    def cat(self,ksh):
        for lis in ksh:
            driver = self.driver
            driver.get(lis)  
            driver.execute_script('return ')
                     
            
li = Scraper()
p = li.category(url="https://www.jiomart.com/")
c = li.sub_cat(p)
li.cat(c)
