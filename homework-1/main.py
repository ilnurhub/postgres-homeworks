"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

DIRNAME = 'north_data'
