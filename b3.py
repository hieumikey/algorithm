from os import name
import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd
import os, csv
with requests.Session() as s:
    p = s.get('https://00e57086a7747a5a96c58b6f4a88eb61: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@hieupn99.myshopify.com/admin/api/2021-04/orders.json')
    print(p.status_code)
    r = s.get('https://00e57086a7747a5a96c58b6f4a88eb61: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@hieupn99.myshopify.com/admin/api/2021-04/customers.json')
    data = r.text
    # with open('data.txt', 'w') as outfile:
    #     json.dump(data, outfile)
    #print(type(data))
    data = json.loads(data)
    print(data['customers'][0]['id'])
    customers = data['customers'][0]
    with open('customertest.csv', 'w') as f:
        for key in customers.keys():
            f.write("%s,%s\n"%(key, customers[key]))
    data_customer = pd.read_csv('customertest.csv').T
    os.remove("customertest.csv")
    print(type(data_customer))
    data_customer.to_csv('customerapi.csv')
    t = pd.read_csv('customerapi.csv')
    print(t)