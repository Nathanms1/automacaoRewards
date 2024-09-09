import random
from random_word import RandomWords
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Recupera as credenciais do ambiente
MICROSOFT_EMAIL = os.getenv('MICROSOFT_EMAIL')
MICROSOFT_PASSWORD = os.getenv('MICROSOFT_PASSWORD')

# Caminho para o WebDriver do Edge
# PATH = "D:\\webdriver\\msedgedriver.exe"
PATH = "/usr/local/bin/msedgedriver" 
service = Service(PATH)

# Inicializa o Edge WebDriver
driver = webdriver.Edge(service=service)

# Acessa o site do Bing
driver.get("https://www.bing.com")

# Realiza o login
driver.get("https://login.live.com/")
email_input = driver.find_element(By.NAME, "loginfmt")
email_input.send_keys(MICROSOFT_EMAIL)
email_input.send_keys(Keys.RETURN)
time.sleep(2)
password_input = driver.find_element(By.NAME, "passwd")
password_input.send_keys(MICROSOFT_PASSWORD)
password_input.send_keys(Keys.RETURN)

# Aguarda o login ser realizado
time.sleep(5)

# Inicializa a classe RandomWords
r = RandomWords()

for _ in range(10):  # Faz 10 pesquisas diferentes
    random_word = r.get_random_word()
    # Localiza a barra de pesquisa
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.clear()
    search_bar.send_keys(random_word)
    search_bar.send_keys(Keys.RETURN)
    
    # Espera alguns segundos antes de fazer a próxima pesquisa
    time.sleep(random.randint(3, 7))

# Fecha o navegador
driver.quit()