from bs4 import BeautifulSoup
import requests

def delN(s):
    s = s.replace('\n\n','\n')
    s = s.replace('\n\n','\n')
    s = s.replace('\n\n','\n')
    return s

def parse(f):
    url = 'https://omgtu.ru/general_information/faculties/' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', id ="pagecontent") # находим  контейнер с нужным id
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег
            description = data.text # записываем в переменную содержание тега
    
    description = delN(description)
    
    result = description.split(sep = '\n')
    for i in range(len(result)):
        if i == 1 or i == len(result)-3:
            result[i] = ''
    result = "\n".join(result)
    
    result = delN(result)

    print(result,file = f)  #,file = f