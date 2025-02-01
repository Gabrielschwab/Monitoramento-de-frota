import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do Selenium
URL_LOGIN = "https://pooltrack.logicasolucoes.com.br"
USUARIO = "08938386000199"
SENHA = "123456"
XPATH_SIDEBAR_BUTTON = "//*[@id=\"sidebar\"]/div/div[1]/ul/li[2]/a"
XPATH_MENU_BUTTON = "//*[@id=\"menu_29\"]/li[1]/a"
XPATH_VEICULO_BUTTON = "//*[@id=\"list-veiculo\"]/table/tbody/tr/td[6]/a"
XPATH_DOWNLOAD_BUTTON = "//*[@id=\"veiculo40161GeraRelatorioXLS\"]"

# Configuração do Chrome
options = webdriver.ChromeOptions()
#options.add_experimental_option("prefs", {
#    "download.default_directory": "./C:\Users\Gabriel Schwab\Downloads"})  # Define a pasta de download

# Inicia o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(URL_LOGIN)
time.sleep(6)

try:
    # Preenche login e senha
    driver.find_element(By.NAME, "username").send_keys(USUARIO)
    driver.find_element(By.NAME, "password").send_keys(SENHA + Keys.RETURN)
    time.sleep(6)

    # Clica no botão do sidebar
    driver.find_element(By.XPATH, XPATH_SIDEBAR_BUTTON).click()
    time.sleep(6)

    # Clica no botão do menu
    driver.find_element(By.XPATH, XPATH_MENU_BUTTON).click()
    time.sleep(6)

    # Clica no botão do veículo
    driver.find_element(By.XPATH, XPATH_VEICULO_BUTTON).click()
    time.sleep(6)

    # Clica no botão de download
    download_button = driver.find_element(By.XPATH, XPATH_DOWNLOAD_BUTTON)
    download_button.click()
    print("✅ Download iniciado com sucesso!")
    time.sleep(5)  # Aguarde o download
except Exception as e:
    print(f"❌ Erro: {e}")
finally:
    driver.quit()
