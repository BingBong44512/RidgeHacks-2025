from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def receive_location():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    print(f"Received GPS: {latitude}, {longitude}")
    return jsonify({"status": "success"})
