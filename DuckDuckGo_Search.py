#duckduckgo eng
print('\n\n')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Web master>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

print('Hello There I am webmaster you can ask me any defintion , spellings , history , \n science things and about famous people too..\n \t Kindly put forward your query!!')

print()

import urllib.request
import urllib.parse

from bs4 import BeautifulSoup as soup



def encode(query,**kwargs):
    safesearch = '1' #if safesearch else '-1'
    html = '0' #if html else '1'
    meanings = '0' #if meanings else '1'
    params = {
        'q': query,
        'o': 'json',
        'kp': safesearch,
        'no_redirect': '1',
        'no_html': html,
        'd': meanings,
        }
    params.update(kwargs)
    encparams = urllib.parse.urlencode(params)
    url = 'http://api.duckduckgo.com/?' + encparams
    return(url)

null=None#some json variable are none.. to support it it is present

class Abstract(object):
    def __init__(self, json):
        self.html = json['Abstract']
        self.text = json['AbstractText']
        self.url = json['AbstractURL']
        self.source = json['AbstractSource']

def results(query):
    try:
        re=urllib.request.Request(encode(query),headers={'User-Agent': useragent})
    except:
        re=urllib.request.Request(encode(query))
    response=urllib.request.urlopen(re)
    web_content=(response.read())
    web_content=str(web_content,'utf-8')#coverting bytes to string    
    json=dict(eval(web_content))
    response.close()
    content=Abstract(json)
    if content.text=='':
        print('Sorry I don\'t know')
    else:
        print()
        print(content.text)
        print()
        print('\t\t\tSource:',content.source)
        print('\t\t\tSearch Results powered by DuckDuckGo \n\t\t\t(an opensource search engine) \n ')

while True :
    query=input('Query:')
    if query.lower()=='bye':
        print('Bye Thank You')
        break
    else:
        results(query)
