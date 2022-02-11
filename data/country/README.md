# Notes on country files
This folder contains three files:
* country.csv -- a table that can be ingested into the SQL database with a list of observed country names, iso codes and simplified names. Simplified country names were obtained from data provided at https://github.com/mledoze/countries and compliant to [ISO Standard 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1)
* countries.json -- a copy of the data downloaded from https://github.com/mledoze/countries. Note this is distributed under the ODbL-1.0 License
* add-common-country-names.pl -- a perl script that allows one to reproducibly update common names

## Important to note:

* Territories, historical nations and de facto states are mapped to an official UN member state when possible (unMember=true in the countries.json file). Only data from UN member states are shown in the final web portal. Certain historical countries that have broken up are considered unresolvable (USSR, Borneo). Data associated with such country names are not mapped to other countries and are not shown in the web portal.
