#Use libraries as "BeautifulSoup" used to analyze and extract data of webpages
# and "Requests" to make HTTP requests finding content of webpages.
# I'm using  the module "zipfile" to work with zip archives and OS trying to interact with
# the operational system.

import requests
from bs4 import BeautifulSoup
import zipfile
import os

#Implementation to acces the website and realize the download of  files
def web_scrape(link):
  #Making syntax most correct possible
  response = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-dasociedade/atualizacao-do-rol-de-procedimentos')
  #print(response.text) #Receiving the content of webpage
  soup = BeautifulSoup(response.text, 'html.parser')
  
def compress_files( files_list, output_name):
  with zipfile.ZipFile(output_name, 'w') as zipf:
      for file in files_list:
          zipf.write(file)
