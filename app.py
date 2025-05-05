import requests
from flask import Flask, request

app = Flask(__name__)

# Your actual Make.com webhook URL
MAKE_WEBHOOK_URL = 'https://hook.eu2.make.com/jhk882a15h3xljj8s3h5bh1d9vs649rv'

@app.route('/', methods=['GET'])
def home():
    return 'Webhook server is running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received:", data)

    try:
        # Forward incoming data to Make.com webhook
        response = requests.post(MAKE_WEBHOOK_URL, json=data)
        print("Forwarded to Make.com:", response.status_code)
    except Exception as e:
        print("Error forwarding to Make:", e)

    return 'Webhook received and forwarded!', 200
