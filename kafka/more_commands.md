INTRODUCCIÓN COMMANDS
# CREACIÓN DE TOPICOS POR DEFAULT

```shell
kafka-topics --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --create
# CREACIÓN DE TOPICOS  PERSONALIZADO
kafka-topics --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --partitions 3 --replication-factor 3 --create
# DESCRIPCIÓN DEL TÓPICO
kafka-topics --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --describe
# LISTADO DE TOPICOS
kafka-topics --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --list
#  ALTER TOPIC
kafka-topics --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --alter --partitions 10
# ALTER REPLICATIONS FACTOR
kafka-reassign-partitions --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --reassignment-json-file /tmp/data/increase-replication-factor.json --execute
#  DELETE TOPIC
kafka-topics --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --delete


# CREACIÓN DE PRODUCTORES
kafka-console-producer --broker-list broker1:19092,broker2:19093,broker3:19094 --topic realtime-class
kafka-console-producer --broker-list broker1:19092,broker2:19093,broker3:19094 --topic realtime-class < /tmp/data/zipcodes.csv
# CREACIÓN DE 1 CONSUMIDOR LATEST BY DEAFULT
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class
kafka-console-consumer --bootstrap-server kafka1:19092 --topic test-topic
# CREACIÓN DE 1 CONSUMIDOR
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --from-beginning
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --from-beginning --group test
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class-b --from-beginning --offset 10
# CONSUMIR MENSAGES POR PARTICION
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --partition 0 --from-beginning
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --partition 1 --from-beginning
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --partition 2 --from-beginning

kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class-b --partition 0
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class-b --partition 1
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class-b --partition 2

kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class-b --group consumer-group-b
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class-b --group consumer-group-b
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class-b --group consumer-group-b

# CONSUMER GROUPS COMANDS
kafka-console-consumer --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --topic realtime-class --group group1 --from-beginning
kafka-consumer-groups --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --list
kafka-consumer-groups --bootstrap-server broker1:19092,broker2:19093,broker3:19094 --group group1 --describe

kafka-topics --bootstrap-server broker1:19092 --topic realtime-class --alter --partitions 31

kafka-topics -- zookeeper broker1:19092 --topic realtime-class --alter --partitions 31
```
