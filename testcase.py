from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time 
from os import getcwd
currentDirectory = getcwd()


# alternative testcases : 

# check all categories
def checkAllCategories(source):

    categories = ["HIPO","WORK","LAB","TEAM", "BLOG", "HIRE US"]

    for category in categories: 

        if category in source:

            print(category+" exists.")
        
        else :

            print(category+ " missing.")

#  main testcase 

def main(): 
    # for some reason I keep getting error while compiling 
    #  driver = webdriver.Chrome() for i kept it in the format below. 

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # go to google 
    driver.get ('http://www.google.com.tr')

    # check if page is in turkish
    if 'lang="tr"' in driver.page_source:

        is_page_tr = True

        # Search for hipo labs
        driver.find_element_by_name('q').send_keys('Hipo Labs', Keys.ENTER)

        if 'hipolabs.com' in driver.page_source : 

            elements = driver.find_elements_by_class_name("g [href]")
            links = [element.get_attribute('href') for element in elements]

            for link in links : 

                if 'hipolabs' in link : 

                    driver.get(link)

                    break

            # go to team page 
            driver.find_element_by_xpath('//*[@id="menuMaximizedButtonTeam"]/a').click()


            # Verify that page has “APPLY NOW” text

            # In our first interview I remember that Mr.Guler said that this test case is being used for some time. I'm guessing the area that used to say "Apply now" 
            # is now divided into "Apply For Jobs" and "Apply for intership". By this assumption first I'll search for "Apply now" and then search for the new ones, respectively

            if 'Apply now' in driver.page_source:

                print("exists")

            elif 'APPLY FOR JOBS' in driver.page_source : 

                if 'APPLY FOR INTERNSHIP' in driver.page_source : 

                    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

                    # with pop-up 
                    time.sleep(5)
                    driver.save_screenshot(f"{currentDirectory}/ss/screenshot.png")
                    # without pop-up 
                    driver.find_element_by_xpath('/html/body/div[6]/iframe').click()
                    driver.save_screenshot(f"{currentDirectory}/ss/screenshot_wo.png")
            
                else : 

                    print("can't find internship option")

        else : 

            print("couldn't find hipolabs.com")

    else : 

        print("the page is not in tr!")

    # checkAllCategories(driver.page_source)
    
if __name__ == "__main__" :

    main()

