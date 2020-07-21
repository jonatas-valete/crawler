import requests
from bs4 import BeautifulSoup as bs
import threading


DOMINIO = 'https://www.localimoveis.com.br'

def busca(url):
    try:
        r = requests.get(url)
        code = r.status_code
        if code == 200:
            html_doc = r.text
            return html_doc
    except Exception as e:
        print('Erro')
        print(e)

def parser (html_doc):
    parse = bs(html_doc, 'html.parser')
    return parse

def links(anunc_raspar):
    a = anunc_raspar.find('a')
    link = a.get('href')
    return link

def telefone(lin):
    req = requests.get('{}{}'.format(DOMINIO, lin))
    html_doc = req.text
    parse = parser(html_doc)
    a = parse.find('a', class_=('telefone'))
    telefone = a.get('href')
    return telefone

def anuncio():
    anuncio_raspar = anuncios.pop(0)
    link = anuncio_raspar.find('a')
    link2 = links(anuncio_raspar)
    text_title = link.get('title')
    span = anuncio_raspar.find_all('span')
    tipo_preco = span[0].get_text()
    descricao = anuncio_raspar.find_all('div', class_="mInfo")
    desc = []
    for i in descricao:
        texto = i.get_text()
        desc.append(texto)
    fone = telefone(link2)
    desc_anunc = [text_title, tipo_preco, desc, fone]
    salvar(desc_anunc)
    print(desc_anunc)

def anuncios(url):
    html_doc = busca(url)
    soup = parser(html_doc)
    anunc = soup.find_all('div', class_='resultadoBusca')
    anuncios = []
    for i in anunc:
        anuncio = i
        anuncios.append(anuncio)
    return anuncios

def salvar(descri):
    str_sub_desc = ('{};{};{};{};'.format(descri[2][0], descri[2][1], descri[2][2], descri[2][3]))
    str_desc = ('{};{};{};{};\n'.format(descri[0], descri[1], str_sub_desc, descri[3]))
    try:
        with open('anuncios.csv', 'a') as file:
            file.write(str_desc)
    except Exception as e:
        print(e)



if __name__ == '__main__':

        URL = 'https://www.localimoveis.com.br/apartamentos/venda/sp/sao-paulo/1/'
        anuncios = anuncios(URL)
        thread_1 = threading.Thread(target=anuncio)
        thread_2 = threading.Thread(target=anuncio)
        thread_3 = threading.Thread(target=anuncio)
        thread_4 = threading.Thread(target=anuncio)
        thread_5 = threading.Thread(target=anuncio)
        thread_6 = threading.Thread(target=anuncio)
        thread_7 = threading.Thread(target=anuncio)
        thread_8 = threading.Thread(target=anuncio)
        thread_9 = threading.Thread(target=anuncio)
        thread_10 = threading.Thread(target=anuncio)
        thread_11 = threading.Thread(target=anuncio)
        thread_12 = threading.Thread(target=anuncio)
        thread_13 = threading.Thread(target=anuncio)
        thread_14 = threading.Thread(target=anuncio)
        thread_15 = threading.Thread(target=anuncio)
        thread_1.start()
        thread_2.start()
        thread_3.start()
        thread_4.start()
        thread_5.start()
        thread_6.start()
        thread_7.start()
        thread_8.start()
        thread_9.start()
        thread_10.start()
        thread_11.start()
        thread_12.start()
        thread_13.start()
        thread_14.start()
        thread_15.start()






