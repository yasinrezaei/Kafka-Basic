from confluent_kafka import Consumer, KafkaException,KafkaError

def consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        is_commit_pending = False
        while True:  # Replace with a proper condition to exit
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    pass
                else:
                    raise KafkaException(msg.error())
            else:
                # Process message
                process_message(msg)

                # Commit asynchronously
                consumer.commit(asynchronous=True)
                is_commit_pending = True

            # Check for commit errors in the next poll
            if is_commit_pending:
                try:
                    consumer.poll(0)
                    # If no exception occurred, assume commit was successful
                    is_commit_pending = False
                except KafkaException as e:
                    # Handle commit error
                    handle_commit_error(e)

    finally:
        # Close the consumer
        consumer.close()

def process_message(msg):
    # Process your message here
    pass

def handle_commit_error(exception):
    # Handle your commit error here
    pass

# Consumer configuration
conf = {
    'bootstrap.servers': "YOUR_KAFKA_BROKER",
    'group.id': "YOUR_GROUP_ID",
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consume_loop(consumer, ['your_topic'])