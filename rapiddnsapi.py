from bs4 import BeautifulSoup
import requests
import os

# todo

# usar args como => { python3 <nome do script> <dominio> }.
# perguntar ao utilizador se quer que se escreva os subdominios num ficheiro txt.

def get_allsubdomains(domain):

	url  = "https://rapiddns.io/subdomain/{}?full=1#result".format(domain)
	
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')

	
	output_rows = []
	website_table = soup.find("table",{"class":"table table-striped table-bordered"})
	website_table_items = website_table.find_all('tr')

	for rows in website_table_items:
		d = rows.find_all('td', limit=1)

		file_to_write = 'sub.txt'
		
		# checkar se o ficheiro existe para ser apagado e reescrito denovo.

		with open(file_to_write, 'a') as file:
			for i in d:
				file.write(i.text+'\n')


get_allsubdomains('google.com') 