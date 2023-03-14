#!/usr/bin/python3
import mysql.connector
import json
from mysql.connector import Error
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password1'
app.config['MYSQL_DB'] = 'anime'

mysql = MySQL(app)

@app.route("/")
def main():
    return jsonify({"title": "animeinfo API"})

@app.route("/anime", methods=['GET'])
def search():
    try:
        idAnime = int(request.args["anime-id"])
    except:
        idAnime = False
    if isinstance(idAnime, int):
        cur = mysql.connection.cursor()
        cur.execute("""SELECT * FROM animes WHERE id = %s""", (idAnime,))
        dataAnime = cur.fetchone()
        if dataAnime is None:
            return jsonify({"error": "Anime not found"})
        anime = {
            "id": dataAnime[0],
            "title": dataAnime[1],
            "description": dataAnime[2],
            "year": dataAnime[3],
            "genre": dataAnime[4],
        }
        return jsonify(anime)
    else:
        return jsonify({"error": "Ocurrió un error"})


@app.route("/anime/all", methods=["GET"])
def allAnimes():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM animes""")
    allData = cur.fetchall()
    allAnimes = []
    for anime in allData:
        allAnimes.append({
            "id": anime[0],
            "title": anime[1],
            "description": anime[2],
            "year": anime[3],
            "genre": anime[4],
        })
    return jsonify(allAnimes)


@app.route("/about")
def anime():
    with open("aboutl.json", "r") as data:
        return jsonify(json.load(data))