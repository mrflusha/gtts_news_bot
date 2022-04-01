from bs4 import BeautifulSoup
import requests

url = ("https://ria.ru/")

page = requests.get(url)

print(page.status_code)
def get_docs():
	
	try:

		if page.status_code == 200:
			filterNews = list()
			allNews = list()
			soup = BeautifulSoup(page.text, "html.parser")
			allNews = soup.findAll('a', class_='cell-list__item-link')
			photoNews = soup.findAll('a', class_='cell-main-photo__link')

			print(photoNews)
			#print(allNews[1])
			for data in allNews:		
				if data.find('span') is not None:
					temp_list = [data.text.strip("\"\'\/\#") ,data['href']]
					filterNews.append(temp_list)
			print(temp_list)

			for data in photoNews:
				if data.find('span') is not None:
					temp_list = [data.text.strip("\"\'\/\#") ,data['href']]
					filterNews.append(temp_list)
			print(temp_list)
	#				if data.has_attr('href'):
	#					print(data['href'])
					#print(data.find("href"))

			return filterNews
		else:
			print(f"error connect to site,\n site return {page.status_code}")
		
	except Exception as e:
		print(e)


#test = get_docs()

#for text, link in test:
#	print(f"text = {text}\n link = {link}\n\n")