### Link guide/tutorial to install pyspark on Windows
[Spark Guide](https://sparkbyexamples.com/pyspark/how-to-install-and-run-pyspark-on-windows/)

### Link to see WebUI Spark
[WebUI acces](https://sparkbyexamples.com/spark/spark-web-ui-understanding/)

### Model Credit Risk
[Tutorial Model Credit Risk](https://deepnote.com/@hernanperci/Modelo-de-riesgo-de-credito-con-Python-96179012-2aa0-4358-8298-0733c576477b)

## Add Pyspark to python project
[Watch this tutorial](https://www.youtube.com/watch?v=j8AcYWQuv-M)

### Real-Time Logistics, Shipping, and Transportation with Apache Kafka
[Real-Time Logistics, Shipping, and Transportation with Apache Kafka](https://www.kai-waehner.de/blog/2022/09/29/real-time-logistics-shipping-transportation-with-apache-kafka/)


## Un vistazo rápido a Spark Structured Streaming + Kafka
[Un vistazo rápido a Spark Structured Streaming + Kafka](https://towardsdatascience.com/a-fast-look-at-spark-structured-streaming-kafka-f0ff64107325)


### SOLUCION
````text
Crear una aplicación que permita consumir eventos provenientes de los servidores de la empresa ABC, el cual emiten eventos de las transacciones realizadas por clientes en establecimientos comerciales.
La necesidad principal es poder repartir dichos eventos a diferentes áreas de la empresa ABC, principalmente al área de Salesforce. (la cantidad de eventos al día son de 5 milones/día aproximadamente).
Éste proceso en streaming deberá realizarse con Spark usando structure streaming del api Spark Streaming con codificación scala o Python.

Para el proceso número 1 (Kafka Producer client service): Crear o usar script de generación de eventos masivos que contenga o simule transacciones, éste como mínimo debe tener el campo “transaction_type” (credit, pos, payment).
	1.Definir cuantos millones de eventos se emitirá y porqué.


Para el proceso número 2 (Spark consumer Client): Crear el script en Python o scala usando Spark.
	2. Creación de consumidores usando spark structure streaming.
	3. Escribir en formato parquet y éste debe ser particionada por la columna transaction_type en una ruta hdfs src/resources/datalke/streamingLayer/${inputTopic}/transactions.

Para el proceso número 3. (Disponibilidad otras áreas)
	4. Lo eventos enviados al hdfs también deben ser enviado a un tópico de Kafka para que esté disponible para otras áreas. (topic-name = abc-onprem-transactions).
````
