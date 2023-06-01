#código em Testes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import instaloader
import random
import os.path

# Atualizar o driver do navegador toda vez que for executado
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# servico = Service(ChromeDriverManager().install())]


driver = webdriver.Chrome("chromedriver.exe")


def sorteioInstagram():
    abrindo_instagram("offsvi_", "061219920800601221", "https://www.instagram.com/p/CsbYeQdLag6/")

    if os.path.isfile("comentarios.txt"):
        print("Arquivo de Seguidores já carregado....")
    else:
        pegar_seguidores("liderwesleyalemao")
    comentandoPost()

def abrindo_instagram(username, password, url):
    print("Abrindo Instagram...")
    driver.get("https://www.instagram.com/")
    sleep(3)
    print("Fazendo Login no Instagram..")
    driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/span').send_keys(username)
    driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]').click()
    sleep(10)
    print("Negando Solicitação de Segurança Instagram...")
    driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]').click()
    sleep(5)
    print("Acessando o Post do sorteio...")
    driver.get(url)


def pegar_seguidores(usuario):
    L = instaloader.Instaloader()
    L.login('offsvi_', '061219920800601221')
    profile = instaloader.Profile.from_username(L.context, usuario)

    print(f"Salvando Seguidores de {usuario}...")
    # Salvando Seguidores em Arquivo .TXT
    file = open("comentarios.txt.txt", "a+")
    for followee in profile.get_followers():
        username = "@" + followee.username
        file.write(username + "\n")

    file.close()


def comentandoPost():
    z = 0
    while 1 == 1:
        cmt = driver.find_element('xpath', '//*[@id="mount_0_0_ZX"]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea')
        cmt.click()
        comment = lendo_arquivo()
        driver.find_element('xpath', '//*[@id="mount_0_0_ZX"]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea').send_keys(comment)
        driver.find_element('xpath', '//*[@id="mount_0_0_ZX"]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea').send_keys(' ')
        sleep(10)
        driver.find_element('xpath', '//*[@id="mount_0_0_ZX"]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea').send_keys(Keys.ENTER)
        sleep(10)
        driver.find_element('xpath', '//*[@id="mount_0_0_ZX"]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea').send_keys(Keys.ENTER)
        z += 1
        print(f"{z}")
        sleep(60)

def lendo_arquivo():
    with open("comentarios.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        return random.choice(words)


sorteioInstagram()