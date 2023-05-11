from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

DB_URL = "dbname=fruits_app_db"
def sql(query):
  connection = psycopg2.connect(DB_URL) 
  cursor = connection.cursor() 
  cursor.execute(query) 
  results = cursor.fetchall()
  connection.commit() 
  connection.close() 
  return results

@app.route('/')
def index():
  fruits = sql('SELECT * FROM fruits')
  return fruits