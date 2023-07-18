# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080
# backgrounds
nohup airflow webserver -p 8081 &

# start the scheduler
airflow scheduler

# stop airflow
systemctl stop airflow-scheduler
systemctl stop airflow-worker

# initiate again
systemctl start airflow-scheduler
systemctl status airflow-scheduler

# stop airflow
systemctl stop airflow-scheduler

# if you have workers
systemctl stop airflow-worker

# how to know the executor
# SequentialExecutor (Runs one task at a time)
# LocalExecutor (Runs on a single system) 
# CeleryExecutor (Uses a Celery backend as task manager)
cat airflow/airflow.cfg | grep "executor ="


