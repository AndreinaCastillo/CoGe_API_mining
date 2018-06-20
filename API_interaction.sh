#!/usr/bash 

# This will get a file including a list of features for a given genome. In this case, it is getting a list of genes and SOME of their attributes
# echo -X GET https://genomevolution.org/coge/api/v1/genomes/2460/features/gene/

echo "Please, enter coge's genome id"

read varname

curl -X GET https://genomevolution.org/coge/api/v1/genomes/$varname/features/gene/ > genome_"$varname"_OUT.json

# Python script to get a list of the commands to pull each gene feature from the API
python coge_genes_ids.py

# Run each line on the file as a command and place all outputs (features per gene) in the same file
while read -r LINE; do
	curl "$LINE"
	echo
done < list_of_commands.txt > gene_by_gene_features.txt

# Python script that changes each string to the original dictionary and parses the gene name/ncbi_id and the corresponding nucleotide percentages into a txt file
python nucleotide_percentages_per_gene.py

echo "Please, enter a new destination folder (enter a new one per run)"

read varname

mkdir $varname

for i in *.{txt,json}; do
	mv "$i" "$varname"
done;

echo
echo "All output files moved to destination folder"
echo "List of GC, AT, and NX content per gene from input genome in 'nucleotide_percetages_per_gene.txt' file"
echo "Acta est fabula!"