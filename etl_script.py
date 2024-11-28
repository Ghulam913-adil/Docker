import pyodbc
import cx_Oracle
import pandas as pd
import pyodbc
import pypyodbc as odbc
from tqdm import tqdm
import time

# Define your SQL Server connection parameters
server = 'ADIL\\SQLEXPRESS'
database = 'master'

# Connection string for SQL Server using Windows Authentication
connection_string = f'Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};Trusted_Connection=yes;'

# Define your Oracle connection parameters
oracle_username = 'hr'
oracle_password = 'hr'
oracle_dsn = 'localhost:1521/orclpdb'  # e.g., 'localhost:1521/orcl'

try:
    # Simulate a connection process with a progress bar
    print("Attempting to connect to SQL Server...")
    for progress in tqdm(range(100), desc="Connecting to SQL Server", unit="%", ncols=80):
        time.sleep(0.02)  # Simulate some delay for each step in the progress bar

    # Attempt to establish a connection to SQL Server
    with pyodbc.connect(connection_string) as sql_connection:
        print("\nConnection to SQL Server successful!")

        # Create a cursor to execute SQL queries on SQL Server
        sql_cursor = sql_connection.cursor()

        # Define your SQL query to fetch data
        sql_query = """SELECT * FROM FinanceRecords;"""  # Modify this as needed

        # Execute the query
        sql_cursor.execute(sql_query)

        # Fetch all rows from the executed query
        rows = sql_cursor.fetchall()
        total_records = len(rows)  # Count the total records fetched
        print(f"Total records fetched from SQL Server: {total_records}")

        # Print the fetched records
        print("\nFetched records from SQL Server:")
        for row in rows:
            print(row)

        # Connect to the Oracle database
        oracle_connection = cx_Oracle.connect(oracle_username, oracle_password, oracle_dsn)
        print("Connection to Oracle database successful!")

        # Create a cursor to execute SQL queries on Oracle
        oracle_cursor = oracle_connection.cursor()
        rows_inserted = 0  # Initialize a counter for inserted rows
        
        # Use tqdm to show progress as we process each row for insertion
        with tqdm(total=total_records, desc="Inserting rows into Oracle", unit="row", ncols=80) as progress_bar:
            for row in rows:
                # Define your Oracle insert query
                insert_query = """INSERT INTO FinanceRecords (RecordID, TransactionDate, AccountNumber, TransactionType, Amount,
                Currency,Description,Category,CreatedAt,ModifiedAt) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)"""  # Modify column names and placeholders as needed
                
                # Execute the insert query
                oracle_cursor.execute(insert_query, row)  # Assuming row contains values for all columns

                # Update progress bar after each row is inserted
                progress_bar.update(1)
                rows_inserted += 1  # Increment the inserted rows counter

        # Commit the transaction to save changes
        oracle_connection.commit()
        print("Data insertion into Oracle database completed successfully!")
        print(f"Total rows inserted into Oracle database: {rows_inserted}")

except Exception as e:
    print("\nError:", e)

finally:
    # Close the Oracle cursor and connection
    if 'oracle_cursor' in locals():
        oracle_cursor.close()
    if 'oracle_connection' in locals():
        oracle_connection.close()
    print("Oracle connection closed.")