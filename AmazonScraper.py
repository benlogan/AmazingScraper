from bs4 import BeautifulSoup
    
import requests
import re
import urllib2

headers = {'user-agent': 'my-app/0.0.1'}

def amazonScrape(url):
        #url = "http://www.amazon.co.uk/Nineteen-Eighty-Four-Penguin-Modern-Classics/dp/014118776X"
        #url = "http://www.amazon.co.uk/Invisible-Man-Penguin-Classics/dp/014143998X"
        #url = "http://www.amazon.co.uk/Harry-Potter-Cursed-Child-Production/dp/0751565350%3FSubscriptionId%3DAKIAIEAGKZ56ICR56CMQ%26tag%3Dwell044-21%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D0751565350"
        
        page = requests.get(url, headers=headers)
        html_contents = page.text
        soup = BeautifulSoup(html_contents, 'html.parser')
        
        #print(soup)
        #print(soup.get_text())
        #print(soup.p)
        
        # kindle books appear to use ASIN.O for some reason, normally its just ASIN
        # ASIN = soup.find("input", {"name" : re.compile('ASIN(.\d)?')})['value']
        # why am I doing this! I can get it from the original data!
        # ASIN = book["asin"]
        
        #hiddenInputAsin = soup.find("input", id="ASIN")
        #if hiddenInputAsin is None:
        #    hiddenInputAsin = soup.find("input", id="ASIN.0")
        #ASIN = hiddenInputAsin['value']
        
        scriptText = ''
        for s in soup.find_all('script'):
            scriptText += s.getText()
        
        #print(scriptText)
        #then look for value of bookDescEncodedData
    
        p = re.compile('bookDescEncodedData = "(.*?)",')
        m = p.search(scriptText)
        
        #print(m.group(0))
        bookDescription = m.group(1)
        #print(bookDescription)
        
        return urllib2.unquote(bookDescription).decode("utf-8", "strict")
        
        #save to disk, using the ASIN as the file name...
        #outputfile = open('output/' + ASIN + '.html', 'w')
        #outputfile.write(decodedBookDescription)
        #outputfile.close()