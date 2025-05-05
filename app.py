from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Webhook server is running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook data:", data)
    return 'Webhook received!', 200