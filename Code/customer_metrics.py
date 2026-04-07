from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count

spark = SparkSession.builder \
    .appName("CustomerMetrics") \
    .getOrCreate()

df = spark.read.parquet("clean_data")

customer_metrics = df.groupBy("customer_id").agg(
    sum("total_amount").alias("total_spent"),
    count("transaction_id").alias("total_orders")
)

customer_metrics.write.mode("overwrite").csv("customer_metrics")
