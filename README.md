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

## Message compression at the broker/topiv level
```
compression.type = producer(default) => broker writes it directly to the topics log file without recompressing the data

compression.type = none => all batches are decompressed by the broker

compression.type = lz4 => if it is matching the producer setting, data is stored on disk as is / if its different compression setting, batches are decompressed by the broker and then recompressed using the compression algorithm specified

```

## Improve batching mechanism
```
max.in.flight.requests.per.connection = 5 => up to 5 message batches being in flight(being sent between the producer and the broker) at most

linger.ms (default = 0) => how long to wait until we send a batch.

batch.size => if a batch is filled before linger.ms, increase the batch size
```

## Producer partitioner when key=null
```
- Round Robin => for kafka 2.3 and below
- Sticky Partitioner => for kafka 2.4 and above : we stick to a partition until the batch is full or linger.ms has elapsed and after sending the batch, the partition that is sticky changes.
```

## max.block.ms & buffer.memory
```
if the producer produces faster than the broker can take, the records will be buffered in memory

max.block.ms => the producer has filled up its buffer, .send() will block,the broker is not accepting any new data
```

## delivery semantics
```
- At most once => if the processing goes wrong, the message will be lost(it won't be read again)
- At least once => offsets are commited after the message is processed(make sure your processing is idempotent!)
```

## Schema Registery
```json
{
	"type": "record",
	"name": "myrecord",
	"fields": [
		{
			"name": "f1",
			"type": "string"
		},
		{
			"name": "f3",
			"type": "int",
			"default": 0
		}
	]
}
```
