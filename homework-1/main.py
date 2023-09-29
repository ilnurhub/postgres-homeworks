"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

DIRNAME = 'north_data'


def create_file_path(filename):
    """
    Создает относительный путь до заданного файла из папки homework-1
    """
    f_path = os.path.join(DIRNAME, filename)
    return f_path


customers_file_path = create_file_path('customers_data.csv')
employees_file_path = create_file_path('employees_data.csv')
orders_file_path = create_file_path('orders_data.csv')

with psycopg2.connect(host='localhost', database='north', user='postgres', password='GoldSa1mon!') as conn:
    with conn.cursor() as cur:
        with open(customers_file_path, 'r', encoding='utf-8') as file:
            data = csv.DictReader(file)
            for customer_data in data:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                            (customer_data['customer_id'], customer_data['company_name'], customer_data['contact_name']))

conn.close()
