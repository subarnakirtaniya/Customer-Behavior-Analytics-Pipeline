from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    "customer_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily"
)

task1 = BashOperator(
    task_id="clean_data",
    bash_command="python pyspark_jobs/data_cleaning.py",
    dag=dag
)

task2 = BashOperator(
    task_id="transform_data",
    bash_command="python pyspark_jobs/customer_metrics.py",
    dag=dag
)

task3 = BashOperator(
    task_id="load_postgres",
    bash_command="python load_to_postgres.py",
    dag=dag
)

task1 >> task2 >> task3

