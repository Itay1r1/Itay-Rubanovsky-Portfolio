from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Test 1 - In this test I will present table's content (cells)
def test_table(driver):
    #find table
    table = driver.find_element(By.TAG_NAME, 'table')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    bodyrows = tbody.find_elements(By.TAG_NAME, 'tr')

    #print table cells
    for row in bodyrows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        for cell in cells:
            print(cell.text)

 # Test 2 - In this test I will fill the fields of Personal Information window and use HTML button clear to clear field's content
def test_information_window(driver):
    #find Personal Information window
    form = driver.find_element(By.TAG_NAME, 'form')

    #fill in the fields
    first_name = driver.find_element(By.NAME, 'fname')
    first_name.send_keys('Itay')
    
    last_name = driver.find_element(By.NAME, 'lname')
    last_name.send_keys('Rubanovsky')
    
    city = driver.find_element(By.NAME, 'City')
    city = Select(city)
    city.select_by_visible_text('Jerusalem')
    
    email = driver.find_element(By.ID, 'email')
    email.send_keys('Itayrubanovsky@gmail.com')
    
    mobile_area_code = driver.find_element(By.NAME, 'areaCode')
    mobile_area_code = Select(mobile_area_code)
    mobile_area_code.select_by_visible_text('054')
    
    mobile_number = driver.find_element(By.ID, 'phone')
    mobile_number.send_keys('054-723-0697')
   
    radio_button_male = driver.find_element(By.ID, 'm')
    radio_button_male.click()

    select_math = driver.find_element(By.NAME, 'math')
    select_math.click()

    select_biology = driver.find_element(By.NAME, 'bio')
    select_biology.click()

    time.sleep(3)

    #clear the fields
    clear = driver.find_element(By.ID, 'CB')
    clear.click()

    time.sleep(3)

# Test 3 - In this test I will use JS button "Set Text" to change page title and then use "Start Loading" button
def test_js_buttons(driver):
    #find "Set Text" button and click it
    set_text_button = driver.find_element(By.CSS_SELECTOR, 'button[onClick="SetText();"]')
    set_text_button.click()
    #switch to the prompt and enter text
    alert = driver.switch_to.alert
    alert.send_keys('QA Automation project')
    alert.accept()

    #click "Start Loading" button
    start_loading_button = driver.find_element(By.CSS_SELECTOR, 'button[onClick="setTimeout(myTimeout1, 5000);"]')
    start_loading_button.click()
    #wait for "Finish" to appear
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'startLoad'), 'Finish')
    )
    
    time.sleep(3)

# Test 4 -In this test I will use the links and then I will check the page title of each site
def test_links(driver):
    #"Next Page" Link
    next_page_link = driver.find_element(By.NAME, 'nextPage')
    next_page_link.click()
    #wait for the page to load
    WebDriverWait(driver, 10).until(EC.title_is("Next Page"))
    #change title
    change_title_button = driver.find_element(By.CSS_SELECTOR, 'button[onClick="changeTitle();"]')
    change_title_button.click()
    #check the title
    if driver.title == "Finish":
        print("true")
    else:
        print("false")
    #return to previous page
    driver.back()

    #"Windy" Link
    windy_link = driver.find_element(By.NAME, 'myLink')
    windy_link.click()
    #wait for the page to load
    WebDriverWait(driver, 10).until(EC.title_is("Windy: Wind map & weather forecast"))
    #check the title
    if driver.title == "Windy: Wind map & weather forecast":
        print("true")
    else:
        print("false")
    #return to previous page
    driver.back()

    #"Tera Santa" Link
    tera_santa_link = driver.find_element(By.NAME, 'myLinkTS')
    tera_santa_link.click()
    #wait for the page to load
    WebDriverWait(driver, 10).until(EC.title_is("TERRASANTA SEAKAYAK EXPEDITIONS | טרה סנטה קיאקים ימיים – SEAKAYAK EXPEDITIONS"))
    #check the title
    if driver.title == "TERRASANTA SEAKAYAK EXPEDITIONS | טרה סנטה קיאקים ימיים – SEAKAYAK EXPEDITIONS":
        print("true")
    else:
        print("false")
    #return to previous page
    driver.back()

    #"Java Book" Link
    java_book_link = driver.find_elements(By.NAME, 'notMyLink')[0]
    java_book_link.click()
    #wait for the page to load
    WebDriverWait(driver, 10).until(EC.title_is("ivbs-white-logo.png (108×63)"))
    #check the title
    if driver.title == "ivbs-white-logo.png (108×63)":
        print("true")
    else:
        print("false")
    #return to previous page
    driver.back()

    #"YouTube" Link
    youtube_link = driver.find_elements(By.NAME, 'notMyLink')[1]
    youtube_link.click()
    #wait for the page to load
    WebDriverWait(driver, 10).until(EC.title_is("YouTube"))
    #check the title
    if driver.title == "YouTube":
        print("true")
    else:
        print("false")
    #return to previous page
    driver.back()

    time.sleep(3)

if __name__ == '__main__':
    # Suppress SSL certificate errors and device logs
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors') #ignore SSL certificate errors
    options.add_experimental_option('excludeSwitches', ['enable-logging']) #suppress device logs

    # Setup Chrome service and driver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get('http://127.0.0.1:5500/HTML_Project.html')
        driver.maximize_window()
    
        # Test 1 (Table)
        test_table(driver)

        # Test 2 (Personal Information Window + HTML Buttons)
        test_information_window(driver)

        # Test 3 (JS Buttons)
        test_js_buttons(driver)

        # Test 4 (Links)
        test_links(driver)

    finally:
        driver.quit() #close the browser