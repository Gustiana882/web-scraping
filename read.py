import pandas as pd

file = pd.read_csv("test1.csv")
url = file["Image"]
i=0
Image = []
Title = []
Sku = []
link = []
while (i < len(url)):
	Sku.append(file.loc[i]["sku"])
	Title.append(file.loc[i]["Title"])
	link.append(file.loc[i]["Link"])
	Image.append(file.loc[i]["Image"].replace("u'","'"))
	
	data= {"SKU" : Sku , "Title":Title , "link":link , "Url_Image":Image}
	df = pd.DataFrame(data)
	df.to_excel("data.xlsx")
	
	
	i+=1
