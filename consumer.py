def generar_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 20)))

def enviar_temperatura():
    topic = 'temperatura'  # Actualizado para consistencia
    while True:
        temperatura = round(random.uniform(10, 30), 1)
        mensaje = {
            "timestamp": int(time.time()),
            "id": generar_id(),
            "temperatura": temperatura
        }
        productor.send(topic, mensaje)  # Se envía el diccionario directamente gracias al serializador
        print('Enviando JSON:', mensaje)
        time.sleep(3)

def enviar_porcentaje_humedad():
    topic = 'porcentaje_humedad'  # Actualizado para consistencia
    while True:
        humedad = random.randint(0, 100)
        mensaje = {
            "timestamp": int(time.time()),
            "id": generar_id(),
            "porcentaje_humedad": humedad
        }
        productor.send(topic, mensaje)  # Se envía el diccionario directamente gracias al serializador
        print('Enviando JSON:', mensaje)
        time.sleep(3)

def enviar_posicion():
    topic = 'posicion'  # Actualizado para consistencia
    while True:
        posicion = random.randint(0, 10)
        mensaje = {
            "timestamp": int(time.time()),
            "id": generar_id(),
            "posicion": posicion
        }
        productor.send(topic, mensaje)  # Se envía el diccionario directamente gracias al serializador
        print('Enviando JSON:', mensaje)
        time.sleep(3)
