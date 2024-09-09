from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# Caminho para o WebDriver do Edge
PATH = "D:\\webdriver\\msedgedriver.exe"
service = Service(PATH)

# Inicializa o Edge WebDriver
driver = webdriver.Edge(service=service)

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