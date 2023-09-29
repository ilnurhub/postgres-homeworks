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
