from bs4 import BeautifulSoup
import requests


def get_allsubdomains(domain):

	url  = "https://rapiddns.io/subdomain/{}?full=1#result".format(domain)
	
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')

	
	output_rows = []
	website_table = soup.find("table",{"class":"table table-striped table-bordered"})
	website_table_items = website_table.find_all('tr')

	for rows in website_table_items:
		d = rows.find_all('td', limit=1)

		with open('sub.txt', 'a') as file:
			for i in d:
				file.write(i.text+'\n')