from dotenv import load_dotenv
load_dotenv() # load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#Configure the API KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Function to load Google Gemini Modle and provide SQL query as response

def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


# Function to retrieve query from the SQL database
def read_sql_query(sql,db):
    connection=sqlite3.connect(db)
    cursor=connection.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    connection.commit()
    connection.close()
    
    for row in rows:
        print(row)

    return rows


#Define the prompt

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION and MARKS \n\nFor Example, \nExample 1- How many entries of records are present?, the SQL command will look like this SELECT COUNT(*) FROM STUDENT ; \nExample2 - Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";

    also the SQL code should not have ``` in the beginning or end and sql word in output
"""
]

#Streamlit App

st.set_page_config(page_title="I can Retreive Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

#if submit button is fired

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    st.subheader("The SQL Query for the given question is:")
    st.subheader(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is:")
    for row in data:
        print(row)
        st.header(row)