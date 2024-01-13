# Kafka-Basic

## cli
```bash
docker exec -it <container_id> /bin/bash

#topics
kafka-topics --create --topic <topic_name> c --bootstrap-server broker:29092 --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server  broker:9092 --describe --topic <topic_name>

kafka-topics --bootstrap-server  broker:9092 --list

kafka-topics --bootstrap-server  broker:9092 --delete --topic <topic_name>

#producer
kafka-console-producer --broker-list broker:29092 --topic <topic_name>
kafka-console-producer --broker-list broker:29092 --topic <topic_name> --producer-property acks=all

kafka-console-producer --bootstrap-server kafka-broker-2:9092 --topic amir_test_topic --property "parse.key=true" --property "key.separator=:"


#consumer
kafka-console-consumer --bootstrap-server broker:29092 --topic <topic_name> --from-beginning

# consumer group 
kafka-console-consumer --bootstrap-server broker:29092 --topic <topic_name> --group <group_name>

kafka-consumer-groups --bootstrap-server broker:29092 --list

kafka-consumer-groups --bootstrap-server broker:29092 --describe --group <group_name>


# reset offset
kafka-consumer-groups --bootstrap-server broker:29092 --group <group_name> --reset-offset --to-earliest --execute --all-topics
```

