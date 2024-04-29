from bs4 import BeautifulSoup
import requests

def delN(s):
    s = s.replace('\n\n','\n')
    s = s.replace('\n\n','\n')
    s = s.replace('\n\n','\n')
    return s

def parse(f):
    url = 'https://omgtu.ru/general_information/faculties/' 
    page = requests.get(url) 
    print(page.status_code) 
    soup = BeautifulSoup(page.text, "html.parser") 

    block = soup.findAll('div', id ="pagecontent")
    description = ''
    for data in block
        if data.find('a'): 
            description = data.text 
    
    description = delN(description)
    
    result = description.split(sep = '\n')
    for i in range(len(result)):
        if i == 1 or i == len(result)-3:
            result[i] = ''
    result = "\n".join(result)
    
    result = delN(result)

    print(result,file = f)
