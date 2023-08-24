import pyspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

# Definir constantes
KAFKA_BOOTSTRAP_SERVERS = "kafka1:19092,kafka2:19093,kafka3:19094"
KAFKA_TOPIC = "test-topic"
KAFKA_TOPIC1 = "other-topic"

# Definir el esquema de los datos
SCHEMA = StructType([
    StructField("transaction_id", IntegerType()),
    StructField("transaction_type", StringType()),
    StructField("transaction_amount", IntegerType()),
    StructField("transaction_timestamp", TimestampType())
])

# Crear una sesión de Spark
spark = SparkSession.builder.appName("KafkaToKafka").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Leer datos desde Kafka
kafka_df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
    .option("subscribe", KAFKA_TOPIC) \
    .load()

# Convertir el valor a una columna de tipo String
value_df = kafka_df.select(F.col("value").cast("STRING"))

# Parsear el JSON y seleccionar columnas
parsed_df = value_df.select(F.from_json(F.col("value"), SCHEMA).alias("value_json"))
selected_df = parsed_df.selectExpr(
    "value_json.transaction_id as transaction_id",
    "value_json.transaction_type as transaction_type",
    "value_json.transaction_amount as transaction_amount",
    "value_json.transaction_timestamp as transaction_timestamp"
)

# Escribir los datos en el tópico de Kafka
write_query = selected_df.writeStream \
    .format("kafka") \
    .outputMode("append") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
    .option("topic", KAFKA_TOPIC1) \
    .option("checkpointLocation", "/tmp/kafka-to-kafka-checkpoint") \
    .start()

write_query.awaitTermination()
