
# se va a guardar en un txt lo le fecha del dia
from datetime import datetime

path = 'data/message/'

def time_today_string():
    return str(datetime.today().strftime('%Y-%m-%d')) + '.txt'

# guarda la informcion dle dia
def create_file_today(path,content):
    with open(path + time_today_string(),'w') as f:
        for i in content:
            f.write(i)
            
# Esta funcion guarda el ultimo mensaje enviado de esa forma sabemos si hay nuevos mensajes
def last_message(message):
    with open("data/",'w') as f:
        f.write(message)