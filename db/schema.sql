CREATE DATABASE fruits_app_db;
\c fruits_app_db

CREATE TABLE fruits(
	id SERIAL PRIMARY KEY,
	name TEXT,
	image_url TEXT,
	sugar REAL,
	calories REAL,
	carbohydrates REAL
);

INSERT INTO fruits(name, image_url, sugar, calories, carbohydrates)
VALUES
	('Blueberry', 'https://images.unsplash.com/photo-1626433281588-ae724357378d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1035&q=80', '5.4', '29.0', '5.5'),('Persimmon', 'https://images.unsplash.com/photo-1604872831875-26cba17467a8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80', '18', '81', '18');

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT
);