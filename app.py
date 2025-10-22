from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('weight.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.before_first_request
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS weights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            weight REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    if request.method == 'POST':
        date = request.form['date']
        weight = request.form['weight']
        conn.execute('INSERT INTO weights (date, weight) VALUES (?, ?)', (date, weight))
        conn.commit()
    weights = conn.execute('SELECT * FROM weights ORDER BY date').fetchall()
    conn.close()
    return render_template('index.html', weights=weights)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM weights WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)