import json
import glob

print ("Processing File(s) : ")
print glob.glob("data/*.json")

print 'Starting Ben\'s Amazing Scraper!'

for inputFile in glob.glob("data/*.json"):
    #with open('data.json') as data_file:
    with open(inputFile) as data_file:    
        data = json.load(data_file)

    for book in data:
    
        ASIN = book["asin"]
    
        from AmazonScraper import amazonScrape
        amazonSynopsis = amazonScrape(book["url"])
        print("Amazon Synopsis : " + amazonSynopsis[:100] + "...")
        
        from WriteToDatabase import databaseQuery
        #databaseQuery(ASIN, '99991', amazonSynopsis)
        
        from WaterstonesScraper import waterstonesScrape
        try:
            waterstonesSynopsis = waterstonesScrape(book["isbn"])
            if(waterstonesSynopsis):
                print("Waterstones Synopsis : " + waterstonesSynopsis[:100] + "...")
                #databaseQuery(ASIN, '99992', waterstonesSynopsis)
        except KeyError, e:
            print 'I got a KeyError - reason "%s"' % str(e)
        
        #print('one loop iteration finished!')
    
print('Finished Ben\'s Amazing Scraper!')