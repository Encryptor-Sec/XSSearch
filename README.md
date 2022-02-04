# XSSearch
##### _A Comprehensive Reflected XSS Scanner_
<p align="center">
  <img  width="350" src="Images/Banner.PNG" />
</p>

<p align="center">
<img src=https://img.shields.io/badge/Made%20with-Python-blue>
<img src=https://img.shields.io/badge/Python-3.7-green>
<img src=https://img.shields.io/badge/Version-1.0-yellowgreen>
<img src=https://img.shields.io/badge/OS-Linux-yellow> <br>
<img src=https://img.shields.io/badge/Framework-Selenium-brightgreen>
<img src=https://img.shields.io/badge/WebDriver-ChromeDriver-blue>
</p>
<p align="center">
    <h3 align="center"> XSSearch is a comprehensive reflected XSS tool with 3000+ Payloads for automating XSS attacks and validating XSS endpoints.  </h3>
</p>

***
>#### DISCLAIMER :

The XSSearch developer will not be held liable if the tool is used with harmful or criminal intent. Please use at your own risk. :)

**** 
>#### USES :
- XSSearch can be used to discover reflected Cross Site Scripting (XSS) vulnerabilities 
- XSSearch is capable of validating XSS payloads.
- XSSearch will facilitate in the automation of brute - force attack for the verification of reflected XSS.
- Works on all Linux environment
- This can also be used in penetration testing to evaluate sanitization strength.
***
>#### FEATURES :
- Contains more than 3000 payloads for XSS validation
- Works on selenium framework & ChromeDriver
- It is faster than other XSS tools since the code is very light and rapid.
- The code and payloads can be modified according to the situation. 
***
>#### SETUP & INSTALLATION
XSSearch requires Selenium, ChromeDriver and Python to work smoothly on your system.

**Installing Selenium**
```
$ sudo apt update
$ pip3 install selenium
```
**Installing Chrome Browser for Linux (Skip this if you already have Chrome browser on your Linux)**
````
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo apt install ./google-chrome-stable_current_amd64.deb
````
**You may use the command to start Chrome from your terminal.**
```
$ google-chrome --no-sandbox
```
**Downloading ChromeDriver**

Go to https://chromedriver.chromium.org/downloads and get the linux 64 zipped version of ChromeDriver 80.0.3987.106.

Unzip the zip file. There will be a file for ChromeDriver. Open terminal on the same location and use the following command.
````
$ sudo chmod +x chromedriver
$ sudo mv -f chromedriver /usr/bin/chromedriver
````
***
>#### USAGE
XSSearch is a command line tool that uses a single command line instruction for simple and speedy execution.<br/>
**Note** : This tool will only work on url which has a input paramter in the url. Example : www[.]target[.]com/?xyz=
```
$ python3 xssearch.py -u url.com/?s={xss} -p payloads.txt
```
**Arguments :**<br/>
**-u** : It is required for URL input<br/>
**-p** : It is required for Payload file input<br/>
**{xss}** : It is a placeholder that the user should append after an equal to sign (=) in the url argument.

**Live Usage**
````
$ python3 xssearch.py -u https://ac121f0e1eb31ae5c0c9473f00f400f7.web-security-academy.net/?search={xss} -p payloads.txt
````
<p align="center">
<img src=https://github.com/Encryptor-Sec/XSSearch/blob/main/Images/xssearch.PNG>
</p>

Above is the screenshot of the tool with live example.<br/>
_Valid XSS exploits are marked with red alerts.<br/>
Invalid XSS exploits are marked with blue alerts._

**Errors & Warnings**<br/>
The following are some errors that might arise as a result of an incomplete command, not specifying arguments or not specifying placeholders.<br/>

Use the below command to get help
````
$ python3 xssearch.py -h
````
<p align="center">
<img src=https://github.com/Encryptor-Sec/XSSearch/blob/main/Images/xssearch_warnings.PNG>
</p>

***
#### LICENSE
[MIT-License](LICENSE)
***
#### More suggestions and contributions are highly appreciated to make this tool better :)
### _STAY SAFE, ACT SMART_
### Hit Me Up
[![Twitter ](https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/_encryptor_)
[![Instagram](https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/xhackerboyy)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sathyaprakashsahoo)
[![Website](https://img.shields.io/badge/Website-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://www.cyberbuddy.co.in)

