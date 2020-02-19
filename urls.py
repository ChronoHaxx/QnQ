import requests# to download the html file
from bs4 import BeautifulSoup #to parse html file

url = "https://pastpapers.papacambridge.com/?dir=Cambridge%20International%20Examinations%20%28CIE%29/AS%20and%20A%20Level/Chemistry%20%289701%29"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

links = []
for link in soup.findAll('a', class_='clearfix'): #loop through all clickable link in page
    link = link.get('href')
    url = "https://pastpapers.papacambridge.com/" + link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.findAll('a', class_='btn btn-outline-primary bbx hidden-sm hidden-xs pull-right'): #loop to get all download pdf link
        link = link.get('href')
        link = "https://pastpapers.papacambridge.com/" + link
        links.append(link)

print('Finished extracting links...')