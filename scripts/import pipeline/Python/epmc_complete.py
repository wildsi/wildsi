import requests
import time
import re
import json
import csv

cursormark = str(1)
i = 0
#f = open("annodata_new.json", "a",encoding="utf-8")
while(cursormark != "0"):
    if i == 0:
        cursormark = str(0)
    url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(ACCESSION_TYPE:gen)&resultType=core&pageSize=500&format=json&cursorMark="+cursormark
    data = requests.get(url)
    cursormark = data.json()['nextCursorMark']
    cursormark = str(cursormark)
    result =data.json()['resultList']['result']
    for i, hit in enumerate(result):
        subset = result[i]
        accession = subset['accession'] if 'accession' in subset else "NA"
        pmid = subset['pmid'] if 'pmid' in subset else "NA"
        _id = subset['id'] if 'id' in subset else "NA"
        source = subset['source'] if 'source' in subset else "NA"  
        isopenaccess = subset['isOpenAccess'] if 'isOpenAccess' in subset else "NA"

        pmcid =subset['pmcid'] if 'pmcid' in subset else "NA"
        doi = subset['doi'] if 'doi' in subset else "NA"
        author = subset["authorList"]["author"] if 'authorList' in subset else "NA"
        affiliation = subset['affiliation'] if 'affiliation' in subset  else "NA"
        fullname = [d['fullName'] if 'fullName' in d  else "NA" for d in author]
        orcid = [d['authorId']['value'] if 'authorId' in d  else "NA" for d in author]
        pubdate = subset['firstPublicationDate'] if 'firstPublicationDate' in subset  else "NA"
        epubdate = subset['electronicPublicationDate'] if 'electronicPublicationDate' in subset  else "NA"
       
        for j,name in enumerate(fullname):
            country=affiliation.split(',')[-1].replace('.','')
            if (re.search(r"(\w+) ([\w.-]+@[\w.-]+.\w+)",country)):
                match=re.search(r"(\w+) ([\w.-]+@[\w.-]+.\w+)",country)
                etat = match.group(1)
            else:
                etat=country
        print("\t".join([_id, source, isopenaccess,  pmid, pmcid, doi, fullname[j], affiliation, etat, pubdate, epubdate, orcid[j]]))
        #complete_string = [_id, source, isopenaccess,  pmid, pmcid, doi, fullname[j], affiliation, etat, pubdate, epubdate, orcid[j]]

        #jsonString = json.dumps(complete_string)
        #f.write(''.join(complete_string)+"\n")
        print(cursormark)
    #print(result)
   
    #f.write(''.join(jsonString+"\n"))
    #f.close()
    i = i+1
    time.sleep(5)
   
#f.close()
