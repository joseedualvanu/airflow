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
    schedule_interval = "00 0-9 * * *",
    default_args = default_args
)

python_task = BashOperator(
    task_id = 'Name_task',
    bash_command = '''
    # Ejecutar PDI 9.0
    export _KITCHEN="/Pentaho_9.0_CE/pdi-ce-9.0.0.0-423/data-integration";
    # job's folder
    # level=Basic
    $_KITCHEN/kitchen.sh -file="/JobsFolder/Job_name.kjb" -level=Basic -logfile=/logs_folder/File_name.log
    ''',
    start_date = datetime(2022,2,24,tzinfo=local_tz),
    dag = dag
)
