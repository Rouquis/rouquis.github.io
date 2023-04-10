import subprocess

# Verifica se o chromedriver já está instalado
try:
    import chromedriver_binary
except ImportError:
    # Caso não esteja instalado, instala automaticamente
    subprocess.check_call(['pip', 'install', 'chromedriver-binary'])

# Seu código Python continua a partir daqui

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurando o serviço do driver e as opções do navegador
s = Service('/path/to/chromedriver')
options = Options()
options.add_argument('--disable-notifications')
options.add_argument('--disable-geolocation')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Iniciando o navegador
driver = webdriver.Chrome(service=s, options=options)

# Acessando a página
driver.get('https://iplogger.com/2i2356')

# Esperando pelo botão "Negar"
negar_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[contains(text(),"Permitir")]'))
)

# Clicando no botão "Negar"
negar_btn.click()

# Fechando o navegador
driver.quit()
