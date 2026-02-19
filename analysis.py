import psycopg2
import pandas as pd


conn = psycopg2.connect(

    host="localhost",
    database="job_agent",
    user="postgres",
    password="123"

)


query = "SELECT * FROM jobs"


df = pd.read_sql(query, conn)


conn.close()


print("\nTotal Jobs:", len(df))


print("\nTop Companies:")

print(df['company'].value_counts().head(10))


print("\nTop Locations:")

print(df['location'].value_counts().head(10))


print("\nSample Data:")

print(df.head())
