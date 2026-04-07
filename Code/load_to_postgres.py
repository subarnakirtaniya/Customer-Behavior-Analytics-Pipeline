import pandas as pd
import psycopg2

conn = psycopg2.connect(
    database="salesdb",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

df = pd.read_csv("customer_metrics.csv")

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO customer_metrics
        VALUES (%s, %s, %s)
    """, (row.customer_id, row.total_spent, row.total_orders))

conn.commit()

