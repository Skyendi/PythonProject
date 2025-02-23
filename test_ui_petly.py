from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_news():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://team-project-petly-frontend-git-main-alekseibaliuk.vercel.app/')
    sleep(2)
    news_link = browser.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div/nav[1]/ul/li[1]/a')
    news_link.click()
    sleep(2)
    title_news = browser.find_element(By.XPATH, '//*[@id="root"]/div/main/section/div/h1')
    sleep(2)
    assert title_news.text == 'News'

