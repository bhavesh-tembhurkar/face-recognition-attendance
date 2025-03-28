from deepface import DeepFace
import json
import sys
import base64
import cv2
import numpy as np

def decode_image(base64_string):
    """Decode base64 image to OpenCV format."""
    img_data = base64.b64decode(base64_string)
    np_arr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img

def get_face_embedding(image_base64):
    try:
        img = decode_image(image_base64)
        
        # Extract face embeddings
        result = DeepFace.represent(img, model_name="Facenet", enforce_detection=False)

        # Return embeddings as JSON
        return json.dumps({"status": "success", "embeddings": result}, indent=4)

    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)}, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"status": "error", "message": "Usage: python deepface_service.py <base64_image>"}))
    else:
        base64_image = sys.argv[1]
        output = get_face_embedding(base64_image)
        print(output)

