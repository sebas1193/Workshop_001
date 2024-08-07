import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv
"""The problem was that the path to the credentials.env file was wrong.
 'cause it was missing the current directory,so the library dotenv couldn't find the file.
 Now, using the function os.path.dirname(__file__), we can get the current directory 
 and with the function os.path.join() we can concatenate the path to the credentials.env file.
 """
dotenv_path = os.path.join(os.path.dirname(__file__), '../../credentials.env')
load_dotenv(dotenv_path=dotenv_path)

#print(os.getenv("HOST"))

def create_table():
    try:
        #Connection to PostgreSQL
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port=os.getenv("PORT"),
            database=os.getenv("DATABASE")
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = conn.cursor()

        try:
            #Table Creation
            cur.execute(
                """
                CREATE TABLE candidates (
                    id SERIAL PRIMARY KEY,
                    FirstName VARCHAR(30) NOT NULL,
                    LastName VARCHAR(30) NOT NULL,
                    Email VARCHAR(70) NOT NULL,
                    Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    Country VARCHAR(40) NOT NULL,
                    YOE INT NOT NULL,
                    Seniority VARCHAR(40) NOT NULL,
                    Technology VARCHAR(60) NOT NULL,
                    CodeScore INT NOT NULL,
                    InterviewScore TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            print("Table 'candidates' created successfully.")
        except psycopg2.Error as e:
            print(f"Error creating the table: {e}")

        finally:
            cur.close()
            conn.close()
    
    except psycopg2.OperationalError as e:
        print(f"Error connecting to PostgreSQL: {e}")

#Funtion call
create_table()