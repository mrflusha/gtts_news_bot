from gtts import gTTS
from time import sleep
import parse
from playsound import playsound

from datetime import datetime
from time import sleep


import time
import google.cloud.texttospeech as tts




#tts = gTTS(text='МОСКВА, 1 апр - РИА Новости. Президент России Владимир Путин проведет в пятницу оперативное совещание с постоянными членами Совбеза РФ, а также международные телефонные разговоры, в том числе с турецким лидером Тайипом Эрдоганом, сообщил журналистам пресс-секретарь главы государства Дмитрий Песков.\"Сегодня у Путина несколько международных телефонных разговоров, продолжает диалог. Один из них будет разговор с Эрдоганом, мы это подтверждаем. Сообщение дадим... В середине дня президент планирует провести оперативное совещание с членами Совбеза\", - сказал Песков журналистам.', lang='ru')
#tts.save("good.mp3")
#playsound('good.mp3')
class Speaker:
	def __init__ (self, speaker = 'aidar',):
		self.lang = 'ru'
		self.model = 'ru_v3'
		self.sample_rate = '24000'
		self.speaker = speaker
		self.put_accent = True 
		self.device = torch.device('cpu')
		self.model, self._ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)


class News:
	news_list = list()
	def __init__ (self, title, link, full_text, resource = 'ria'):
		self.resource = resource
		self.title = title 
		self.link = link
		self.full_text = full_text
		self.news_list.append(self)


	def get_full_text(self):
		return self.full_text


text_list = ['И вот мы сидим сдесь, как два вайтишника, вайтишно сидим.',
'Ты баги то фиксишь? -фикшу! ',
'Братишка, братишка просыпайся. :censored: всё положили, rm -rf \/написали :censored:'
, 'Вот это таска, вот это да. '
,
'Снимаем логи... -стоит у меня дебаг бридж, стоит. '
,
'Один отчёт :censored: другого'
,
'Где он критикал то? Где он критикал... '
,
'-я тимлид пойдём на митап'
,
'Натестировали :censored:']

now = datetime.now()

current_time = now.strftime("%H:%M")

time_to_parse = "23:00"

'''

test = parse.get_full_text("https://realty.ria.ru/20220621/putin-1797051961.html")
print(test)

tts = gTTS(text = test, lang='ru')
tts.save("путлер.mp3")
playsound("путлер.mp3")
sleep(20)
'''
test = parse.get_docs()

for i, arr in enumerate(test):
	print(type(arr))


	sleep(30)
	full_text = parse.get_full_text(arr[1])
	News(arr[0],arr[1],full_text)
	print(i,News.news_list[i].title,News.news_list[i].link,News.news_list[i].full_text, sep = '\t')

	tts = gTTS(text = full_text, lang = 'ru')
	tts.save(f"ria{i}.mp3")
	playsound(f"ria{i}.mp3")

	#tts = gTTS(text = arr[0], lang='ru')

	#tts.save("new_"+str(i)+".mp3")
	#playsound("new_"+str(i)+".mp3")


	