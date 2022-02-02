load data into table tmp_sqlldr_test
append
fields terminated by "\t"
TRAILING NULLCOLS
(
accession,
primary_pmid,
primary_doi,
primary_pmcid,
origin,
country,
submission_date,
first_created,
lat_lon,
organism,
taxid,
code
)
