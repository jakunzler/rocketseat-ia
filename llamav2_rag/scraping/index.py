
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configura o WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abre a página web
driver.get("https://embrasca.com.br/")

# Agora, você pode interagir com a página
# Por exemplo, vamos supor que você quer extrair o título da página
titulo = driver.find_element_by_tag_name('h1').text
print("Título da página:", titulo)

# Fechar o navegador após a extração
driver.quit()
