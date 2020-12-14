import pandas as pd
import requests
from bs4 import BeautifulSoup

def conect(index):
	df = pd.read_csv("inventory_export_1.csv")

#new_file = pd.read_csv("test.csv")
#data = {"sku" : [] , "Title" : [], "Link" : [], 	"Image" : []}
#dft = pd.DataFrame(data)
#dft.to_csv("test.csv")
	

	

	id =[]
	title = []
	page = []
	image1 = []

#ambil data satupersatu 3125 3125
	i = int(index)
	while (i < len(df["SKU"])):
		sku = df.loc[i]["SKU"]
	
	
	

#https://www.truebrands.com/catalogsearch/result/?q=7678
#https://www.truebrands.com/chateau-2-bottle-vintage-trunk-wine-box-by-twine.html

		url = requests.get("https://www.truebrands.com/catalogsearch/result/?q="+sku)
		try:
			soup = BeautifulSoup(url.content, "html.parser")
			status = soup.find("div", "notice").text

			print(str(i)+'. '+sku+'Your search returned no results.     ')
			i+=1


		except:
		#print("barang ada")

		#mengambil data html card product
			product = soup.find("a", "product-item-link")
		#mengambil link sesuai sku
			link = product["href"]

			print(str(i)+". "+sku+" link : "+link)

		#masuk ke link detail
			uri = requests.get(str(link))
			parse = BeautifulSoup(uri.content,"html.parser")
			img = parse.find_all("a","mt-thumb-switcher")
	
		
			d=[]
			for g in img:
				d.append(g["href"])
		
		
			id.append(sku)
			title.append(df.loc[i]["Title"])
			page.append(link)
			image1.append(d)
		
			i+=1

			data = {"sku" : id , "Title" : title, "Link" : page , 	"Image" : image1}
			data_new = pd.DataFrame(data)
		
			data_new.to_csv("test.csv")
		



index = 4826
conect(index)