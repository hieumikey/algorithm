from os import name
import requests
from bs4 import BeautifulSoup
# Fill in your details here to be posted to the login form.
payload = {
    'log': 'admin',
    'pwd': '123456aA'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('http://45.79.43.178/source_carts/wordpress/wp-login.php', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    # print(p.text)
    # soup = BeautifulSoup(p.content, "html.parser")
    # uname = soup.findAll('span', class_='display-name')
    # print(uname)
    # # An authorised request.
    r = s.get('http://45.79.43.178/source_carts/wordpress/wp-admin/profile.php')
    print (r.text)
    soup = BeautifulSoup(r.content, "html.parser")
    uname = soup.select_one('#user_login')
    uname = soup.find('input', {'id': 'user_login'}).get('value')
    print(uname)