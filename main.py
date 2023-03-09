#!/usr/bin/python3
import mysql.connector
import json
from mysql.connector import Error
from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return "HOLA ITE"


@app.route("/bye")
def adios():
    return "<center><h2>Hola</h2><marquee>Hola</marquee></center>"


@app.route("/about")
def anime():
    with open("aboutl.json", "r") as data:
        about = json.load(data)
    
    return about;


# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='anime',
#                                          user='root',
#                                          password='password1')
#     if connection.is_connected():
#         sql_select_Query = "select * from animes"
#         cursor = connection.cursor()
#         cursor.execute(sql_select_Query)
#         # get all records
#         records = cursor.fetchall()
#         print("Total number of rows in table: ", cursor.rowcount)

#         print("\nPrinting each row")
#         for row in records:
#             print("idAnimes = ", row[0], )
#             print("title = ", row[1])
#         # db_Info = connection.get_server_info()
#         # print("Connected to MySQL Server version ", db_Info)
#         # cursor = connection.cursor()
#         # cursor.execute("select database();")
#         # record = cursor.fetchone()
#         # print("You're connected to database: ", record)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
