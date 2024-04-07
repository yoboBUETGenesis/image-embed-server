# Image Embedding Flask Application

This Flask application provides an endpoint `/image-embed` to generate embeddings for images using the Roboflow API.

## Getting Started

To run this application locally, follow these steps:

### Prerequisites

- Python 3.x installed on your machine
- `pip` package manager

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/image-embedding-flask.git
    ```

2. Navigate to the project directory:

    ```bash
    cd image-embedding-flask
    ```

3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Make sure you have set up your environment variables. You need to provide your Roboflow API key. Create a `.env` file in the root directory of the project and add your API key:

```
ROBOFLOW_API_KEY=your_api_key_here
```


### Running the Application

Run the Flask application:

```
python3 app.py
```
The application will start running on http://localhost:8080.

### Usage
Once the application is running, you can make a POST request to the /image-embed endpoint with form data containing an image link (imageLink). The application will return the embeddings for the provided image.

Example request using curl:

```
curl -X POST -F "imageLink=https://example.com/image.jpg" http://localhost:8080/image-embed

```

### Dependencies
- Flask: Web framework for building the application
- dotenv: Load environment variables from a .env file
- inference_sdk: SDK for interacting with the Roboflow API