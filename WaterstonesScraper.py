from bs4 import BeautifulSoup
    
import requests
headers = {'user-agent': 'my-app/0.0.1'}

def waterstonesScrape(isbn):
    #print 'Starting Ben\'s Amazing Waterstones Scraper!'
    
    url = "https://www.waterstones.com/book/" + isbn
    
    page = requests.get(url, headers=headers)
    if(page.status_code == 404):
        print("404! Skipping ISBN : " + isbn)
    else:
        html_contents = page.text
        soup = BeautifulSoup(html_contents, 'html.parser')
        
        if(soup.find("div", id="scope_book_description")):
            return soup.find("div", id="scope_book_description").text.strip()
        else:
            return

    #print('Finished Ben\'s Amazing Waterstones Scraper!')

#synopsis = waterstonesScrape("9780091816971")
#print(synopsis)

#404 test
#print(waterstonesScrape("9788126506750"))