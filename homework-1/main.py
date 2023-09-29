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

        with open(employees_file_path, 'r', encoding='utf-8') as file:
            data = csv.DictReader(file)
            for employee_data in data:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                            (employee_data['employee_id'], employee_data['first_name'], employee_data['last_name'],
                             employee_data['title'], employee_data['birth_date'], employee_data['notes']))

        with open(orders_file_path, 'r', encoding='utf-8') as file:
            data = csv.DictReader(file)
            for order_data in data:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                            (order_data['order_id'], order_data['customer_id'], order_data['employee_id'],
                             order_data['order_date'], order_data['ship_city']))

conn.close()
