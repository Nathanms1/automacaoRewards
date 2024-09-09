from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
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

# Acessa o site do Bing Rewards
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

# Acessa o site do Bing Rewards
driver.get("https://rewards.bing.com/")

# Aguarda a página carregar completamente
time.sleep(5)  # Você pode ajustar esse tempo de acordo com a velocidade de sua conexão

# Localiza as ofertas na página inicial do Rewards
offers = driver.find_elements(By.CSS_SELECTOR, ".ds-card-sec")  # Ajuste o seletor CSS conforme necessário

# Clica em cada oferta
for offer in offers:
    try:
        offer.click()  # Clica na oferta
        time.sleep(2)  # Espera 2 segundos entre os cliques
        driver.switch_to.window(driver.window_handles[1])  # Muda para a nova aba aberta
        driver.close()  # Fecha a aba
        driver.switch_to.window(driver.window_handles[0])  # Volta para a aba original
    except Exception as e:
        print(f"Erro ao clicar na oferta: {e}")

# Fecha o navegador
driver.quit()