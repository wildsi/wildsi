import sys
from datetime import date
import requests
import json

#Get date from database
db_date = sys.argv[1]
#date from database has \r\n. Must be removed otherwise it won't work
db_date = db_date.rstrip("\r\n") 
print ("Argument: ", db_date)

#current_date
today = str(date.today())
print(today)

f = open("ena_data.dat","w")
url="https://www.ebi.ac.uk/ena/portal/api/search?result=sequence&query=country=%22*%22%20AND%20(first_public>"+db_date+"%20AND%20first_public<"+today+")%20+OR%20(last_updated>"+db_date+"%20AND%20last_updated<"+today+")&fields=pubmed_id,doi,country,first_public,last_updated,location,scientific_name,tax_id,tax_division&limit=0&format=json"
data = requests.get(url)
if data.status_code == 204:
    print('No Data')
else:
    result = data.json()
    for i, hit in enumerate(result):
        subset = result[i]
        accession = subset['accession']
        pmid = subset['pubmed_id']
        doi = subset['doi']
        pmcid = ''
        origin = subset['country']
        if ':' in origin:
            x = origin.split(":")
            country = x[0]
        else:
            country = origin
        first_created = subset['first_public']
        submission_date = subset['last_updated']
        location = subset['location']
        name = subset['scientific_name']
        taxid = subset['tax_id']
        division = subset['tax_division']
        #print('\t'.join([accession,pmid,pmcid,doi,origin,country,first_created,submission_date,location,name,taxid,division])+"\n")
        f.write('\t'.join([accession,pmid,pmcid,doi,origin,country,first_created,submission_date,location,name,taxid,division])+"\n")
    
f.close()