from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

DB_URL = "dbname=fruits_app_db"
def sql(query, parameters=[]):
  connection = psycopg2.connect(DB_URL) 
  cursor = connection.cursor() 
  cursor.execute(query, parameters) 
  results = cursor.fetchall()
  connection.commit() 
  connection.close() 
  return results

@app.route('/')
def index():
  fruits = sql('SELECT * FROM fruits')
  return render_template('fruits/index.html', fruits=fruits)

@app.route('/fruits/new')
def new():
  return render_template('fruits/new.html')

@app.route('/fruits', methods=['POST'])
def create():
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  sugar = request.form.get('sugar')
  calories = request.form.get('calories')
  carbohydrates = request.form.get('carbohydrates')
  sql('INSERT INTO fruits(name, image_url, sugar, calories, carbohydrates) VALUES(%s, %s, %s, %s, %s) RETURNING *', [name, image_url, sugar, calories, carbohydrates])
  return redirect('/')