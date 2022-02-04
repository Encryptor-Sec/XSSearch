#!/usr/bin/python
# -*- coding: utf-8 -*-
# importing all required libraries

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import warnings
import argparse
import sys

banner = \
    '''            
	 __   __ _____ _____                     _     
	 \ \ / // ____/ ____|                   | |    
	  \ V /| (___| (___   ___  __ _ _ __ ___| |__  
	   > <  \___ \\__ _ \ / _ \/ _` | '__/ __| '_ \ 
	  / . \ ____) |___) |  __/ (_| | | | (__| | | |
	 /_/ \_\_____/_____/ \___|\__,_|_|  \___|_| |_|
	-----------------------------------------------
 	   \033[33m A Comprehensive Reflected XSS Scanner\033[0m 
	-----------------------------------------------

	   DEVELOPED & OWNED BY : SATHYAPRAKASH SAHOO 

'''

# Configuring options for Chrome WebDriver

warnings.filterwarnings('ignore')

options = webdriver.ChromeOptions()

options.add_argument('--headless')

options.add_argument('--disable-xss-auditor')

options.add_argument('--disable-web-security')

options.add_argument('--ignore-certificate-errors')

options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',
                          chrome_options=options)

# Creating arguments for taking input

parser = \
    argparse.ArgumentParser(epilog='Command : python3 xssearch -u https://www.target.com/search={xss} -p payloads.txt'
                            )

parser.add_argument('-u', metavar='url.com/?s={xss}',
                    help='Add URL with paramter as ={xss}',
                    required=True)

parser.add_argument('-p', metavar='payloads.txt',
                    help='Add file containing all the payloads',
                    required=True)

args = parser.parse_args()

# Printing Banner

print (banner)

# Checking if placeholder is assigned in the URL or not

if not '{xss}' in args.u:

    sys.exit("""
\033[31mError\033[0m : Need '{xss}' placeholder parameter ! 
\033[31mMessage\033[0m : python3 xssearch.py -h for more help :) """)
else:

    target = args.u

p = args.p

print ("[*] Starting XSSearch ...")

# Executing a loop for checking valid XSS payload in the given URL

for payload in open(p, 'r').readlines():

    url = target.replace('{xss}', payload)

    driver.get(url)

# Checking for a javascript pop-up

    try:

        WebDriverWait(driver, 1).until(EC.alert_is_present())

        alert = driver.switch_to.alert

        alert.accept()

        print ("\033[31m[+] XSS Triggered !\033[0m", payload)
    except TimeoutException:

        print ("\033[36m[+] XSS not Triggered ! \033[0m", payload)

driver.close()
