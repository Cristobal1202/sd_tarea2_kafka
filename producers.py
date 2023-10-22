from kafka import KafkaProducer
from json import dumps
import time
import random
import string

# Configuración de los servidores Kafka
servidores_bootstrap = 'localhost:9092'  # Cambia a la dirección de tus servidores Kafka
topic_inscripcion = 'inscripcion'  # Cambia al tópico correspondiente

productor = KafkaProducer(
    bootstrap_servers=[servidores_bootstrap],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

def generar_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)

def enviar_inscripciones():
    topic = topic_inscripcion
    maestros = ['Maestro1', 'Maestro2', 'Maestro3', 'Maestro4', 'Maestro5']
    while True:
        maestro = random.choice(maestros)
        inscripcion_prioritaria = random.choice([True, False])
        try:
            mensaje = {
                "timestamp": int(time.time()),
                "id": generar_id(),
                "maestro": maestro,
                "inscripcion_prioritaria": inscripcion_prioritaria
            }
            productor.send(topic, value=mensaje)
            print(f"Enviando inscripción a Kafka: {mensaje}")
        except Exception as e:
            print(f"Error al enviar mensaje de inscripción: {e}")

        time.sleep(5)

if __name__ == "__main__":
    enviar_inscripciones()
