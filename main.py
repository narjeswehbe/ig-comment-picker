# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from lib2to3.pgen2 import driver

from selenium import webdriver
import random as r
from time import sleep
from dotenv import load_dotenv
import pandas as pd
from selenium.webdriver.common import by
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import os

# global section
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()
option = webdriver.ChromeOptions()
option.add_argument('--lang=en-US')
option.add_argument('--window-size=1200,1000')


def openURI(url):
    s = Service('C:\\chromedriver.ex')
    print("inside openURI")
    print(url)
    browser = webdriver.Chrome(service=s, options=option)
    browser.get(url)
    login(browser)

    # names = getFollowers(browser)
    openPost(browser, "https://www.instagram.com/reel/Cl3qcbRoWae/?utm_source=ig_web_copy_link")
    comments = getComments(browser)
    winner = getRandomWinner(comments)
    sleep(10)


def login(browser):
    global username, password, login_btn, not_now_1, not_now_2

    try:
        username = WebDriverWait(browser, timeout=10).until(
            lambda d: d.find_element(by.By.XPATH, "//input[@name='username']"))
    except TimeoutError:
        print("time out")

    try:
        password = WebDriverWait(browser, timeout=10).until(
            lambda d: d.find_element(by.By.XPATH, "//input[@name='password']"))
    except TimeoutError:
        print("time out")

    try:
        login_btn = WebDriverWait(browser, timeout=10).until(
            lambda d: d.find_element(by.By.XPATH, "//button[@type='submit']"))
    except TimeoutError:
        print("time out")

    username.send_keys(os.getenv("USERNAME_IG"))
    password.send_keys(os.getenv("PASSWORD_IG"))
    login_btn.click()
    try:
        not_now_1 = WebDriverWait(browser, timeout=10).until(
            lambda d: d.find_element(by.By.XPATH, "//button[contains(text(),'Not Now')]"))
    except TimeoutError:
        print("time out")
    if not_now_1 is not None:
        not_now_1.click()
    # try:
    #     not_now_2 = WebDriverWait(browser, timeout=10).until(
    #         lambda d: d.find_element(by.By.XPATH, "//button[contains(text(),'Not Now')]"))
    # except TimeoutError:
    #     print("time out")
    # if not_now_2 is not None:
    #     not_now_2.click()

    sleep(10)


def openAccount(browser):
    global account_name
    browser.get("https://www.instagram.com/reel/Cl3qcbRoWae/?utm_source=ig_web_copy_link")
    sleep(10)
    browser.find_elements(by.By.XPATH,
                          '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _acan _acao _acat _acaw _aj1- _a6hd"]')[
        0].click()

    # try:
    #     account_name =  WebDriverWait(browser, timeout=10).until(
    #         lambda d: d.find_element(by.By.XPATH, "//a[contains(text(),'{0}')]".format(account)))
    # except TimeoutError:
    #     print("time out")
    #
    # account_name.click()

    # Press the green button in the gutter to run the script.


def getComments(browser):
    # find the books of the comments
    global comment_box
    global comments
    try:
        comment_box = WebDriverWait(browser, timeout=12).until(
            lambda d: d.find_element(by.By.XPATH,
                                     "//ul[@class='_a9z6 _a9za']"))

    except TimeoutError:
        print("time out")

    while 1:
        try:
            load_more = WebDriverWait(browser, timeout=18).until(
                EC.element_to_be_clickable((by.By.XPATH,
                                            "//*[@aria-label='Load more comments']")))
            load_more.click()
            comments = []
            for c in comment_box.find_elements(by.By.XPATH, '//span[@class="_aap6 _aap7 _aap8"]'):
                comments.append(c.text)
            print(comments)
            print(len(comments))
            print("===================================")
            print('''==============================================
                  THE WINNER IS
                  =================================================
              ''')
            print(comments[r.randint(1,len(comments)-1)])

        except :
            return comments
            pass



    return comments


def getRandomWinner(comments):
    return


def openPost(browser, url):
    browser.get(url)


def getFollowers(browser):
    global followers_link, names
    try:
        followers_link = WebDriverWait(browser, timeout=12).until(
            lambda d: d.find_element(by.By.XPATH, "//a[contains(.,'followers')]"))
    except TimeoutError:
        print("time out")

    followers_link.click()
    sleep(3)
    scroll_box = browser.find_element(by.By.XPATH, "//div[@class='_aano']")
    sleep(5)
    # height variable
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        sleep(2)
        # scroll down and return the height of scroll (JS script)
        ht = browser.execute_script(""" 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)

        # list follower name
        sleep(5)
        # print(f"{line} Scroll Buttom  Done!!! {line}")
        links = scroll_box.find_elements(by.By.TAG_NAME, 'a')
        sleep(2)
        names = [name.text for name in links if name.text != '']
        # need to filter empty string so we used name.text instead of name
        # btn = browser.find_element(by.By.XPATH,"//*[@id='mount_0_0_4p']/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
        # btn.click()

        sleep(10)
    browser.quit()
    return names


if __name__ == '__main__':
    b = openURI("https://www.instagram.com/")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
