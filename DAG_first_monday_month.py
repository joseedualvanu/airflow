from airflow.models import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import pendulum

local_tz = pendulum.timezone("America/Montevideo")

default_args = {
    'email': ['integraciones@tata.com.uy'],
    'email_on_failure': True,
    'email_on_success': True
}

def check_if_monday():
    today = datetime.now(tz=local_tz)
    if today.day <= 7 and today.weekday() == 0:  # First 7 days and Monday
        return 'run_python_task'
    else:
        return 'skip_task'

dag = DAG(
    dag_id='DAG_NAME',
    default_args=default_args,
    start_date=datetime(2023, 7, 12, tzinfo=local_tz),
    schedule_interval='0 19 1-7 * *',
)

check_monday_task = BranchPythonOperator(
    task_id='check_if_monday',
    python_callable=check_if_monday,
    dag=dag
)

run_python_task = BashOperator(
    task_id='run_python_task',
    bash_command='python3.9 python_script.py',
    dag=dag
)

skip_task = BashOperator(
    task_id='skip_task',
    bash_command='echo "Skipping task."',
    dag=dag
)

check_monday_task >> run_python_task
check_monday_task >> skip_task