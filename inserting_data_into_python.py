import mysql.connector as mc
from datetime import datetime
mydatabase=mc.connect(host="localhost",user="root",passwd="",database="week5")
cursor=mydatabase.cursor()


for i in range(0,5):
    Id=int(input("enter id"))
    name=input("enter name")
    description=input("enter description")
    category_id=int(input("enter category id"))
    chef_id=int(input("enter the chef id"))
    created=input("enter hotel name")
    cursor.execute("INSERT INTO recipes (Id,name,description,category_id,chef_id, created) VALUES(%d,%s,%s,%d,%d,%s);"),(Id,name,description,category_id,chef_id, created)
    mydatabase.commit()
