from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'bbc_news_dag',
    default_args=default_args,
    description='A DAG to scrape BBC news articles',
    schedule_interval=timedelta(days=1),
)

def run_scrapy():
    subprocess.run(['scrapy', 'crawl', 'bbc'], check=True, cwd='/opt/airflow/scrapy_project')

run_python_project = PythonOperator(
    task_id='run_python_project',
    python_callable=run_scrapy,
    dag=dag,
)

