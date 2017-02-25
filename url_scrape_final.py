from bs4 import BeautifulSoup
import csv
import requests
from time import sleep

r  = requests.get("http://www.famousquotesandauthors.com/quotes_by_topic.html")

data = r.content

soup = BeautifulSoup(data,'html5lib')

#finddiv = soup.find('table',attrs = {"cellpadding:0; cellspacing:0; align:center; width:95%"})

finddiv = soup.find_all('td', attrs={'width':'36%'})

urllinks =[]

for links in finddiv:
    l = links.find_all("a")
    urls = [x.get("href") for x in l]
    for i in range(len(urls)):
        urllinks.append(urls[i])
    print len(urls)
    
finddiv2 = soup.find_all('td', attrs={'xwidth':'33%'})

for links2 in finddiv2:
    l2 = links2.find_all("a")
    urls2 = [x2.get("href") for x2 in l2]
    for j in range(len(urls)):
        urllinks.append(urls[j])
    print len(urls)

print "total_no_of_urls :", len(urllinks)


URL2 = "http://www.famousquotesandauthors.com"

quotes=[]  # a list to store quotes

csvfile = "quotes.csv"

curr =743
for ul in urllinks[743:]:
    r2 = requests.get(URL2 + ul)
    soup2 = BeautifulSoup(r2.content, 'html5lib')
    winner = [div.string for div in soup2.find_all('div', style = {"font-size:12px;font-family:Arial;"})]
    print "Done topic" , curr,"/861"
    #for k in range(len(winner)):
        #quotes.append(winner[k])
    print "moving to csv"
    with open(csvfile, "a") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in winner:
            writer.writerow([val]) 
    curr+=1
    sleep(1)


#print "ready to move to csv file now !!"




    
    
  
    
