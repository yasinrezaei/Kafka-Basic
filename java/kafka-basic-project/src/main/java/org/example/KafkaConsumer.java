package org.example;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.common.serialization.StringDeserializer;


import java.time.Duration;
import java.util.Collections;
import java.util.Properties;


public class KafkaConsumer {
    public static void main(String[] args) {
        //kafka consumer
        org.apache.kafka.clients.consumer.KafkaConsumer<String,String> consumer = createKafkaConsumer();
        System.out.printf("Start Consuming ...");
        consumer.subscribe(Collections.singleton("wikimedia_recent_change"));
        while (true){
            ConsumerRecords<String,String> records = consumer.poll(Duration.ofMillis(3000));
            int recordCount = records.count();
            for(ConsumerRecord<String,String> record:records){
                System.out.printf("record :%s",record);
            }
        }
    }
    private static org.apache.kafka.clients.consumer.KafkaConsumer<String,String> createKafkaConsumer(){
        String bootstrapServers = "localhost:29092";
        String groupId = "java-app";


        //create consumer configs
        Properties properties = new Properties();
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG,bootstrapServers);
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.GROUP_ID_CONFIG,groupId);
        properties.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG,"latest");

        //create consumer
        return new org.apache.kafka.clients.consumer.KafkaConsumer<>(properties);
    }
}


