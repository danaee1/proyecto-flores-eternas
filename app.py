from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'flores_eternas'
}

def get_db():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/flowers')
def get_flowers():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM flowers')
    flowers = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(flowers)

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO orders (user_id, fecha, estado, total, created_at) VALUES (%s, %s, %s, %s, NOW())',
        (data.get('user_id'), data.get('fecha'), data.get('estado'), data.get('total'))
    )
    order_id = cursor.lastrowid
    
    # Insertar items de la orden
    for item in data.get('items', []):
        cursor.execute(
            'INSERT INTO order_items (order_id, flower_id, cantidad) VALUES (%s, %s, %s)',
            (order_id, item.get('flower_id'), item.get('cantidad'))
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'success': True, 'order_id': order_id})

if __name__ == '__main__':
    app.run(debug=True, port=5000)