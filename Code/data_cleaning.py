from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("CustomerDataCleaning") \
    .getOrCreate()

df = spark.read.csv("data/customer_transactions.csv", header=True, inferSchema=True)

df_clean = df.dropna()

df_clean = df_clean.withColumn("total_amount", col("price") * col("quantity"))

df_clean.write.mode("overwrite").parquet("clean_data")
