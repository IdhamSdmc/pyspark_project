### List of commands to exec kafka

```shell
docker exec -it --user root container_name /bin/bash 
docker exec -it pyspark_project-master-1 /bin/bash 
# Setup test environment

# Comandos a usar
kafka-topics --bootstrap-server kafka1:19092,kafka2:19093,kafka3:19094 --topic test-topic --create
kafka-topics --bootstrap-server kafka1:19092,kafka2:19093,kafka3:19094 --topic other-topic --create
kafka-topics --list --bootstrap-server kafka1:19092,kafka2:19093,kafka3:19094

kafka-console-consumer --topic test-topic --bootstrap-server kafka1:19092,kafka2:19093,kafka3:19094

kafka-console-consumer --topic other-topic --bootstrap-server kafka1:19092,kafka2:19093,kafka3:19094
kafka-console-consumer --topic abc-onprem-transactions --bootstrap-server kafka1:19092,kafka2:19093,kafka3:19094

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /src/streaming/read_transactions.py



# Inside the kafka container:
kafka-topics.sh --create --replication-factor 1 --bootstrap-server kafka1:9092 --topic test_topic

# LISTADO DE TOPICOS
kafka-topics.sh --bootstrap-server kafka1:9092 --list

kafka-topics.sh --list --bootstrap-server localhost:9092


# Producer

kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test_topic --property "parse.key=true" --property "key.separator=:"

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /src/read_test_stream.py

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /src/streaming/read_transactions.py

# Convert the jsons into parquet file
Unprotect the folder
sudo chmod -R 777 data/ 

## JSON to parquet job
spark-submit --deploy-mode client --master spark://spark:7077 --driver-memory 2G --executor-memory 2G transform_json_to_parquet.py


# Setup traffic_sensor topic
# Inside the kafka container:
kafka-topics.sh --create --replication-factor 1 --bootstrap-server localhost:9092 --topic traffic_sensor

# Test write
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 streaming/insert_traffic_topic.py

kafka-console-consumer.sh --topic traffic_sensor --bootstrap-server localhost:9092

kafka-console-consumer --topic test-topic --bootstrap-server kafka1:19092,kafka2:19093,kafka3:19094
kafka-console-consumer --topic other-topic --bootstrap-server kafka1:19092,kafka2:19093,kafka3:19094

# Test read
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 streaming/consume_traffic_topic.py

# Execute a general job
spark-submit --master spark://spark:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 <<job.py>>
```
