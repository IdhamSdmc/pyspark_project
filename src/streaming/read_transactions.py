import pyspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
import time

SCHEMA = StructType([
    StructField("transaction_id", IntegerType()),
    StructField("transaction_type", StringType()),
    StructField("transaction_amount", IntegerType()),
    StructField("transaction_timestamp", TimestampType())
])

KAFKA_BOOTSTRAP_SERVERS = "kafka1:19092,kafka2:19093,kafka3:19094"
KAFKA_TOPIC = "transactions-topic"
KAFKA_TOPIC1 = "abc-onprem-transactions"

# Create a Spark session
spark = SparkSession.builder.appName("read_transactions").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Read the events from Kafka
df1 = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
    .option("subscribe", KAFKA_TOPIC) \
    .load()

value_df = df1.select(F.col("value").cast("STRING"))

value_df1 = value_df.withColumn("value_json", F.from_json(F.col("value"), SCHEMA))

value_df2 = value_df1.select(
    F.col("value_json.transaction_id").alias("transaction_id"),
    F.col("value_json.transaction_type").alias("transaction_type"),
    F.col("value_json.transaction_amount").alias("transaction_amount"),
    F.col("value_json.transaction_timestamp").alias("transaction_timestamp")
)

value_df3 = value_df2.groupBy(F.col("transaction_type")).sum("transaction_amount")

# query = value_df2.writeStream \
#     .format("console") \
#     .outputMode("append") \
#     .option("truncate", "false") \
#     .start()


# Write to HDFS
value_df2.writeStream.outputMode("append").partitionBy("transaction_type").format("parquet") \
    .option("path", f"hdfs://namenode:9000/datalake/streamingLayer/{KAFKA_TOPIC}/transactions") \
    .option("failOnDataLoss", "false") \
    .option("checkpointLocation", "/tmp/transactions") \
    .start()


#Read from HDFS
df_traffic_stream = spark.readStream.format("parquet") \
    .schema(SCHEMA) \
    .load(f"hdfs://namenode:9000/datalake/streamingLayer/{KAFKA_TOPIC}/transactions") \
    .withColumn("value", F.to_json( F.struct(F.col("*")) ) ) \
    .withColumn("key", F.lit("key")) \
    .withColumn("value", F.encode(F.col("value"), "iso-8859-1").cast("binary")) \
    .withColumn("key", F.encode(F.col("key"), "iso-8859-1").cast("binary")) \

# Write the stream to the topic
query = df_traffic_stream.select(
    F.col("key"),
    F.col("value")
).writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
    .option("topic", KAFKA_TOPIC1) \
    .option("checkpointLocation", "/tmp/nuevo2") \
    .start() \
    .awaitTermination()

query.awaitTermination()


# Send the events to another Kafka topic

# df_traffic_stream.select(
#     F.col("transaction_id"),
#     F.col("transaction_type"),
#     F.col("transaction_amount"),
#     F.col("transaction_timestamp")
# ).writeStream \
#     .format("console") \
#     .outputMode("append") \
#     .option("truncate", "false") \
#     .start()





