from bs4 import BeautifulSoup
import requests

# source has just request and status, so we need to run text on that
source = requests.get('http://coreyms.com').text
# the source needs to be parsed.
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())
