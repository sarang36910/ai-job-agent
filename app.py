import streamlit as st
import psycopg2
import pandas as pd
import ollama


st.title("AI Job Market Intelligence Assistant")


# connect database

# from sqlalchemy import create_engine

# engine = create_engine("postgresql://postgres:123@localhost/job_agent")

# df = pd.read_sql("SELECT * FROM jobs", engine)
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:JobAgent%40123@db.idszbogxpqxoberjaoga.supabase.co:5432/postgres")

df = pd.read_sql("SELECT * FROM jobs", engine)




# summary

top_locations = df['location'].value_counts().head(10)

top_companies = df['company'].value_counts().head(10)

total_jobs = len(df)


summary = f"""

Total Jobs: {total_jobs}

Top Locations:

{top_locations}

Top Companies:

{top_companies}

"""


# input

question = st.text_input("Ask your question")


if st.button("Get Answer"):

    prompt = f"""

    You are job market expert.

    Here is summary:

    {summary}

    Answer:

    {question}

    """


    response = ollama.chat(

        model="llama3",

        messages=[{"role": "user", "content": prompt}]

    )


    st.write(response['message']['content'])
