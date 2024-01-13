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

## Producer Acks
```
- acks = 0 => Producer won't wait for acknowledgment(possible data loss)
- acks = 1 => Producer will wait for leader acknowledgment(limited data loss)
- acks = all => leader + replica acknowledgment(no data loss)
```
## acks=all & min.insync.replicas
```
- min.insync.replicas = 1 => only the broker leader needs to successfully ack
- min.insync.replicas = 2 => at least the broker leader and one replica need to ack

```

## Since kafka 3.0 the producer is "safe" by default
```
acks = all(-1)
enable.idempotence = true
```

## Message compression at the producer level
```
compression.type can be none(default), gzip, lz4, snappy, zstd(kafka 2.1)
```
