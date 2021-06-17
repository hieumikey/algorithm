from os import name
import requests
from bs4 import BeautifulSoup
import json
import re
with requests.Session() as s:
    p = s.get('https://00e57086a7747a5a96c58b6f4a88eb61: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@hieupn99.myshopify.com/admin/api/2021-04/orders.json')
    print(p.status_code)
    r = s.get('https://00e57086a7747a5a96c58b6f4a88eb61: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@hieupn99.myshopify.com/admin/api/2021-04/customers.json')
    data = r.text
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    