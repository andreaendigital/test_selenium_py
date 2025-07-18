from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_page_title():
    browser = webdriver.Chrome(service= Service("C:\\chromedriver-win64\\chromedriver.exe"))
    browser.get("https://www.github.com")
    titleElement = browser.find_element(By.ID, "hero-section-brand-heading")
    assert titleElement.text == "Build and ship software on a single, collaborative platform"
    browser.quit()
