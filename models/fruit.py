from db.db import sql

def all_fruits():
  return sql('SELECT * FROM fruits ORDER BY id')

def get_fruit(id):
  fruits = sql("SELECT * FROM fruits WHERE id = %s", [id])
  return fruits[0]

def create_fruit(name, image_url, sugar, calories, carbohydrates):
  sql('INSERT INTO fruits(name, image_url, sugar, calories, carbohydrates) VALUES(%s, %s, %s, %s, %s) RETURNING *', [name, image_url, sugar, calories, carbohydrates])

def update_fruit(name, image_url, sugar, calories, carbohydrates, id):
	sql('UPDATE fruits SET name=%s, image_url=%s, sugar=%s, calories=%s, carbohydrates=%s WHERE id=%s RETURNING *', [name, image_url, sugar, calories, carbohydrates, id])
        
def delete_fruit(id):
	sql('DELETE FROM fruits WHERE id=%s RETURNING *', [id])

def like_fruit(fruit_id, user_id):
  sql("INSERT INTO likes(user_id, fruit_id) VALUES(%s, %s) RETURNING *", [user_id, fruit_id])

def search_fruit(search):
  fruit = sql("SELECT * FROM fruits WHERE name = %s", [search])
  return fruit[0]