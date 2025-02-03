from requests_html import HTMLSession

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
} #To mask from getting caught webscraping.

url = 'https://catalog.iit.edu/courses/' #URL of your target site

s = HTMLSession() #for dynamic web scraping
r = s.get(url)

r.html.render(sleep=1) #it renders the web scrapper using chromium

for ul in r.html.find('#atozindex ul'):
    for item in ul.absolute_links:
        r = s.get(item)
        print(r.html.find('h1.page-title', first=True).text)




# for i in range(1, 16):
#     products = r.html.xpath(f'//*[@id="atozindex"]/ul[{i}]', first = True)


#     for item in products.absolute_links:
#         r = s.get(item)
#         print(r.html.find('h1.page-title', first = True).text)


# products = r.html.xpath(f'//*[@id="atozindex"]/ul[{3}]', first = True)
# for item in products.absolute_links:
#     r = s.get(item)
#     print(r.html.find('h1.page-title', first = True).text)


