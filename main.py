from bs4 import BeautifulSoup   
import requests
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Yashas_08",database="DBMS_ass")
#Connection to the mySQL server is established
cursor=con.cursor()

url="https://coinmarketcap.com/"
result=requests.get(url).text
doc=BeautifulSoup(result,"html.parser")
#Connection to the website is done, and the website will be parsed

tbody=doc.tbody
trs=tbody.contents

crypto=[]
#Used for storing all the information extracted

for tr in trs[:10]:
    x=[]
    name,price=tr.contents[2:4]
    x.append(name.p.string)
    x.append(price.a.string)
    x.append(tr.contents[2].find_all('p')[1].get_text())
    crypto.append(x)


for tr in trs[10:100]:
    x=[]
    x.append(tr.contents[2].find_all('span')[1].string)
    x.append(tr.contents[3].get_text())
    x.append(tr.a.find_all('span')[2].string)
    crypto.append(x)
#Extracted using tags and stored all of them in crypto variable

sql="CREATE TABLE crypto(short_name varchar(30),name varchar(30) primary key, value varchar(15))"
cursor.execute(sql)
#Created a mySQL table
for i in crypto:
    sql1="INSERT INTO crypto VALUES('{}','{}','{}')".format(i[2],i[0],i[1])
    #All the data is embedded into the mySQL table
    cursor.execute(sql1)
con.commit()
