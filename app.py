from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'cars.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret-key'


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            image TEXT NOT NULL
        )
        '''
    )
    conn.commit()
    conn.close()


@app.route('/')
def home():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', cars=cars)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        image = request.form.get('image', '').strip()

        if name and description and image:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO cars (name, description, image) VALUES (?, ?, ?)',
                (name, description, image)
            )
            conn.commit()
            conn.close()

        return redirect(url_for('admin'))

    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('admin.html', cars=cars)


@app.route('/delete/<int:car_id>')
def delete_car(car_id: int):
    conn = get_db_connection()
    conn.execute('DELETE FROM cars WHERE id = ?', (car_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
