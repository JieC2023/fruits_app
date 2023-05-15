from flask import render_template, request, redirect, session
from models.fruit import all_fruits, get_fruit, create_fruit, update_fruit, delete_fruit, like_fruit, search_fruit
from services.session_info import current_user

def index():
  fruits = all_fruits()
  return render_template('fruits/index.html', fruits=fruits, current_user=current_user())

def new():
  return render_template('fruits/new.html')

def create():
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  sugar = request.form.get('sugar')
  calories = request.form.get('calories')
  carbohydrates = request.form.get('carbohydrates')
  
  create_fruit(name, image_url, sugar, calories, carbohydrates)
  return redirect('/')

def edit(id):
  fruit = get_fruit(id)
  return render_template('fruits/edit.html', fruit=fruit)

def update(id):
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  sugar = request.form.get('sugar')
  calories = request.form.get('calories')
  carbohydrates = request.form.get('carbohydrates')
 
  update_fruit(name, image_url, sugar, calories, carbohydrates, id)
  return redirect('/')

def delete(id):
  delete_fruit(id)
  return redirect('/')

def like(id):
  like_fruit(id, session['user_id'])
  return redirect('/')

def search():
  search=request.args.get('search')
  search_result = search.capitalize()
  fruit = search_fruit(search_result)
  print(fruit)
  return render_template('fruits/search.html', fruit=fruit, current_user=current_user)