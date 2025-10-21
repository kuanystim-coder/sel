from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
assert "Example Domain" in driver.title
driver.quit()
