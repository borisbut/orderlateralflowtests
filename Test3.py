import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Hard code method
# path=r"C:\Users\bbut\AppData\Local\Google\Chrome\Application\chrome.exe"
# driver = webdriver.Chrome(path)
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.gov.uk/order-coronavirus-rapid-lateral-flow-tests")

# parent = driver.find_element(By.ID, "get-started")
# button = parent.find_element(By.TAG_NAME, 'a')
# button = driver.find_element(By.TAG_NAME, "a")
parent = driver.find_element(By.ID, "content")
button = parent.find_element(By.CLASS_NAME, "gem-c-button")
button.click()

symptoms = driver.find_element(By.ID, "condition-2")
symptoms.click()

# parent = driver.find_element(By.CLASS_NAME, "govuk-grid-column-two-thirds")
# parent = driver.find_element(By.CLASS_NAME, "govuk-!-margin-top-4 govuk-button")
# button = driver.find_element(By.CLASS_NAME, "govuk-!-margin-top-4")
# button = parent.find_element(By.CLASS_NAME, "button")
# button = parent.find_element(By.TAG_NAME, "submit")
# button = parent.find_element(By.CSS_SELECTOR, ".button.button--wide")
# button = driver.find_element(By.CSS_SELECTOR, ".button.button--wide")
# button = driver.find_element(By.CSS_SELECTOR, "button")
button = driver.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top-4']")
# button = parent.find_element(By.NAME, "Continue")
button.click()

# Sign in
parent = driver.find_element(By.ID, "main-content")
button = parent.find_element(By.LINK_TEXT, "Continue without an account")
# child = parent.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top-6']")
# button = child.find_element(By.TAG_NAME, "a")
# button = child.find_element(By.CLASS_NAME, "govuk-link")
# # button = child.find_element(By.TAG_NAME, "a")
# # child = parent.find_element(By.CLASS_NAME, "govuk-!-margin-top-6")
# # button = child.find_element(By.CLASS_NAME, "govuk-link")
# child = parent.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top-6']")
# # button = parent.find_element(By.TAG_NAME, "a")
# # parent = driver.find_element(By.CLASS_NAME, "govuk-grid-column-two-thirds")
# # button = parent.find_element(By.TAG_NAME, "a")
# button = child.find_element(By.TAG_NAME, "a")
# button = child.find_element(By.CLASS_NAME, "govuk-link")
button.click()

# name
driver.find_element(By.ID, "first-name").send_keys("Fee Fee")
driver.find_element(By.ID, "last-name").send_keys("Wan")
button = driver.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top-4']")
button.click()

# email
driver.find_element(By.ID, "email-available").click()
driver.find_element(By.ID, "email").send_keys("borisb.ut@googlemail.com")
driver.find_element(By.ID, "email-confirmation").send_keys("borisb.ut@googlemail.com")
button = driver.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top-4']")
button.click()

# mobile
driver.find_element(By.ID, "mobile-available-2").click()
button = driver.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top-4']")
button.click()

# DOB
driver.find_element(By.ID, "date-of-birth-day").send_keys("31")
driver.find_element(By.ID, "date-of-birth-month").send_keys("5")
driver.find_element(By.ID, "date-of-birth-year").send_keys("1964")
button = driver.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top-4']")
button.click()

# Live where
driver.find_element(By.ID, "country").click()
button = driver.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top-4']")
button.click()

# NHS
driver.find_element(By.ID, "nhs-staff-2").click()
button = driver.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top']")
button.click()

# Continue
button = driver.find_element(By.CSS_SELECTOR, "*[class^='govuk-!-margin-top']")
button.click()

# Delivery
driver.implicitly_wait(3)
button = driver.find_element(By.ID, "submit-delivery-information")
button.click()

# Postcode
driver.find_element(By.NAME, "postcode-input").send_keys("GU51 2TZ")
button = driver.find_element(By.ID, "submit-postcode-home")
button.click()

# dropdown
select = Select (driver.find_element(By.ID, "home-address-select-list"))
select.select_by_visible_text('5, RYELAND CLOSE, FLEET, HAMPSHIRE, GU51 2TZ')
button = driver.find_element(By.ID, "home-address-submit")
button.click()

# Same address
driver.find_element(By.ID, "x-same-address").click()
button = driver.find_element(By.ID, "x-address-check-next")
button.click()

# check email address for code
button = driver.find_element(By.ID, "3-send-code")
button.click()

#  enter code
driver.find_element(By.NAME, "code-input").send_keys("K75CBC7L")
button = driver.find_element(By.ID, "4-confirm-code")
button.click()

# place order
driver.find_element(By.NAME, "disclaimer").click()
button = driver.find_element(By.ID, "7-submit-order")
button.click()
