from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Simulación de datos del collar
def get_pet_data():
    return {
        "name": "Firulais",
        "location": {"lat": 4.711, "lon": -74.0721},  # Bogotá
        "heart_rate": random.randint(60, 120),  # Latidos por minuto
        "temperature": round(random.uniform(37.5, 39.0), 1),  # °C
        "respiratory_rate": random.randint(15, 30)  # Respiraciones por minuto
    }

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el mapa interactivo
@app.route('/map')
def map_page():
    return render_template('map.html')

# Ruta para la guía de primeros auxilios
@app.route('/guide')
def guide_page():
    return render_template('guide.html')

# Ruta para monitoreo
@app.route('/monitor')
def monitor_page():
    return render_template('monitor.html')

# API para obtener datos del collar
@app.route('/api/pet_data', methods=['GET'])
def pet_data():
    return jsonify(get_pet_data())

if __name__ == '__main__':
    app.run(debug=True)
