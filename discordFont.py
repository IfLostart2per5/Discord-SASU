
import pyautogui as pyg
import pyperclip as ppc
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
cemail, cuser, cpassw, cday, cmonth, cyear = '//*[@id="uid_5"]', '//*[@id="uid_7"]', '//*[@id="uid_9"]', '//*[@id="react-select-2-input"]', '//*[@id="react-select-3-input"]', '//*[@id="react-select-4-input"]'
BtnEnter = '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div[2]/div/div[5]/button'


def winloop():
    t = 1
    while t > 0:
        time.sleep(1)


CYAN = "\033[1;37m"
BOLD = "\033[;1m"
RESET = "\033[;0m"
user = input("Escreva o nome desejado: ")
email = input("Escreva o email desejado: ")
password = input("Coloque a senha: ")
unbirthday = input("Coloque sua Data de nascimento (Coloque a barra para separar): ")
birthday = unbirthday.split("/")
brw = webdriver.Chrome()
print(CYAN + "Sistema: " + BOLD + RESET + "pode ignorar os erros que aparecem no console, são só erros de usb mesmo '-'")
brw.get("https://discord.com/register")
time.sleep(5)
brw.find_element('xpath', cemail).send_keys(email)
brw.find_element('xpath', cuser).send_keys(user)
brw.find_element('xpath', cpassw).send_keys(password)
brw.find_element('xpath', cday).send_keys(birthday[0])
brw.find_element('xpath', cday).send_keys(Keys.ENTER)
brw.find_element('xpath', cmonth).send_keys(birthday[1])
brw.find_element('xpath', cmonth).send_keys(Keys.ENTER)
brw.find_element('xpath', cyear).send_keys(birthday[2])
brw.find_element('xpath', cyear).send_keys(Keys.ENTER)
time.sleep(1)
brw.find_element('xpath', BtnEnter).click()
winloop()