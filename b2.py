import mysql.connector
import pandas as pd
import numpy as np
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password = "",
  database="customerb2"
)

print(mydb)
mycursor = mydb.cursor()
check_sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(check_sql)

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

mycursor.execute("CREATE TABLE customers (customerid VARCHAR(255), firstname VARCHAR(255), lastname VARCHAR(255), companyname VARCHAR(255), billingaddress1 VARCHAR(255), billingaddress2 VARCHAR(255), city VARCHAR(255), state VARCHAR(255), postalcode VARCHAR(255), country VARCHAR(255), phonenumber VARCHAR(255), emailaddress VARCHAR(255), createddate VARCHAR(255))")

data = pd.read_csv("customer.csv")
data['customerid'] = data['customerid'].map(str)
c = data.columns.values
for i in c:
    data[i] = data[i].fillna(0)
sql = """INSERT INTO customers (customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city,  state, postalcode, country, phonenumber, emailaddress, createddate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
vals = []
cus_data = []
for i in range(0, 18):
    vals.append(data.iloc[i].values)
for val in vals:
    y = [x for x in val]
    y = tuple(y)
    cus_data.append(y)
print(cus_data)
mycursor.executemany(sql, cus_data)
mydb.commit()