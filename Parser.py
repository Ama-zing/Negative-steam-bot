import requests
from bs4 import BeautifulSoup
print('Введите свой id стим')
id = input()
page = requests.get('https://convars.com/csgostats/ru/' + id)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'html.parser')
a = soup.select("#round11 > div:nth-child(5)")
text = str(a)
textend = []
i = text.find("<")
while i != (-1):
    i = text.find('''fff;">''')
    text = text[(i+6):]
    i = text.find("<")
    textend.append(text[0:i])
    i = text.find('''fff;">''')
print("Твоя статистика: \n Убийств:", textend[0], '\n Смертей:', textend[1], '\n Матчей:', textend[2], "\n Раунды:" , textend[3], "\n Время:", textend[4], '\n KD = ', round(int(textend[0])/int(textend[1]), 2) )
