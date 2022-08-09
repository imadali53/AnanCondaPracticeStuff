#div[@class="our-services-wrapper mb-60"]

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Headless mode i.e without opening automated browser
c = Options()

c.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(),options=c) # options = headless

driver.get("https://web.bisemdn.edu.pk/downloads",)

driver.implicitly_wait(0.5)




