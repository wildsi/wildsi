# Notes on Treaty Annex1 files
This folder contains two files:
* mapping_TREATY_ANNEX1_to_NCBI_GENUS.csv -- a table that maps the [Treaty Annex1](https://www.fao.org/plant-treaty/areas-of-work/the-multilateral-system/annex1/en/) to [NCBI taxonomy database](https://www.ncbi.nlm.nih.gov/Taxonomy/). The initial version was conducted by map by shared genus name.
* subtaxa_for_TREATY_ANNEX1_in_NCBI.cvs -- expand all NCBI subtaxa for a Annex1 genus. The initial version was conducted by a hierarchical data retrieval. This list is under curation to match the [Treaty Annex1](https://www.fao.org/plant-treaty/areas-of-work/the-multilateral-system/annex1/en/) agreed exclusion and inclusion rules.

# Methods description:

## Mapping of annex 1 plants to the NCBI taxonomy

Annex I of the International Treaty on Plant Genetic Resources for Food and Agriculture includes a list of crop and forage plants that are specifically covered by the treaty.1 This list consists of a table of plant names and their associated taxonomic genera, along with additional notes that may limit scope to, or exclude, certain species or taxonomic subgroups within each genera. We have mapped this table to the NCBI Taxonomy,2 in order to accommodate automated searching and filtering of sequence records relevant to Annex I. 

A spreadsheet describing our mapping is available as File X. The first column lists genera relevant to Annex I. The second column lists the NCBI Taxonomy ID (TxID) of the genus. The third columns lists “Observations” or “Species” from the Annex I list, which are generally intended to limit scope to, or exclude, certain species or taxonomic subgroups with each genera. The fourth and fifth columns list specific TxIDs relevant to these exclusion or inclusion rules, respectively. Each genus will have TxIDs in at most one of these two columns. If both columns are empty, all species in the genus are presumed included. When specific species are included or excluded, all child subspecies are presumed to also be included or excluded. The last column includes notes that help explain certain curation decisions.

Conflicts and ambiguities were resolved as follows. If a species mentioned in Annex I was included in a different genus in the NCBI Taxonomy, this genus was added to the table. If these differences left a genus in Annex I with no relevant species, the genus name was retained in the table, but “NA” was listed as the genus TxID. When additional genera were mentioned in the “Observations”, these were added as separate rows, and the whole genus was presumed to be included unless otherwise stated. Genera that are mentioned more than once were merged into a single row. Within Solanum, prior publications were used to determine which species fall under Tuberosa and Melongena.3,4 Additional information on these taxonomic groups are provided in separate worksheets. 

In order to be able to assign DSI records from databases, which are assigned to species via the NCBI taxonmy ID, to ANNEX1 plants, all subspecies were listed as a flat table in File Y, taking into account the inclusion and exclusion rules mentioned above. For this purpose, the tree structure was traversed from the genus node, expanded, the exclusion list excluded and the inclusion list added. For this purpose, the NCBI Taxonomy was used as a database dump5 as of December 2021.
References

1. Annex I: List of crops covered under the Multilateral System | International Treaty on Plant Genetic Resources for Food and Agriculture | Food and Agriculture Organization of the United Nations. https://www.fao.org/plant-treaty/areas-of-work/the-multilateral-system/annex1/en/.
2. Schoch, C. L. et al. NCBI Taxonomy: a comprehensive update on curation, resources and tools. Database 2020, baaa062 (2020).
3. Hijmans, R. J., Spooner, D. M., Salas, A. R., Guarino, L. & de la Cruz, J. Atlas of wild potatoes. (IPGRI, 2002).
4. Furini, A. & Wunder, J. Analysis of eggplant (Solanum melongena)-related germplasm: morphological and AFLP data contribute to phylogenetic interpretations and germplasm utilization. Theor. Appl. Genet. 108, 197–208 (2004).
5. Conrad L Schoch, Stacy Ciufo, Mikhail Domrachev, Carol L Hotton, Sivakumar Kannan, Rogneda Khovanskaya, Detlef Leipe, Richard Mcveigh, Kathleen O’Neill, Barbara Robbertse, Shobha Sharma, Vladimir Soussov, John P Sullivan, Lu Sun, Seán Turner, Ilene Karsch-Mizrachi, NCBI Taxonomy: a comprehensive update on curation, resources and tools, Database, Volume 2020, 2020, baaa062, https://doi.org/10.1093/database/baaa062

## Important to note:

* This files are created by manual, expert supervised mapping Treaty Annex 1 plants by Genus name to related node in [NCBI taxonomy database](https://www.ncbi.nlm.nih.gov/Taxonomy/)