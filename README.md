#### Introduction
This repository is sample project for using **ClickHouse** with **SqlAlchemy** and **Alembic**.

- **ClickHouse**: Column-oriented database management system

- **SqlAlchemy**: Popular ORM for interacting with SQL databases in python

- **Alembic**: Popular migration manager for python+sqlalchemy


#### Run ClickHouse Server

this project contains a **docker-compose.yaml** file that you can use to start clickhouse server. set your environment variables in **.env** file.

use this command to start clickhouse server:
```
$ docker compose up
```

#### Alembic Commands

To generate new migration:
```
$ alembic revision --autogenerate -m <migartion_name>
```
To update database with the last migration:
```
$ alembic upgrade head
```
