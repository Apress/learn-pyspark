from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator



args = {
    'owner': 'Pramod',    
    'start_date': airflow.utils.dates.days_ago(3),
    # 'end_date': datetime(2018, 12, 30),
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    # If a task fails, retry it once after waiting
    # at least 5 minutes
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    }


dag = DAG(
    'pramod_airflow_dag',
    default_args=args,
    description='A simple DAG',
    # Continue to run DAG once per day
    schedule_interval=timedelta(days=1)
)


# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag,
)



t1 >> t2

