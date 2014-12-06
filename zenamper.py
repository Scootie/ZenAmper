#Copyright (c) 2014 Caleb Ku
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import zenamp_settings
import time, datetime
import logging


SLEEP_SECONDS = 8

def login(driver,myusername,mypassword):

	driver.get("https://cloud.zenminer.com/login")
	
	if check_exists_by_xpath(driver,"//*[@id='login-form']/div[1]/div/input")==True:
		logging.info('Portal loaded properly.')
	else:
		logging.info('Page did not load properly.')
		return

	username = driver.find_element_by_name('username')
	password = driver.find_element_by_name('password')

	username.send_keys(myusername)
	password.send_keys(mypassword)

	driver.find_element_by_xpath("//*[@id='login-form']/div[3]/div/div[2]/button").click()


def boostme(driver,NotAmped,amptype,doubledipchoice):

	if amptype=='DD':

		for k,v in NotAmped.iteritems():

			v.click()
			time.sleep(SLEEP_SECONDS)

			sele=Select(driver.find_element_by_xpath("//*[@id='secondPool']/div/div/div[2]/form/div/select"))
			dropdown_options = sele.options

			
			for available in range(0,len(dropdown_options)):
				current_option=dropdown_options[available].text

				if doubledipchoice==current_option:
					sele.select_by_visible_text(current_option)
					time.sleep(SLEEP_SECONDS)
					break
			SecondPoolDiv=driver.find_element_by_id("secondPool")

			SecondPoolDiv.find_element_by_xpath(".//button[contains(text(), 'Add Pool')]").click()

			time.sleep(SLEEP_SECONDS)
	
	elif amptype=='Boost':
		
		for k,v in NotAmped.iteritems():
			v.click()
			time.sleep(5)

def find_hashletprimes(driver,myampchoice):

	driver.get("https://cloud.zenminer.com/miners/")
	time.sleep(SLEEP_SECONDS)

	if check_exists_by_xpath(driver,"//*[@id='tab-hashlets']/div[3]/div[1]/button")==True:
		logging.info('Miner page is loaded')
	else:
		logging.info('Miner page is not loaded')
		return

	AllPrimes = driver.find_elements_by_css_selector(".hashlet-prime")

	AllPrime_status={}
		
	for primes in range(0,len(AllPrimes)): #cycle through Hashlet Primes
		Focus=AllPrimes[primes]
		primenumber=primes+1
		status_lock = check_exists_by_classname(Focus,"im-lock")

		status_secondpool = check_exists_by_classname(Focus,"second-pool-icon")

		status_boosted = check_exists_by_classname(Focus,"fa-ban-circle")

		if (status_lock==True) or (status_secondpool==True) or (status_boosted==True):
			statusmsg=Focus.find_element_by_css_selector(".power-scrypt").get_attribute("data-title")
			AllPrime_status[primes]= "Not Available for action"
			logging.info("Prime # %d is N/A, %s" % (primenumber, statusmsg))
		elif myampchoice=='Boost':
			AllPrime_status[primes]=Focus.find_element_by_class_name("im-rocket")
			logging.info("Boosting Prime # %d" % primenumber)
		elif myampchoice=='DD':
			AllPrime_status[primes]=Focus.find_element_by_class_name("fa-plus-sign")
			logging.info("Double Dipping Prime # %d" % primenumber)
	return AllPrime_status

def find_ampable_primes(AllPrime_status):
	available_primes={}
	locked_primes={}

	for primes in range(0,len(AllPrime_status)):
		current_status=str(AllPrime_status[primes])

		if "Not Available" in current_status:
			locked_primes[primes]=AllPrime_status[primes]
		else:
			available_primes[primes]=AllPrime_status[primes]

	return available_primes

def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_classname(driver,classname):
    try:
        driver.find_element_by_class_name(classname)
    except NoSuchElementException:
        return False
    return True

def cleanup_exit(driver):
	time.sleep(SLEEP_SECONDS)
	driver.close()


def Zen_AutoCharger():

	driver = webdriver.Chrome()
	logging.basicConfig(filename='zenamper.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)
	driver.set_page_load_timeout(30)
	login(driver,zenamp_settings.ZENMINER_USERNAME,zenamp_settings.ZENMINER_PASSWORD)

	prime_array = find_hashletprimes(driver,zenamp_settings.PREFERENCE) #find all primes
	ampable_primes = find_ampable_primes(prime_array) # find all available primes
	if not ampable_primes: #check if there are any available primes
		logging.info('No primes to amp.')
		
	else:
		boostme(driver,ampable_primes,zenamp_settings.PREFERENCE,zenamp_settings.DD_ORDER)
		
	cleanup_exit(driver)


Zen_AutoCharger()

