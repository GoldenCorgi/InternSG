import csv
import time
import datetime
import urllib.request
from bs4 import BeautifulSoup as bs

import datetime

now = datetime.datetime.now()

time_now = "{}_{}_{}".format(now.year,now.month,now.day)
# YYYY/M/D
print(time_now)


def urlget(url):
   url_link = url
   fp = urllib.request.urlopen(url_link)
   mybytes = fp.read()
   mystr = mybytes.decode("utf8") #no fucking clue what this 4 lines does but i found it online and it works
   fp.close()
   return mystr

## https://docs.python.org/3/library/csv.html#csv.writer

def WebToCSV(FileName,appendwritechoice,samplelist):
    with open(FileName, appendwritechoice, newline='',encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerows(samplelist)

#'{}, {}, {}'.format('a', 'b', 'c')


def thisisitchief(numberofpages):
    urlofinternship = 'https://www.internsg.com/jobs/go/{}/'.format(numberofpages)
    soup = bs(urlget(urlofinternship), 'html.parser')
    bodytextofST = soup.findAll("div", {"class": "row-job"}) #find all the <p> and </p>
    
    ListOnePage = []
    for p in bodytextofST:
        if "window.__gaTracker" not in p.text:
            if p.text != "":
                AllFiveStringInOne = p.text
                AllFiveStringInOneList = AllFiveStringInOne.split("\n")
                while "" in AllFiveStringInOneList:
                    AllFiveStringInOneList.remove("")
                #print("'{}'".format(p.text))
                a = p.find('a')
                try:
                    AllFiveStringInOneList.append(a['href'])
                except:
                    print('fail')
                #print(AllFiveStringInOneList)
                # The command below checks if AllFiveStringInOneList is NOT EMPTY.
                if AllFiveStringInOneList:
                    AllFiveStringInOneList.append(numberofpages)
        ListOnePage.append(AllFiveStringInOneList)
    ListOnePage = [x for x in ListOnePage if x != []]
    #print(ListOnePage)
    del ListOnePage[0] #Deleting first row
    return ListOnePage

# w for overwrite/a for append
#WebToCSV('eggs.csv','w')
numberpage = 1
FinalList = []
while numberpage < 51:
    try:
        print(numberpage)
        numberpagestr = str(numberpage)
        zz = thisisitchief(numberpagestr)
        for z in zz:
            FinalList.append(z)
        numberpage = numberpage + 1
    except:
        print("SHit")
DocumentName = "ListofInternshipCSV_{}.csv".format(time_now)
WebToCSV(DocumentName,'w',FinalList)
#thisisitchief()

