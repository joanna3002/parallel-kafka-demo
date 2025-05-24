# Parallel Kafka Demo

This repository contains a demo project for parallel processing using Apache Kafka.

## Project Structure

- `consumer/` — Kafka consumer application files  
- `producer/` — Kafka producer application files  
- `manifests/` — Kubernetes deployment and service manifests for Kafka and Zookeeper  

## How to Run

### Prerequisites
- Docker installed  
- Kafka and Zookeeper running (can be done with Docker or Kubernetes)  
- Python 3.x (for consumer and producer scripts)  

### Running with Docker

Start Zookeeper:
```bash
docker run -d --name zookeeper --network=host -e ZOOKEEPER_CLIENT_PORT=2181 wurstmeister/zookeeper

Start kafka:
docker run -d --name kafka --network=host \
  -e KAFKA_ZOOKEEPER_CONNECT=localhost:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_LISTENERS=PLAINTEXT://localhost:9092 \
  wurstmeister/kafka

Running the Producer and Consumer
python3 producer/producer.py
python3 consumer/consumer.py

