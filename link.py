import requests
import json

def chatbot(text):
    data={'sender':'test_user', 'message':text}
    url='http://localhost:81/ '
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    k=r.json()[0].get('text')
    print(k)
    return k