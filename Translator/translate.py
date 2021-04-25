import speech_recognition as sr # импорт нужных библиотек
from textblob import TextBlob

r = sr.Recognizer() 

mic = sr.Microphone(device_index=14) # индекс микрофона

voice = 1 # переменная для запуска программы

while voice == 1: # пока voice = 1
	with mic as source: # прослушивание фона
		print('Скажите что - нибудь, чтобы перевести текст на английский')
		audio = r.listen(source)

	query = r.recognize_google(audio, language = "ru-Ru") # запись полученного текста в переменную, где language - язык ввода
	print(query.lower()) # печать русского текста 
	blob = TextBlob(query) # перевод полученного текста
	print(blob.translate(to='en')) # печать переведенного текста (параметр 'en' можно именить на другой язык)

	with mic as source: # получение ключевого слова
		print('Скажите ключевое слово')
		audio = r.listen(source)

	z = r.recognize_google(audio, language="ru-Ru") # запись слова в переменную z
	print(z.lower()) # печать полученного слова

	if z == 'переведи': # если z = 'переведи'
		voice = 1 # присвоить voice 1
	if z == 'хватит': # если z = 'хватит'
		voice = 0 # присвоить voice 0
	if voice == 0: # если voice = 0
			break # выйти из цикла и завершить программу