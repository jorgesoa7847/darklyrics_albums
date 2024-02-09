#!/usr/bin/env python
# coding: utf-8

# In[593]:


import requests
from bs4 import BeautifulSoup
import re
from functools import reduce


# In[594]:


Letra_abecedario=input("Escoga la letra del artista que guste: ")


# In[595]:


url='http://www.darklyrics.com/'+f'{Letra_abecedario.casefold()}'+'.html'
result=requests.get(url)
content=result.text
soup=BeautifulSoup(content,'lxml')
box=soup.find('div',class_='cont')


# In[596]:


box_fr=box.find('div',class_='artists fr')
box_f1=box.find('div',class_='artists fl')
artistas_fr=[]
for i in box_fr:
    artistas_fr.append(i.text)
artistas_f1=[]
for i in box_f1:
    artistas_f1.append(i.text)
artistas_fr=[i for i in artistas_fr if i.startswith(Letra_abecedario.upper())]
artistas_f1=[i for i in artistas_f1 if i.startswith(Letra_abecedario.upper())]
artistas=artistas_fr+artistas_f1
artistas=[f"{artistas.index(i)+1}--{i}" for i in artistas]


# In[597]:


for i in artistas:
    print(i)
eleccion_1=int(input(f'Choose the number of artist: ' ))


# In[598]:


artista_seleccionado=artistas[eleccion_1-1].split("--")[1].casefold()
artista_seleccionado=reduce(lambda x, y: x + y, re.findall('[A-Za-z]',artista_seleccionado))


# In[599]:


sitio_web_letras=f'http://www.darklyrics.com/{Letra_abecedario}/'+f'{artista_seleccionado}'+'.html'
result=requests.get(sitio_web_letras)
content=result.text
soup=BeautifulSoup(content,'lxml')
discos=soup.find_all('h2')
discos_=[]
for i in discos:
    discos_.append(i.text)


# In[600]:


albums=[re.findall('\"(.+)\" ',i)[0] for i in discos_]
albums=[f'{albums.index(i)+1}--{i}' for i in albums]


# In[601]:


for i in albums:
    print(i)
album_escogido=int(input("Escoge un album por numero: "))


# In[602]:


albums[album_escogido-1]
album_s=albums[album_escogido-1].split("--")[1].casefold().replace(' ','')
album_s=reduce(lambda x, y: x + y, re.findall('[A-Za-z]',album_s))


# In[603]:


sitio_web=f'http://www.darklyrics.com/lyrics/{artista_seleccionado}/{album_s}.html'
result=requests.get(sitio_web)
content=result.text
soup=BeautifulSoup(content,'lxml')
canciones=[]
for item in soup.find('div',class_='albumlyrics').find_all('a',href=True):
    canciones.append(item.text)


# In[604]:


letras=soup.find('div',class_='lyrics').get_text(strip=True,separator=' ')
with open(f'{artista_seleccionado}-{album_s}','w',encoding='utf-8') as file: file.write(letras)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




