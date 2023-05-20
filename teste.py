from selenium import webdriver
import time

navegador = webdriver.Chrome("chromedriver.exe")

navegador.get("https://www.instagram.com/")
time.sleep(2)

navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("offsvi_")
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("061219920800601221")
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
