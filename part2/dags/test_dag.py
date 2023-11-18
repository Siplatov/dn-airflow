from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator


dag = DAG(
    'test_dag',
    description='Тестируем git-sync',
    schedule_interval=None,
    start_date=datetime(2023, 11, 15),
    catchup=False
)


hello_world_task = BashOperator(
    task_id='hello_world_task',
    bash_command='echo Hello world!',
    dag=dag
)

hello_world_task