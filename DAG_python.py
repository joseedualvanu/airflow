from airflow.models import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import pendulum
local_tz = pendulum.timezone("America/Montevideo")

default_args={
    'email': ['email@gmail.com.uy'],
    'email_on_failure': True,
    'email_on_success': True
}

dag = DAG(
    dag_id = 'Name_dag',
    schedule_interval = "00 09 * * *",
    default_args=default_args
)

python_task = BashOperator(
    task_id = 'Name_task',
    bash_command = 'python3.9 /ubication/script.py',
    start_date = datetime(2022,2,24,tzinfo=local_tz),
    dag = dag
)
