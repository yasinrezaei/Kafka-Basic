import socket
from confluent_kafka import Producer
import random
conf = {'bootstrap.servers': 'localhost:19092,localhost:29092,localhost:39092',
        'client.id': socket.gethostname()}

producer = Producer(conf)

MAX_RETRY = 3

def acked(err, msg,data,retry_number=0):
    
    if err is not None:
        if retry_number>MAX_RETRY:
            print(f"MAX_RETRY {MAX_RETRY}")
        else:
            print(f"Failed to deliver message: {str(msg)}: {str(err)}")
            producer.produce(topic='temperature_topic',key="name",callback=lambda err,msg :acked(err,msg,data,retry_number+1))
        
    else:
        message_key = msg.key()
        if message_key is not None:
            message_key = message_key.decode('utf-8')  # Decode if the key is in bytes

        message_value = msg.value()
        if message_value is not None:
            message_value = message_value.decode('utf-8')  # Decode if the value is in bytes

        message_topic = msg.topic()

        print(f"{message_topic} :  / Sensor ID: {message_key} / Value: {message_value}")


for i in range(100):
    sensor_id = random. randint(1, 10)
    temperature = random. randint(0,100)
    producer.produce(topic='temperature_topic',key=str(sensor_id),value=str(temperature),callback=lambda err,msg : acked(err,msg,str(temperature)))
    producer.poll(1)
    
producer.flush()
