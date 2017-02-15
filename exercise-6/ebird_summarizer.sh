#! /bin/bash
# the next line will create a new file called formatted_eBird_data.csv
inClass_replace_newlines.sh eBird_Taxonomy_v2016_9Aug2016.csv
# the next line will replace all extra commas and will replace the contents of formatted_eBird_data.csv
sed 's/,\s/ /g' formatted_eBird_Taxonomy_v2016_9Aug2016.csv > formatted_eBird_Taxonomy_v2016_9Aug2016.csv

python name_fav.py aa bb
