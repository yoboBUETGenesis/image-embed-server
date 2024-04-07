import os
from dotenv import load_dotenv 
from flask import Flask, request, jsonify
from inference_sdk import InferenceHTTPClient

load_dotenv()
os.environ["ROBOFLOW_API_KEY"] = os.getenv('ROBOFLOW_API_KEY')
CLIENT = InferenceHTTPClient(
    api_url="https://infer.roboflow.com",
    api_key=os.environ["ROBOFLOW_API_KEY"],
)

app = Flask(__name__)

@app.route('/image-embed', methods=['POST'])
def submit_form():
    # Check if 'imageLink' is in the form data
    if 'imageLink' not in request.form:
        return jsonify({'error': 'Image link not provided'}), 400

    # Get the image link from the form data
    image_link = request.form['imageLink']
    print(image_link)
    # Make a request to Roboflow API to get image embeddings
    try:
        res = CLIENT.get_clip_image_embeddings(inference_input=image_link, clip_version="ViT-B-32")
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    embeddings = res["embeddings"][0]

    return jsonify({
        "image_embeddings": embeddings
    })
    