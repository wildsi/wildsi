import requests
import json

f = open("ena_data_complete.txt","w")
url="https://www.ebi.ac.uk/ena/portal/api/search?result=sequence&query=country=%22*%22%20AND%20first_public>=2020-04-01 OR last_updated>=2020-04-01&fields=pubmed_id,doi,country,first_public,last_updated,location,scientific_name,tax_id,tax_division&limit=0&format=json"
data = requests.get(url)
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