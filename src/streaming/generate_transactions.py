import random
import time
import json
from kafka import KafkaProducer

# VARIABLES
KAFKA_BOOTSTRAP_SERVERS = "kafka1:19092,kafka2:19093,kafka3:19094"
KAFKA_TOPIC = 'transactions-topic'
transaction_types = ["credit", "pos", "payment"]
count = 1

# PRODUCTOR DE KAFKA
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS
)

print(f"▶️ Startting simulate transactions ... ")

# SIMULACION DE TRANSACCIONES

for i in range(100):
    time.sleep(0.4)

    transaction_id = random.randint(11111, 99999)
    transaction_type = random.choice(transaction_types)
    transaction_amount = random.randint(100, 10000)
    now = time.localtime()
    transaction_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", now)

    # Print the event
    data = {
        "transaction_id": transaction_id,
        "transaction_type": transaction_type,
        "transaction_amount": transaction_amount,
        "transaction_timestamp": transaction_timestamp,
    }


    # ENVIAR TRANSACCIONES AL TOPICO DE KAFKA
    producer.send(
        topic=KAFKA_TOPIC,
        value=json.dumps(data).encode('utf-8'),
    )
    # SALIDA DE CONSOLA
    print(f"▶️ Sending transaction to {KAFKA_TOPIC} with #{count} ✅")
    count+=1


# CERRAR PRODUCTOR
producer.close()
print(f"⏹️ Finish successfully ✅")

