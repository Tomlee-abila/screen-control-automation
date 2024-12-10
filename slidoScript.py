from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import traceback

def setup_driver():
    """Set up and return a Chrome WebDriver instance."""
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    
    # Use WebDriver Manager to automatically download and manage ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def clear_browser_cache(driver):
    """Clear browser cache using keyboard shortcut."""
    try:
        # Send Ctrl+Shift+Delete to clear cache
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.SHIFT + Keys.DELETE)
        time.sleep(2)  # Wait for cache clearing dialog/process
    except Exception as e:
        print(f"Error clearing cache: {e}")

def run_slido_automation(url, input_name, loops=1000):
    """
    Automate Slido page interaction with enhanced error handling
    """
    driver = setup_driver()
    
    try:
        for loop in range(loops):
            print(f"Starting loop {loop + 1}")
            
            # Navigate to Slido event page
            driver.get(url)
            
            # Wait for and select the specific input
            try:
                # Print page source for debugging
                print("Page source length:", len(driver.page_source))
                
                # Find all input elements for debugging
                all_inputs = driver.find_elements(By.TAG_NAME, 'input')
                print(f"Total inputs found: {len(all_inputs)}")
                for inp in all_inputs:
                    print(f"Input attributes - Name: {inp.get_attribute('name')}, ID: {inp.get_attribute('id')}, Type: {inp.get_attribute('type')}")
                
                # Try multiple methods to find and click the input
                try:
                    # Method 1: Wait and click by name
                    input_element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.NAME, input_name))
                    )
                    input_element.click()
                    print(f"Selected input by name: {input_name}")
                except TimeoutException:
                    # Method 2: Try find elements by name and click first
                    input_elements = driver.find_elements(By.NAME, input_name)
                    if input_elements:
                        input_elements[2].click()
                        print(f"Selected input by direct find: {input_name}")
                    else:
                        # Method 3: Try XPath partial match
                        input_elements = driver.find_elements(By.XPATH, f"//*[contains(@name, '{input_name}')]")
                        if input_elements:
                            input_elements[0].click()
                            print(f"Selected input by partial name match: {input_name}")
                        else:
                            raise Exception(f"Could not find input with name: {input_name}")
            
            except Exception as e:
                print(f"Comprehensive error selecting input: {e}")
                print("Detailed traceback:")
                traceback.print_exc()
            
            # Clear browser cache
            clear_browser_cache(driver)
            
            # Refresh page
            driver.refresh()
            
            # Optional: Add a delay between loops
            time.sleep(5)
    
    except Exception as e:
        print(f"Critical error occurred: {e}")
        traceback.print_exc()
    
    finally:
        # Close the browser
        driver.quit()

# Replace with your actual Slido event URL and input name
EVENT_URL = "https://app.sli.do/event/1VW5NGfMCLFmCCDUdD22P1/live/polls"
INPUT_NAME = "13a5e0fa-0e94-4af6-ba2b-40b984ecf0c9"

# Run the automation
run_slido_automation(EVENT_URL, INPUT_NAME)