from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.json['text']
    
    # Text to speech conversion
    tts = gTTS(text)
    tts.save("output.mp3")
    
    return send_file("output.mp3", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
