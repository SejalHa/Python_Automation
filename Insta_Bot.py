import os
import time
import random
import requests
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Global variables
credentials = ['Reshmah571', '123@abc']
cred_filename = "creds.txt"
driver = None
actions = None
ec_wait = None
URL = "https://www.instagram.com"
IMPLICIT_WAIT_TIME = 10
WAIT_TIME = 5
USERNAME_TEXTBOX = "//input[@name = 'username']"
PASSWORD_TEXTBOX = "//input[@name = 'password']"
NOT_NOW_BUTTON = "//button[@type='button']"
LOGIN_BUTTON = "//button[@type='submit']"
SEARCH_BY_TAG = URL + "/explore/tags/"
POSTS_SEARCH = "//a[@tabindex='0']"
LIKE_BUTTON = "//span[@class='_aamw']"
CROSS_BUTTON = "//div[@class='x160vmok x10l6tqk x1eu8d0j x1vjfegm']"
COMMENT_BOX = "//textarea[contains(@aria-label, 'Add a comment')]"
COMMENT_BUTTON = "//span[@class='_aamx']"
FOLLOW_LINK = "//a[@class = 'sqdOP yWX7d     _8A5w5   ZIAjV ']"
FOLLOW_BUTTON = "//button[contains(text(),  'Follow')]"

s = Service(r"C:\sejal\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

def login():
    global ec_wait

    print()
    print("[INFO] Checking for Internet Connectivity")
    if requests.get("https://www.google.com").status_code != 200:
        print("[ERROR] No internet connection detected...please try again")
        exit(0)

    print("[INFO] Opening {0}".format(URL))
    driver.get(URL)
    driver.implicitly_wait(10)

    try:
        print("[INFO] Logging into Instagram")
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(credentials[0])
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(credentials[1])
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        ec_wait = WebDriverWait(driver, 10)
        waiter = ec_wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
    except Exception as ex:
        print(ex)

def like_post_by_tag(tagname, amount, comment_list=[], followpercentage=0):
    global driver, ec_wait, actions

    try:
        print()
        print("[INFO] Finding posts by the tag {0}".format(tagname))
        tag_url = SEARCH_BY_TAG + tagname.replace(' ', '')
        driver.get(tag_url)
        page_title = ec_wait.until(EC.title_contains("Instagram"))
        time.sleep(5)

        posts = ec_wait.until(EC.presence_of_all_elements_located((By.XPATH, POSTS_SEARCH)))
        selected_posts = random.sample(posts, min(amount, len(posts)))

        for post in selected_posts:
            actions = ActionChains(driver)
            actions.move_to_element(post).click().perform()
            time.sleep(2)
            
            page_title = ec_wait.until(EC.title_contains("Instagram"))
            time.sleep(5)

            try:
                element = ec_wait.until(EC.presence_of_element_located((By.XPATH, LIKE_BUTTON)))
                like_button = driver.find_element(By.XPATH, LIKE_BUTTON)
                like_button.click()
                print("[INFO] Liked post: {0}".format(driver.current_url))
                time.sleep(5)

                if comment_list:
                    comment_choice = random.choice(comment_list)
                    driver.find_element(By.XPATH, COMMENT_BUTTON).click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, COMMENT_BOX).send_keys(comment_choice + Keys.ENTER)
                    print("[INFO] Commented '{0}' on {1}".format(comment_choice, driver.current_url))
                    time.sleep(5)

                    if followpercentage > 0:
                        if random.randint(1, 100) <= followpercentage:
                            link = driver.find_element(By.XPATH, FOLLOW_LINK).get_attribute("href")
                            driver.execute_script("window.open('');")
                            driver.switch_to.window(driver.window_handles[1])
                            driver.get(link)
                            time.sleep(5)
                            try:
                                driver.find_element(By.XPATH, FOLLOW_BUTTON).click()
                                print("[INFO] Followed user: {0}".format(driver.current_url))
                            except:
                                print("[INFO] Already following user: {0}".format(driver.current_url))
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])

                driver.find_element(By.XPATH, CROSS_BUTTON).click()
                time.sleep(5)

            except Exception as ex:
                print("[INFO] Already liked post: {0}".format(driver.current_url))
                driver.find_element(By.XPATH, CROSS_BUTTON).click()
                time.sleep(5)

    except Exception as ex:
        print(ex)

def like_post_by_multiple_tags(tag_list, amount, comment_list=[], followpercentage=0):
    print("[INFO] Finding posts by the tags {0}".format(tag_list))
    for tag in tag_list:
        like_post_by_tag(tag, amount, comment_list, followpercentage)

def main():
    global driver, ec_wait, actions, credentials

    try:
        if not os.path.exists(cred_filename):
            print("[ERROR] Invalid path...please try again")
            exit(0)

        with open(cred_filename, "r") as file:
            credentials = file.read().split(" ")

        tags, comment_list = [], []

        while True:
            tags = input("Enter tag/tags you want to search (required) (separated by commas): ").split(",")
            amount = int(input("Enter amount of posts you want to check per tag (required) (not more than 10): "))
            followpercentage = int(input("Enter follow percentage (type '0' for no follows): "))
            comment_list = input("Enter list of comments you want to enter (separated by commas): ").split(",")

            print('\n[INFO] Here is your bot configurations')
            print("[INFO] Tags: {0}".format(tags))
            print("[INFO] Amount:", amount)
            print("[INFO] Comments List:", comment_list)
            print("[INFO] Follow percentage:", followpercentage)
            agree = input("Do you agree with the configurations (y/n): ")

            if agree.lower() == 'y':
                break
            else:
                print("")
                continue

        login()
        like_post_by_multiple_tags(tags, amount, comment_list, followpercentage)
        driver.quit()

    except KeyboardInterrupt:
        print("[INFO] User stopped the program...exiting")
        exit(0)
    except TypeError:
        print("[ERROR] Some input was entered wrong...please try again")
        exit(0)
    except Exception as ex:
        print("[ERROR] Something went wrong:", ex)
        traceback.print_exc()
        exit(0)

if __name__ == '__main__':
    main()
