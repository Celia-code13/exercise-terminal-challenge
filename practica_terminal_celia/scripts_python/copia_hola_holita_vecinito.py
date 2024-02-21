from datetime import datetime

fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('/workspaces/exercise-terminal-challenge/practica_terminal_celia/res/test_celia.txt', "a") as archivo:
    
    archivo.write(f'Travesura realizada a las {fecha_hora_actual}')

