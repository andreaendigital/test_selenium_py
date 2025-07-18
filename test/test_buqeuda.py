from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # para github

def test_page_title():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar sin abrir ventana gráfica
    options.add_argument("--no-sandbox")  # Mejora estabilidad en CI/CD
    options.add_argument("--disable-dev-shm-usage")  # Evita errores por espacio compartido

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.get("https://www.github.com")

    titleElement = browser.find_element(By.ID, "hero-section-brand-heading")
    assert titleElement.text == "Build and ship software on a single, collaborative platform"
    browser.quit()


#def test_page_title():
 #   browser = webdriver.Chrome(service= Service("C:\\chromedriver-win64\\chromedriver.exe"))
 #   options.add_argument("--headless")  # importante para GitHub Actions

  #  browser.get("https://www.github.com")
  #  titleElement = browser.find_element(By.ID, "hero-section-brand-heading")
  #  assert titleElement.text == "Build and ship software on a single, collaborative platform"
  #  browser.quit()
