import streamlit as st
import os 
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

llm = ChatGroq(api_key = groq_api_key, model_name = "Llama3-8b-8192") # ChatGroq is a wrapper around the GROQ API

prompt = ChatPromptTemplate(
    """
    Answer the question based on the provided context only.
    Please provide the most accurate response based on the question 
    <context>
    {context}
    <context>
    Question:{input}
    """
)

def create_vector_embeddings():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OllamaEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("Data") ##data ingestion
        st.session_state.docs = st.session.loader.load() #document loading
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 200) #chunking
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50]) #text splitting
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings) #vector embeddings


user_prompt = st.text_input("Enter you query regarding the research paper")

if st.button("Document embedding"):
    create_vector_embeddings()
    st.write("Vector Database in ready")
    
import time 

if user_prompt:
    document_chain = create_stuff_documents_chain(llm,prompt)
    retriever = st.session_state.vectors.as_retriever()
    retriever_chain = create_retrieval_chain(retriever, document_chain)
    
    start = time.process_time()
    response = retriever_chain.run({'input':user_prompt})
    print(f"response time: {time.process_time() - start}")
    
    st.write(response['answer'])
    
    #with a streamlit expander
    with st.expander("Document similarity search"):
        for i, doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write('-------------------')