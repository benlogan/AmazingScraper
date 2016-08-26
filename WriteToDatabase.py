import psycopg2
import sys

def databaseQuery(asin, oauthid, text):

    # Connect to an existing database
    # FIXME source from init script or heroku props?
    dbName = sys.argv[1]
    dbUser = sys.argv[2]
    dbHost = sys.argv[3]
    dbPassword = sys.argv[4]
    
    conn = psycopg2.connect("dbname='" + dbName + "' user='" + dbUser + "' host='" + dbHost + "' password='" + dbPassword + "' sslmode='require'")
    
    # Open a cursor to perform database operations
    cur = conn.cursor()
    
    
    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    cur.execute("INSERT INTO public.\"SummaryText\" (isbn, oauthid, datetime, text) VALUES (%s, %s, %s, %s)",(asin, oauthid, 'now()', text))
    
    # FIXME don't store duplicates (some items will have existed on the top sellers list for a while!)
    
    # Make the changes to the database persistent
    conn.commit()
    
    # Close communication with the database
    cur.close()
    conn.close()
    
#databaseQuery('0751565350', 'test from python')