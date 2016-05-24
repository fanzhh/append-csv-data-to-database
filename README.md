# append-csv-data-to-database

In my work I have to import data from csv file to Postgresql DB frequently, so I write this code.

Usage: 
~~~~
ImportData.py TableName CsvFile.csv
~~~~
**ImportData.py** is this program self, **TableName** is the table name in Database, **CsvFile.csv** is the csv file contain data.

In my python code I use Postgresql and psycopg2, of course you can change it to other database.
