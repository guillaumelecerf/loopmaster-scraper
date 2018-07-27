#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests

LOGIN = 'xxx@example.org' # FIXME
PWD = 'xxx' # FIXME

PATH = 'loopmaster/'
BASE_URL = 'https://www.loopmasters.com'
LOGIN_URL = '/users/sign_in'
FILTERS = '?filter[view]=tiles&filter[products_page]=$page$'
GENRE = '/genres/94'

def getSoup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup;

def login():
    soup = getSoup(BASE_URL+LOGIN_URL)
    token = soup.find('meta', attrs={'name': 'csrf-token'}).get('content')
    credentials = { 'user[email]' : LOGIN, 'user[password]' : PWD, 'user[remember_me]' : 0, 'authenticity_token' : token, 'utf8' : '&#x2713;' }
    r = requests.post(BASE_URL+LOGIN_URL, data = credentials)
    print('Status code : {}'.format(r.status_code))
    if r.status_code == 500 :
        print('Url : {}'.format(r.url));
        print('Cookies : {}'.format(list(r.cookies)));
    print(r.cookies)

login()
