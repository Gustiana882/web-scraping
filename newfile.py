import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

def conect(url, index):
	try:
		result = requests.get(str(url)+str(index))
		return result
	except:
		time.sleep(1.5)
		return "conecting..."


def Dataframe(ex_file , path):
	try:
		if(int(ex_file) == 1):
			df = pd.read_csv(path)
		elif(int(ex_file) == 2):
			df = pd.read_excel(path)
		else:
			df = "extensi file yang anda pilih salah"
		return df
	except:
		print("file tidak ditemukan")
	
	
def html_content(index, conect):
	try:
		soup = BeautifulSoup(conect.content, "html.parser")
		element  = soup.find("div" , "notice").text
		return str(index)+'. Your search returned no results.     '
	except:
		try:
		#mengambil data html card product
			product = soup.find("a", "product-item-link")
		#mengambil link sesuai sku
			link = product["href"]

			print(str(index)+". "+sku+" link : "+link)

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
		
		

			data = {"sku" : id , "Title" : title, "Link" : page , 	"Image" : image1}
			data_new = pd.DataFrame(data)
			return data_new
		except:
			return "disconec"
		
			#data_new.to_csv("test.csv")




print("Jenis File")
print("[1] .csv")
print("[2] .excel")
ex_file = input("pilih jenis file : ")
path     = input("masukan lokasi file : ")
url 		= input("masukan url target : ")


#start looping
i =0
file = Dataframe(ex_file, path)

while(True):
	index = file.loc[i]["SKU"]
	if(conect(url, index) =="conecting..."):
		print(conect(url, index))
	else:
		conect(url,index)
		d = html_content(i, conect(url,index))
		print(d)
		if(d == "disconec"):
			i -=1
		else:
			i +=1
	