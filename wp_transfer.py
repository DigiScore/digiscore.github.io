import requests
from bs4 import BeautifulSoup

orig_url = 'https://digiscore.dmu.ac.uk/wp-json/wp/v2/posts?order=asc'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
blog_json = requests.get(orig_url, headers=headers).json()
path_to_images = "assets/img"
path_to_save = "_posts"


def get_cat_banner_image(categories):
    if categories == 30:
        return "Theory", f"{path_to_images}/theory_banner.png"
    elif categories == 31:
        return "Case Study", f"{path_to_images}/case_study_banner.png"
    elif categories == 32:
        return "Digital Musicianship", f"{path_to_images}/digi_mus_banner.png"
    elif categories == 33:
        return "Outputs", f"{path_to_images}/outputs_banner.png"
    elif categories == 34:
        return "Trans-disciplinary Insights", f"{path_to_images}/tdi_banner.jpg"
    elif categories == 36:
        return "Impact", f"{path_to_images}/impact_banner.png"
    else:
        return None, None


print(len(blog_json))
# print(blog_json)
blog_json = requests.get(orig_url, headers=headers).json()
for blog in blog_json:
    entry = blog
    list(entry.keys())

    entry_date = entry['date_gmt']
    entry_title = entry['title']['rendered']
    entry_content = entry['content']['rendered']
    categories = entry['categories']
    cat_text, cat_banner = get_cat_banner_image(categories)
    # entry_text = BeautifulSoup(entry_content).get_text()
    print(entry_date[:10], entry_title, categories) #, entry_content)

    entry_title_snakey = entry_title.replace(" ", "_")

    title = f"{entry_date[:10]}-{entry_title_snakey}.md"
    print(title)

    header = "---\n" \
             "layout: post\n" \
             f"title: {entry_title}\n" \
             f"categories: {categories}"\
             f"share-img: {cat_banner:}"\
             f"cover-img: {cat_banner}"\
             "---"

    # make the md doc
    f = open(f"{path_to_save}/{title}", "w")
    f.write(header)
    f.write(entry_content)
    f.close()



    # link_to_image = f"{path_to_images}/{entry_date[:5]}/{entry_date[5:8]}"




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
