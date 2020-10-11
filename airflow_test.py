from datetime import timedelta

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime,timedelta
from airflow.operators.python_operator   import PythonOperator

args = {
    'owner':'Airflow',
    'start_date':datetime(2020,10,11,hour=17),
    'end_date':datetime(2020,10,13,hour=10),
    'retries':1,
    'retry_delay':timedelta(seconds=20)

}

def sayhello(**kwargs):
    print(f"{kwargs['name']} is here")

dag = DAG('Airflow_Test',
default_args = args,
description = 'Sample airflow testing with parameters and api',
concurrency=5,
schedule_interval=timedelta(days=1),

)

with dag:
    run_first = PythonOperator(task_id="Run_first TaskID",
    python_callable = sayhello,
    op_kwargs = {"name":"Gangadhar","sayhello":"welcome to the world"}
    )