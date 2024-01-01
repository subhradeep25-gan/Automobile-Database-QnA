
# Automobile: Database QnA

This is an end to end LLM project based on OpenAI and Langchain. We are building a system that can talk to MySQL database. 
User asks questions in a natural language and the system generates answers by converting those questions to an SQL query and
then executing that query on MySQL database. 
# Database
The system is intelligent enough to generate accurate queries for given question and execute them on MySQL database

## Project Highlights

- The database belongs to a automobile distributor selling cars of various brands such as Harley Davidson, Ford, Ferrari, Mercedes and many more.
- Their products, orders, customers and employees data is stored in a MySQL database.
- We will build an LLM based question and answer system that will use following,
  - OpenAI LLM
  - Hugging face embeddings
  - Streamlit for UI
  - Langchain framework
  - FAISS as a vector store
  - Few shot learning
- In the UI, store manager will ask questions in a natural language and it will produce the answers


## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/subhradeep25-gan/Automobile-Database-QnA
```
2.Navigate to the project directory:

```bash
  cd Automobile-Database-QnA
```
3.Acquire an api key through openai.com and put it in .env file

```bash
  OPENAI_API_KEY="your_api_key_here"
```
4. For database setup, run database/classicmodels.sql in your MySQL workbench

## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser where you can ask questions

## Sample Questions
  - What is the total quantity sold and revenue for each product in the 'Vintage Cars' product line?
  - Find the average credit limit for customers in the 'USA' country.
  - Show the total revenue generated from orders shipped to the 'Germany' country.
  - Find the top 5 customers with the highest credit limits.
  
## Project Structure

- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- formated_few_shot.py: Contains few shot prompts
- .env: Configuration file for storing your OpenAI API key.
