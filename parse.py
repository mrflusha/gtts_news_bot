from bs4 import BeautifulSoup
import requests

url = ("https://ria.ru/")
user_agent = {"User-Agent": "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5"}
page = requests.get(url, headers=user_agent)

print(page.status_code)
def get_docs():
	
	try:

		if page.status_code == 200:
			filterNews = list()
			allNews = list()
			soup = BeautifulSoup(page.text, "html.parser")
			allNews = soup.findAll('a', class_='cell-list__item-link')
			photoNews = soup.findAll('a', class_='cell-main-photo__link')

			#print(photoNews)
			#print(allNews[1])
			for data in allNews:		
				if data.find('span') is not None:
					temp_list = [data.text.strip("\"\'\/\#") ,data['href']]
					filterNews.append(temp_list)
			#print(temp_list)

			for data in photoNews:
				if data.find('span') is not None:
					temp_list = [data.text.strip("\"\'\/\#") ,data['href']]
					filterNews.append(temp_list)
			#print(temp_list)
	#				if data.has_attr('href'):
	#					print(data['href'])
					#print(data.find("href"))

			return filterNews
		else:
			print(f"error connect to site,\n site return {page.status_code}")
		
	except Exception as e:
		print(e)

def get_full_text(link):
	tts = requests.get(link, headers=user_agent)
	if page.status_code == 200:
			tts_list = list()
			soup = BeautifulSoup(tts.text, "html.parser")
			html_tts = soup.findAll('div',class_='article__text')
			
			for data in html_tts:
				tts_list.append(data.text)
			
			tts = " ".join(map(str,tts_list))
			return tts

	else:
		print(f"error connect to site,\n site return {page.status_code}")




	return text_to_speech
	
#test = get_docs()

#for text, link in test:
#	print(f"text = {text}\n link = {link}\n\n")
