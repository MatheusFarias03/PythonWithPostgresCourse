import os
import psycopg2

def create_connection():
    return psycopg2.connection(os.environ.get("DATABASE_URI"))