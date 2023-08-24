import requests
import json

# moduls locales
import storage
import config


def retrieve_message(chanelid):
    headers = {
        'authorization': config.TOKEN,
    }
    baseURL = f'https://discord.com/api/v9/channels/{chanelid}/messages'
    r = requests.get(baseURL,headers=headers)
    jsonn = json.loads(r.text)
    
    message = []
    for value in jsonn[::-1]:
        #print(value['content'])
        message.append(value["content"]+'\n')
        
    storage.create_file_today(storage.path,message)

# Estes es mi servidor        
#retrieve_message('912168147975536713')

tetas_chanel = '653357731591225381'
retrieve_message(tetas_chanel)


def send_message_discord(chanelid,message):
    headers = {
        'authorization': config.TOKEN,
        'Content-Type': 'application/json'
    }
    data = json.dumps({"content":message})
    baseURL = f'https://discordapp.com/api/channels/{chanelid}/messages'
    r = requests.post(baseURL,headers=headers,data=data)
    if r:
        print("enviado: ",message)
    else:
        print("error al ser enviado") 

#send_message_discord(tetas_chanel,"hola")

