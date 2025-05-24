from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(1, 6):
    print(f"Producing: {i}")
    producer.send('numbers', {'number': i})

producer.flush()

