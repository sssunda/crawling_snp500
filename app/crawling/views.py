# Third Party Module Import
from bs4 import BeautifulSoup
from flask import Blueprint

# Python Module Import
import urllib.request

crawling_blueprint = Blueprint('crawling', __name__)

@crawling_blueprint.route('/')
def crawling():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    req = urllib.request.urlopen(url)
    res = req.read()
    result = []

    soup = BeautifulSoup(res, 'html.parser')
    snp_table = soup.find("table", {"id": "constituents"})
    # except table head row
    snp_rows = snp_table.find_all("tr")[1:]

    for idx, row in enumerate(snp_rows):
        result.append(str(idx+1)+"."+row.find_all('a')[1].get_text())
    result = "<br>".join(result)
    return str(result)