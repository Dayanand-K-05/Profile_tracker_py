from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enable headless mode (Runs in background)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Initialize WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# GitHub username
username = "Your GitHub username"  # Replace with the target GitHub username
github_url = f"https://github.com/{username}?tab=repositories"

# Open GitHub profile (in headless mode)
driver.get(github_url)

# Wait until repositories load
wait = WebDriverWait(driver, 10)
repo_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h3[@class='wb-break-all']/a")))

# Get repository names
repositories = [repo.text for repo in repo_elements]

# Dictionary to store repo info
repo_data = {}

# Loop through each repository
for repo in repositories:
    repo_url = f"https://github.com/{username}/{repo}"
    driver.get(repo_url)

    try:
        # Wait for commit info to load
        recent_commit = wait.until(EC.presence_of_element_located((By.XPATH, "//relative-time"))).get_attribute("datetime")
    except:
        recent_commit = "No commits found"

    try:
        total_commits = driver.find_element(By.XPATH, "//span[@class='d-none d-sm-inline']/strong").text
    except:
        total_commits = "Unknown"

    # Store data
    repo_data[repo] = {
        "Recent Commit": recent_commit,
        "Total Commits": total_commits
    }

# Print results
for repo, details in repo_data.items():
    print(f"Repository: {repo}")
    print(f"Recent Commit: {details['Recent Commit']}")
    print(f"Total Commits: {details['Total Commits']}\n")

# Close the browser
driver.quit()
