#!/usr/bin/env python
# encoding: utf-8
import json, requests
import psycopg2,os
from psycopg2 import Error
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify,request
app = Flask(__name__)

class Pripoj_do_db:
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="172.22.0.3",
                                      port="5432",
                                      database="postgres")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



@app.route('/')
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

@app.route('/user/request', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="172.22.0.3",
                                  port="5432",
                                  database="postgres")

# Create a cursor to perform database operations
    cursor = connection.cursor()
    # Executing a SQL query to insert data into  table
    insert_query = """ INSERT INTO kava (ID, login,pass,email) VALUES (default, '1', '1','1')"""
    cursor.execute(insert_query)
    connection.commit()
    print("1 Record inserted successfully")
    cursor.execute("SELECT id from kava ORDER BY ID DESC  LIMIT 1")
    record = cursor.fetchall()
    return jsonify(record)


# @app.route('/maschine', methods=['POST'])
# def create_record():
#     record = json.loads(request.data)
#     with open('/tmp/data.txt', 'r') as f:
#         data = f.read()
#     if not data:
#         records = [record]
#     else:
#         records = json.loads(data)
#         records.append(record)
#     with open('/tmp/data.txt', 'w') as f:
#         f.write(json.dumps(records, indent=2))
#     return jsonify(record)

app.run()