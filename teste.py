from selenium import webdriver
import time

navegador = webdriver.Chrome("chromedriver.exe")

navegador.get("https://www.instagram.com/")
time.sleep(2)

navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("offsvi_")
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("061219920800601221")
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[3]').click()
time.sleep(7)
# Indo para o link do sorteio
navegador.get("https://www.instagram.com/p/CsbYeQdLag6/")
time.sleep(2)

z = 0
while 1 == 1:
    navegador.find_element('xpath', '//*[@id="mount_0_0_iw"]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea').send_keys("G")
    z += 1
    print(f"{z}")

