import sqlite3
from flask import Flask, render_template, request

conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():  # put application's code here
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_restaurant():
    new_restaurant = request.form.get('new_restaurant')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO restaurants (new_restaurant) VALUES (?)", new_restaurant)
    conn.commit()
    conn.close()
    #cursor.execute("SELECT * FROM restaurants")
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
