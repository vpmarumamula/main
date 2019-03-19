from bs4 import BeautifulSoup
import requests

#print('imports ready')
with open('simple.html', 'r') as simplehtml:
    #htmlstrdata = simplehtml.read()
    # print(htmlstrdata)
    soup = BeautifulSoup(simplehtml, 'lxml')
    # print(soup.prettify())
# we can use like variables instead of methods
# first title if  multiple are there
match = soup.title
print('match = {}'.format(match))
match1 = soup.title.text
print('match1 = {}'.format(match1))
# if we want div there are multiple divs, for  that use find method
match2 = soup.find('div')
print('match2 = {}'.format(match2))
# more options to narrow down.class_ because class is spl.We can also use option like id etc
match3 = soup.find('div', class_='footer')
print('match3 = {}'.format(match3))
# now if you want para data in footer we can use just match3 instead of whole file again to find it
match4 = match3.find('p')
print("match4 = {}".format(match4))
# we can find href inside article by
article = soup.find('div', class_='article')
print('article = {}'.format(article))
atext = article.h2.a.text
print('atext = {}'.format(atext))

# Now,  if there are multiple articles  we can get all articles in a list using findall
print('following is a list of articles:')
articlelist = soup.find_all('div', class_='article')

print(articlelist)
for artitem in articlelist:
    print("article item text = {}".format(artitem.h2.text))
