import websocket
import json
import time

#modulos locales
import config

# para solicitudes en tiempo real

# Implementacion de comunicacion en paralela de discord recibe las seciones de todos los canales:
# ws: websocket
def send_json_request(ws,request):
    ws.send(json.dumps(request))

def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)
    
ws = websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?v=6&encording=json")
heartbeat_interval = receive_json_response(ws)["d"]["heartbeat_interval"]


payload = {
    "op": 2,
    "d" : {
        "token": config.TOKEN,
        "intents": 513,
        "properties": {
            "$os": 'linux',
            "$browser": 'chrome',
            "$device": 'pc'
        }
    }
}

send_json_request(ws,payload)

while True:
    event = receive_json_response(ws)
    try:
        content = event['d']['content']
        author = event['d']['author']['username']
        print(f'{author}: {content}')
    except:
        #send_json_request(ws,payload)
        pass
    
    
#TODO: necesitamos implementar una funcion en tiempo real para poder recibir un mensaje y responder de inmediato en el canal
def notification_request():
    pass