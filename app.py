# import streamlit as st
# import psycopg2
# import pandas as pd
# import ollama
# from groq import Groq



# st.title("AI Job Market Intelligence Assistant")


# # connect database

# # from sqlalchemy import create_engine

# # engine = create_engine("postgresql://postgres:123@localhost/job_agent")

# # df = pd.read_sql("SELECT * FROM jobs", engine)
# from sqlalchemy import create_engine

# engine = create_engine(
# "postgresql://postgres.idszbogxpqxoberjaoga:JobAgent%40123@aws-1-ap-northeast-1.pooler.supabase.com:6543/postgres"
# )


# df = pd.read_sql("SELECT * FROM jobs", engine)




# # summary

# top_locations = df['location'].value_counts().head(10)

# top_companies = df['company'].value_counts().head(10)

# total_jobs = len(df)


# summary = f"""

# Total Jobs: {total_jobs}

# Top Locations:

# {top_locations}

# Top Companies:

# {top_companies}

# """


# # input

# question = st.text_input("Ask your question")


# if st.button("Get Answer"):

#     prompt = f"""

#     You are job market expert.

#     Here is summary:

#     {summary}

#     Answer:

#     {question}

#     """

# # for ollama local
#     # response = ollama.chat(

#     #     model="llama3",

#     #     messages=[{"role": "user", "content": prompt}]

#     # )
# if st.button("Get Answer"):

#     question_lower = question.lower()

#     if "data analyst" in question_lower:

#         count = df[df['title'].str.contains("data analyst", case=False)].shape[0]

#         st.write(f"Total Data Analyst jobs available: {count}")

#     elif "location" in question_lower:

#         st.write(top_locations)

#     elif "company" in question_lower:

#         st.write(top_companies)

#     else:

#         st.write("Total jobs available:", total_jobs)


#     # st.write(response['message']['content'])
# # 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
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from groq import Groq


# ---------------------------
# PAGE TITLE
# ---------------------------

st.title("AI Job Market Intelligence Assistant")


# ---------------------------
# DATABASE CONNECTION (Supabase Pooler)
# ---------------------------

engine = create_engine(
    "postgresql://postgres.idszbogxpqxoberjaoga:JobAgent%40123@aws-1-ap-northeast-1.pooler.supabase.com:6543/postgres"
)

df = pd.read_sql("SELECT title, company, location, experience FROM jobs", engine)


# ---------------------------
# GROQ API SETUP
# ---------------------------

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# ---------------------------
# USER INPUT
# ---------------------------

question = st.text_input("Ask your question")


# ---------------------------
# AI RESPONSE
# ---------------------------

if st.button("Get Answer"):

    if question.strip() == "":
        st.warning("Please enter a question")
    else:

        # Convert dataframe to text (limit size for performance)
        data_summary = df.head(300).to_string()


        prompt = f"""
        You are an expert Job Market Analyst.

        Here is real job market data:

        {data_summary}

        Answer this question clearly and professionally:

        {question}
        """


        try:

            chat_completion = client.chat.completions.create(

                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],

                model="llama-3.3-70b-versatile",

            )

            answer = chat_completion.choices[0].message.content

            st.success(answer)


        except Exception as e:

            st.error("Error getting AI response")
            st.error(e)


# ---------------------------
# OPTIONAL DATA VIEW
# ---------------------------

if st.checkbox("Show Raw Data"):

    st.dataframe(df)

