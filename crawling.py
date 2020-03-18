import urllib.request
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
req = urllib.request.urlopen(url)
res = req.read()

soup = BeautifulSoup(res, 'html.parser')
all_divs = soup.find_all("table", {"id":"constituents"})
print(all_divs)