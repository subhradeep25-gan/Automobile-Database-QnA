from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from formated_few_shot import examples
import os

from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(google_api_key = os.environ["OPENAI_API_KEY"], temperature = 0.1)


def get_few_shot_db_chain():
    db_user = "root"
    db_password = "jojo12345"
    db_host = "localhost"
    db_name = "classicmodels"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)

    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    to_vectorise = [" ".join(example.values()) for example in examples]
    example_selector = SemanticSimilarityExampleSelector.from_examples(examples, embeddings, FAISS, k=2)

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="Question: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    similar_prompt = FewShotPromptTemplate(
        # We provide an ExampleSelector instead of examples.
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "prompt"]
    )

    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=similar_prompt)

    return chain

if __name__ == "__main__":
    chain = get_few_shot_db_chain()
    print(chain.run("Find the average credit limit for customers in the 'USA' country"))

