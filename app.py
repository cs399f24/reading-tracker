from flask import Flask, render_template, jsonify, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template("index.html")

# Backend route to call Google Books API
@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('query')  # Get the query from the search form
    google_books_api_key = os.getenv('GOOGLE_BOOKS_API_KEY')  # Get API key from environment variable
    google_books_api = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={google_books_api_key}"
    
    response = requests.get(google_books_api)
    data = response.json()
    return jsonify(data)  # Return Google Books API data as JSON to frontend

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
