import requests
from bs4 import BeautifulSoup

orig_url = 'https://digiscore.dmu.ac.uk/wp-json/wp/v2/posts?order=asc'
# orig_url = 'https://digiscore.dmu.ac.uk/2022/03/01/digital-musicianship-forum-oporto-portugal/'
blog_name = 'The Digital Score'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
blog_json = requests.get(orig_url, headers=headers).json()

# print(blog_json)
# blog_json = requests.get(orig_url, headers=headers).json()
entry = blog_json[0]
list(entry.keys())

entry_content = entry['content']['rendered']
print(entry_content)


#
# # Importing BeautifulSoup class from the bs4 module
# from bs4 import BeautifulSoup
#
# # Opening the html file
# HTMLFile = open("_wp_originals/index.html", "r")
#
# # # Reading the file
# # index = HTMLFile.read()
# # url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
# html = HTMLFile.read()
# soup = BeautifulSoup(html, features="lxml")
#
# articles = soup.find_all('article', class_='post-summary')
#
# print(articles)
# # for a in articles:
# #     print(a)
#
#
# #
# #
# # # kill all script and style elements
# # for script in soup(["script", "style"]):
# #     script.extract()    # rip it out
# #
# # # get text
# # # text = soup.get_text()
# # text = soup.get_text(separator=' ')
# #
# # # break into lines and remove leading and trailing space on each
# # lines = (line.strip() for line in text.splitlines())
# # # break multi-headlines into a line each
# # chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # # drop blank lines
# # text = '\n'.join(chunk for chunk in chunks if chunk)
# #
# # print(text)
#
# # # Importing BeautifulSoup class from the bs4 module
# # from bs4 import BeautifulSoup
# #
# # # Opening the html file
# # HTMLFile = open("_wp_originals/index.html", "r")
# #
# # # # Reading the file
# # # index = HTMLFile.read()
# #
# # # Creating a BeautifulSoup object and specifying the parser
# # S = BeautifulSoup(HTMLFile, 'lxml')
# #
# # # Creating a BeautifulSoup object and specifying the parser
# # # S = BeautifulSoup(Web.text, 'lxml')
# #
# # # Using the prettify method
# # for row in S:
# #     if S[0] == "<":
# #         print(S.prettify())
