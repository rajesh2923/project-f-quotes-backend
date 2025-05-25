cat > app.py << 'EOF'
from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final; failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you’re halfway there. – Theodore Roosevelt"
]

@app.route("/quote")
def get_quote():
    return jsonify(quote=random.choice(quotes)), 200

@app.route("/health")
def health():
    return jsonify(status="OK"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")
EOF

