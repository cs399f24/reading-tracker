from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template("index.html")

# Backend route to call Google Books API
@app.route('/search')
def search():
    query = request.args.get('query', 'harry potter')  # Default to 'harry potter' if no query provided
    google_books_api = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    
    response = requests.get(google_books_api)
    data = response.json()

    return jsonify(data)  # Return Google Books API data as JSON to frontend

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
