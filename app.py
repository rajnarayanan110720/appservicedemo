from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Azure Flask App!'

if __name__ == '__main__':
    # Get the port number from the environment variable set by Azure, default to 5000 if not found
    port = int(os.environ.get("PORT", 5000))
    
    # Run the app with the appropriate host and port for Azure
    app.run(host='0.0.0.0', port=port, debug=True)
