-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(30) NOT NULL,
	last_name varchar(30) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

