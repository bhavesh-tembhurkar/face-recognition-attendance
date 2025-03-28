from flask import Flask, request, jsonify
from deepface import DeepFace
import cv2
import numpy as np
import base64
import os

app = Flask(__name__)

# Face recognition endpoint
@app.route('/verify', methods=['POST'])
def verify():
    try:
        data = request.get_json()
        img1_base64 = data.get('img1')
        img2_base64 = data.get('img2')

        # Decode base64 images
        img1 = base64.b64decode(img1_base64)
        img2 = base64.b64decode(img2_base64)

        # Convert to numpy arrays
        img1_array = np.frombuffer(img1, np.uint8)
        img2_array = np.frombuffer(img2, np.uint8)

        # Decode images
        img1 = cv2.imdecode(img1_array, cv2.IMREAD_COLOR)
        img2 = cv2.imdecode(img2_array, cv2.IMREAD_COLOR)

        # Perform face verification
        result = DeepFace.verify(img1, img2)

        return jsonify({
            "verified": result['verified'],
            "distance": result['distance'],
            "similarity": result['similarity']
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
