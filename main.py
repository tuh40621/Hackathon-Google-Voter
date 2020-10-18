# Updated 10/6/20

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

'''
Setting up Chrome options for use - necessary for chrome to be used in Repl.it
'''
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless') # allows for running in a silent window

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get('https://docs.google.com/forms/d/e/1FAIpQLSdsTHf6WeD8Bti3mCUGVMKQWa1dP9phkEXo3eSR2ppHOFt1FA/viewform')
sleep(3)

for i in range(25):
#path to wanted option
 VoteButtonPath='/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/span/div/div[8]/label/div/div[1]/div/div[3]/div'
 VoteButton=webdriver.find_element_by_xpath(VoteButtonPath)
 VoteButton.click()
 sleep(2)
#presses submit
 SubmitButtonPath='//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div/span/span'
 Submit=webdriver.find_element_by_xpath(SubmitButtonPath)
 Submit.click()
#wait for page to finish loading
 sleep(3)
 print("before")
 AgainButtonPath='/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
 again=webdriver.find_element_by_xpath(AgainButtonPath)
 again.click()
 sleep(3)
#now it repeats for as many times as it is wanted