#Python script to get a list of the commands to pull each gene feature from the API

import json
import glob

features_per_gene_from_API = "https://genomevolution.org/coge/api/v1/features/"
list_command_file = open("list_of_commands.txt", 'w')

for api_file in glob.glob("*.json"):
	if api_file.endswith('json'):	
		with open(api_file) as data_file:
			data = json.load(data_file)
			data_features = data["features"]
			for feature in data_features:
				coge_gene_id = feature["id"]
				command_for_shell = features_per_gene_from_API + str(coge_gene_id)
				list_command_file.write(command_for_shell+'\n')
	    		
list_command_file.close()
