#!/usr/bin/python3
import mysql.connector
import json
from mysql.connector import Error
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'anime'

mysql = MySQL(app)

@app.route("/")
def main():
    return jsonify({"title": "animeinfo"})

@app.route("/search",methods=['GET'])
def search():
    try :
       idAnime = int(request.args["anime-id"]);
    except:
        idAnime = False
    if isinstance(idAnime, int):
        cur = mysql.connection.cursor()
        cur.execute("""SELECT * FROM animes WHERE id = %s""", (idAnime,))
        dataAnime = cur.fetchone()
        anime = {
            "id": dataAnime[0],
            "title": dataAnime[1],
            "description": dataAnime[2],
            "year": dataAnime[3]
        }
        return jsonify(anime)
    else:
        return jsonify({"error": "Ocurrio un error"});


@app.route("/all", methods=["GET"])
def allAnimes():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM animes""")
    allDatas = cur.fetchmany()
    return jsonify(allDatas)

@app.route("/about")
def anime():
    with open("aboutl.json", "r") as data:
        about = json.load(data)
    return about;