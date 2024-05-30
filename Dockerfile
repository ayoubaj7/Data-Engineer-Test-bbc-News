FROM apache/airflow:2.5.1

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY dags /opt/airflow/dags

COPY scrapy_project /opt/airflow/scrapy_project

WORKDIR /opt/airflow/scrapy_project


