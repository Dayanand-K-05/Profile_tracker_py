from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open GitHub Profile
github_profile_url = "https://github.com/Dayanand-K-05"
driver.get(github_profile_url)

# Wait for the Repositories tab to be present
try:
    repo_count_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Counter"))
    )
    repo_count = repo_count_element.text.strip()
    print(f"Repositories Count: {repo_count}")
except Exception as e:
    print("Error: Could not find the repositories count element.")
    print(e)

# Close browser
driver.quit()
