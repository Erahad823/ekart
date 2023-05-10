from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.jiomart.com/c/groceries/2")
soup = BeautifulSoup(response.content, 'lxml')
category_div = soup.find("div", attrs={'id': "actionField"})
print(category_div)

print("================================tHIS IS MY BRANCH =================================")
print("================================ecnekc,mw")