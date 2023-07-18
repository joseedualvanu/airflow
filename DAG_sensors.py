from airflow.contrib.sensors.file_sensor import FileSensor
from datetime import datetime

file_sensor_task = FileSensor(
    task_id='file_sensor_task',
    filepath='/path/to/your/file',
    poke_interval=60,  # Interval between file checks (in seconds)
    dag=dag
)

dependent_task = YourOperator(
    task_id='dependent_task',
    ...
    dag=dag
)

# Set the dependency of the dependent task on the file sensor task
dependent_task.set_upstream(file_sensor_task)
