from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random_word import RandomWords
import time
import random

# Caminho para o WebDriver do Edge
PATH = "D:\\webdriver\\msedgedriver.exe"
service = Service(PATH)

# Inicializa o Edge WebDriver
driver = webdriver.Edge(service=service)

# Acessa o site do Bing
driver.get("https://www.bing.com")

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