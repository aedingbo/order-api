# Import necessary modules from Flask
from flask import Flask, request, jsonify  # `jsonify` is used to return properly formatted JSON responses

# Initialize the Flask application
app = Flask(__name__)  

# Define an API route that listens for POST requests at "/orders"
@app.route('/orders', methods=['POST'])
def create_order():
    """
    This function handles incoming API requests to the '/orders' endpoint.

    - It expects the request to contain JSON data.
    - `request.json` extracts the JSON data sent in the request body.
    - The extracted data is processed and returned in the response.
    - `jsonify(...)` ensures that the response is properly formatted as JSON.

    Why use `jsonify`?
    - `jsonify` automatically converts Python objects (dict, list) to JSON format.
    - It sets the correct HTTP Content-Type header (`application/json`).
    - It handles special cases like Unicode characters and ensures compatibility.
    """
    order = request.json  # Retrieve JSON data from request body
    
    # Return a JSON response confirming receipt of the order
    return jsonify({"message": "Order received", "order": order}), 201  

# The following line ensures that the Flask app runs only when executed directly
if __name__ == '__main__':
    """
    Why do we use '__name__ == "__main__"'?
    
    - '__name__' is a special variable in Python that stores the name of the script.
    - If this script is being run directly (like `python app.py`), '__name__' is set to '__main__'.
    - If this script is imported as a module (`import app`), '__name__' is set to 'app' instead.
    - This prevents unintended execution when the script is used in a larger project.
    
    When executed directly, this block starts the Flask application.
    """

    # Run the Flask app and make it accessible externally on port 5000
    app.run(host='0.0.0.0', port=5000)  
