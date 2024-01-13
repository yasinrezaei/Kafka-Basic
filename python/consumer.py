import socket
from confluent_kafka import Consumer,KafkaError,KafkaException
import sys

conf = {'bootstrap.servers': 'localhost:19092,localhost:29092,localhost:39092',
        'client.id': socket.gethostname(),'group.id':'Backend'}
consumer = Consumer(conf)
MIN_COMMIT_COUNT=1

def msg_process(msg):
    message_key = msg.key()
    if message_key is not None:
        message_key = message_key.decode('utf-8')  # Decode if the key is in bytes

    message_value = msg.value()
    if message_value is not None:
        message_value = message_value.decode('utf-8')  # Decode if the value is in bytes

    message_topic = msg.topic()

    print(f"{message_topic} : Sensor ID: {message_key} / Value: {message_value}")




def synchronous_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        msg_count = 0
        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg)
                msg_count += 1
                if msg_count % MIN_COMMIT_COUNT == 0:
                    consumer.commit(asynchronous=False)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

def asynchronous_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        msg_count = 0
        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg)
                msg_count += 1
                if msg_count % MIN_COMMIT_COUNT == 0:
                    consumer.commit(asynchronous=True)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

asynchronous_consume_loop(consumer,['temperature_topic',])