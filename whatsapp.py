import os
from twilio.rest import Client
from flask import Flask, request
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# Your Account SID and Auth Token from twilio.com/console
account_sid  = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

# Send a message
message = client.messages \
                .create(
                     body="Hello from Python",
                     from_='whatsapp:+14155238886',
                     to='whatsapp:+34619492313'
                 )

print(message.sid)

# Receive a message
@app.route('/incoming', methods=['POST'])
def incoming():
    body = request.values.get('Body', None)
    # Do something with the incoming message
    print(body)
    return ('', 204)

if __name__ == '__main__':
    app.run()