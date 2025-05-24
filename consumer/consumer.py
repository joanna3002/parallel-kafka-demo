from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'demo-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='demo-group'
)

print("Listening for messages on 'demo-topic'...")

for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")



