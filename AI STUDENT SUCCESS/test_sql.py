import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=StudentSuccessDB;"
    "Trusted_Connection=yes;"
)

print("SQL Server connected successfully!")

connection.close()