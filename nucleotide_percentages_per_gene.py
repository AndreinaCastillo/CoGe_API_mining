#Python script that changes each string to the original dictionary and parses the gene name/ncbi_id and the corresponding nucleotide percentages into a txt file

# import os
# import fileinput
# import ast
# 
# file_name = 'gene_by_gene_features.txt'
# source = fileinput.FileInput(os.path.expanduser(file_name))
# 
# def features_per_gene(source):
#     nucleotide_percentages_per_gene = open("nucleotide_percetages_per_gene.txt", 'w')
#     nucleotide_percentages_per_gene.write("gene_name\t"+"wobble_gc_content\t"+"wobble_at_content\t"+"wobble_nx_content\n")
# 
#     for gene_features in source:
#         strip_gene_features = gene_features.strip()
#         dictionary_gene_features = ast.literal_eval(strip_gene_features)
#         gene_name = dictionary_gene_features["names"]
#         gene_percentages_gc = dictionary_gene_features["wobble"]["gc"]
#         gene_percentages_at = dictionary_gene_features["wobble"]["at"]
#         gene_percentages_nx = dictionary_gene_features["wobble"]["nx"]
#         nucleotide_percentages_per_gene.write(str(gene_name[0])+"\t")
#         nucleotide_percentages_per_gene.write(str(gene_percentages_gc)+"\t")
#         nucleotide_percentages_per_gene.write(str(gene_percentages_at)+"\t")
#         nucleotide_percentages_per_gene.write(str(gene_percentages_nx)+"\n")
# 
#     nucleotide_percentages_per_gene.close()
# 
# features_per_gene(source)

import os
import fileinput
import ast

file_name = 'gene_by_gene_features.txt'
source = fileinput.FileInput(os.path.expanduser(file_name))

def features_per_gene(source):
    nucleotide_percentages_per_gene = open("nucleotide_percetages_per_gene.txt", 'w')
    nucleotide_percentages_per_gene.write("gene_name\t"+"gc_content\t"+"at_content\t"+"nx_content\n")

    for gene_features in source:
        strip_gene_features = gene_features.strip()
        dictionary_gene_features = ast.literal_eval(strip_gene_features)
        gene_name = dictionary_gene_features["names"]
        gene_percentages_gc = dictionary_gene_features["percentages"]["gc"]
        gene_percentages_at = dictionary_gene_features["percentages"]["at"]
        gene_percentages_nx = dictionary_gene_features["percentages"]["nx"]
        nucleotide_percentages_per_gene.write(str(gene_name[0])+"\t")
        nucleotide_percentages_per_gene.write(str(gene_percentages_gc)+"\t")
        nucleotide_percentages_per_gene.write(str(gene_percentages_at)+"\t")
        nucleotide_percentages_per_gene.write(str(gene_percentages_nx)+"\n")

    nucleotide_percentages_per_gene.close()

features_per_gene(source)