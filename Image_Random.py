# Python 3
# 04/14/20
# Script that randomly selects an image based on user preference.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import random
from PIL import Image

# Obtain path of chromedriver
def path():
    ChromeDriver_Path = "C:\Program Files (x86)\chromedriver.exe"
    
    return ChromeDriver_Path
    

# run webbrowser in headless mode
def background(ChromeDriver_Path):
    options = Options()

    options.add_argument("--headless")    
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(ChromeDriver_Path , chrome_options=options) # choose webbrowser

    return driver



# User selection
# Open html of webpage
def decision(driver):

    display = '''[><><><><><><><><><><><><><>><><>><><><><><><><><><><><><><><><><><><><><><><><><><]\n    Hello User, what would you like to see today? *kitten *puppy *otter *random\n[><><><><><><><><><><><><><>><><>><><><><><><><><><><><><><><><><><><><><><><><><><] \n Selection: '''
    user_choice = input(display) # user types out selection
    print("loading...")

    dict_database = {'kitten': "https://shorturl.at/qJK35", 'puppy': "https://shorturl.at/nAKOU", 'otter': "https://shorturl.at/ipIRU", 'random': "https://shorturl.at/rzSW3"}

    for selection,url in dict_database.items():
        if selection == user_choice.lower():
            driver.get(url) 

    

# Locating desired content within html 
def locate(driver):
    list1 = []
    for img_tag in driver.find_elements_by_xpath("//img[@class='GrowthUnauthPinImage__Image']"): # limited to pinterest
        src = img_tag.get_attribute('src')
        list1.append(src)

    return list1


# Select & Save Image

def SS_output(list1,driver):
    random_src = random.choice(list1)
    urllib.request.urlretrieve(random_src, "Enjoy!.jpg")
    driver.quit()

def runstuff():
    ChromeDriver_Path = path()
    driver = background(ChromeDriver_Path)
    decision(driver)
    list1 = locate(driver) # takes no argument : assuming driver.get(url) is global
    SS_output(list1,driver)




def open_image():
    im = Image.open("Enjoy!.jpg")
    im.show()


runstuff()
open_image()