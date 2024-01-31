#Bacic or must needed dependencies to import to start the project
import os
import streamlit as st
import pandas as pd
from tabulate import tabulate

# For using LLM the necessary packages are imported
from langchain_community.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv,find_dotenv

#OpenAI API key which is already beign sorted and stored in other folder 
from apikey import apikey



#OpenAI API key
os.environ['OPENAI_API_KEY'] = apikey
load_dotenv(find_dotenv())


#title 
st.title("AI Assistant for Data Science 🤖")

#welcoming message 
st.write('Hello,👋🏼 I am your AI assistant and I am here to help your data science projects.')

# Explaination Sidebar
with st.sidebar:
    st.write('*Your Data Science Adventure Begins with an CSV file.*')
    st.caption('''**You may already know that every exiting data science journey start with a dataset.
            That's why I'd love for you to upload a CSV file . Once we have your data in hand , we'll
            dive into understanding it and have some fun exploring it. Then, we'll work toghether
            to shape your business challenges into a data science framework. I'llintroduce you to 
            collest machine learning models, and we'll use them to tackle your problem. 
            Sounds fun right!!**''')
    
    #divider is used to create a line between the two sections
    st.divider()
    
    #caption is used to add the text in the center
    st.caption("<p style = 'text-align:center'> Design And Developed by 🫱🏻‍🫲🏼: Japanjot Singh</p>" , unsafe_allow_html=True)

#Initialise the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False}

#Function to update the key in the session state 
def clicked(button):
    st.session_state.clicked[button] = True
st.button("let's get started", on_click=clicked, args=[1])
if st.session_state.clicked[1]:
    df = st.file_uploader('Upload your CSV file here', type="csv")
    if df is not None:
         df.seek(0)
         df = pd.read_csv(df , low_memory=False)

         #LLM model 
         llm = OpenAI(temperature = 0) 

         #Pandas agent 
         pandas_agent = create_pandas_dataframe_agent(llm,df,verbose=True)


         #Main Function
         def main(): 
           #display the dataset
           st.write("**Data Overvirw**")
           st.write("The first row of your dataset look like this:")
           head_data = pd.DataFrame(df.head())
           st.write(head_data)  
           #Preprocessing work starts from here!!
           st.write("**Preprocessing of Data**" )
           #check the shape of the dataset
           st.write("The shape of your dataset is:")
           st.write(df.shape) 
           #check the columns of the dataset
           st.write("The columns of your dataset are:")
           st.write(df.columns)  
           #check the datatypes of the dataset
           st.write("The datatypes of your dataset are:")
           st.write(df.dtypes)  
           #check the missing values in the dataset
           st.write("The missing values in your dataset are:")
           st.write(df.isnull().sum())  
           #check the unique values in the dataset
           st.write("The unique values in your dataset are:")
           st.write(df.nunique())  
           #check the duplicate values in the dataset
           st.write("The duplicate values in your dataset are:")
           st.write(df.duplicated().sum()) 
           #check the statistical values in the dataset
           st.write("The statistical values in your dataset are:")
           st.write(df.describe())  
           #check the correlation values in the dataset
           st.write("The correlation values in your dataset are:")
           st.write(df.corr()) 
           #check the skewness values in the dataset
           st.write("The skewness values in your dataset are:")
           st.write(df.skew()) 
           #check the kurtosis values in the dataset
           st.write("The kurtosis values in your dataset are:")
           st.write(df.kurt())
           # line chart for the data 
           st.write("The line chart for your dataset is:")
           user_column = st.selectbox("Select the column for line chart" , df.columns)
           st.line_chart(df , y = [user_column]) 

           # bar chart for the data
           st.write("The bar chart for your dataset is:")
           user_column = st.selectbox("Select the column for bar chart" , df.columns)
           st.bar_chart(df , y = [user_column])
           # area chart for the data
           st.write("The area chart for your dataset is:")
           user_column = st.selectbox("Select the column for area chart" , df.columns)
           st.area_chart(df , y = [user_column])
        
           #how to display special data in streamlit
           st.write("The Special description for your dataset is given below in the information section:")

           
         main()

         def df():
           description = st.info(pandas_agent.run(f"check the data and check is there any problem in the data{df}"))
           st.write(description)
           st.write("Is there any other issue in the dataset let's check!!")
           #solution = st.info(pandas_agent.run(f"if the dataset contains any other issue and provide a solution for that{df}"))
           #st.write(solution)
           st.balloons()
           return 
         df()

