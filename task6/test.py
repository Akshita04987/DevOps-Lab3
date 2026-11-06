from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=opts)
try:
    driver.get("http://localhost:5000")
    text = driver.find_element("tag name", "h1").text
    print("Page text:", text, flush=True)
    assert "New Feature" in driver.page_source
    print("TEST PASSED", flush=True)
finally:
    driver.quit()
