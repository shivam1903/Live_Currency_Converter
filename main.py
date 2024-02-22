from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def convert_currency(cur_from, cur_to, amount):
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--ignore-certificate-errors")
    prefs = {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,
    "safebrowsing.enabled": True}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)

    url = "https://www.google.com/search?q=" + cur_from + "+to+" + cur_to + "+currency"
    driver.get(url)
    try:
        div_element = driver.find_element(By.CSS_SELECTOR, "div.sD9T5c")
        cur1_field = driver.find_element(By.CSS_SELECTOR, "select.l84FKc")
        selected_option_1 = cur1_field.find_element(By.CSS_SELECTOR, "option:checked")
        cur2_field = driver.find_element(By.CSS_SELECTOR, "select.NKvwhd")
        selected_option_2 = cur2_field.find_element(By.CSS_SELECTOR, "option:checked")
        output_field = driver.find_element(By.CSS_SELECTOR, "input.a61j6")  # Targeting output field by class
        rate = output_field.get_attribute("value")
        print("Current Conversion rate is 1 " + selected_option_1.text + " = " + str(rate) + " " + selected_option_2.text)
        input_field = driver.find_element(By.CSS_SELECTOR, "input.lWzCpb")  # Targeting input field by class
        input_field.clear()
        input_field.send_keys(amount)
        time.sleep(2)
        # output_field = driver.find_element(By.CSS_SELECTOR, "input.a61j6")  # Targeting output field by class
        output_list = []
        output_list.append(output_field.get_attribute("value"))
        output_list.append(selected_option_2.text)
        
        return output_list
    
    except:
        print("Incorrect Currencies Entered. Please enter them again")
        driver.close()
        main()
        

def main():
    curr_fr = str(input("Enter the Currency you want to covert from(or Country Name): "))
    curr_to = str(input("Enter the Currency you want to covert to(or Country Name): "))
    moni = int(input("Enter the amount that you want to convert: ")) or 1
    final_list = convert_currency(curr_fr, curr_to, moni)
    # print(final_list)
    print("After conversion you have " + str(final_list[0]) + " " + final_list[1])
    exit()

if __name__ == "__main__":
    main()