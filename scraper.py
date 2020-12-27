from bs4 import BeautifulSoup
import pandas
import requests
import re

		

class Scrape:
	def __init__(self):
		#menyiapkan array kosong untuk menyimpan data
		self.array  = []
		self.url = input("masukan alamat website yang ingin di scrap : ")
		self.one_page()
				
	def one_page(self):
		try:
			self.get = requests.get("https://"+self.url)
			print("status url "+self.get.status_code+" ok")
			self.content = BeautifulSoup(self.get.content, "html.parser")
		except:
			print("conneting error")
			Scrape()
		
		print("pilih html yang ingin di ambil")
		print("[1] Alamat link")
		print("[2] String")
		
		sp = input("masukan pilihan : ")
		if(str(sp) == "1"):
			self.find_link()
		elif(str(sp) == "2"):
			self.find_string()
		else:
			print("menu salah")
	
	def find_link(self):
		self.cls = input("masukan attr class : ")
		print("==== masukan base url link agar pencarian lebih akurat =====")
		self.link = input("masukan base url : ")
		
		self.data = self.content.find_all(href=re.compile(str(self.link)), class_=re.compile(str(self.cls)))
		for data in self.data:
			#print(data)
			self.array.append(data["href"])
			
		self.dataframe()
			
	def find_string(self):
		self.tag = input("masukan tag html : ")
		self.cls = input("masukan attr class : ")
		
		self.data = self.content.find_all(str(self.tag) , class_=re.compile(str(self.cls)))
		for data in self.data:
			#print(data)
			self.array.append(data.text)
			
		self.dataframe()

	def dataframe(self):
		data_array = {"Scrape data" : self.array}
		self.df = pandas.DataFrame(data_array)
		print(self.df)	

		
Scrape()

