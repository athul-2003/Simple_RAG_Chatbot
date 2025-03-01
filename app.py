import streamlit as st
import warnings
import logging
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA

# Disable warnings and info logs
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

# Streamlit App Title
st.set_page_config(page_title="RAG Chatbot", page_icon="📜", layout="wide")
st.title("📜 Simple RAG Chatbot - Chat with PDF")

# Sidebar for PDF upload
with st.sidebar:
    st.header("📄 Upload PDF")
    st.write("Upload a PDF document to chat with the content inside it.")
    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

    if uploaded_file and 'pdf_path' not in st.session_state:
        pdf_path = f"./{uploaded_file.name}"  # Save uploaded file locally
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.session_state.pdf_path = pdf_path
        st.success(f"📄 {uploaded_file.name} uploaded successfully!✅")

@st.cache_resource
def get_vectorstore(pdf_path):
    loaders = [PyPDFLoader(pdf_path)]
    # Create chunks, aka vector database–Chromadb
    index = VectorstoreIndexCreator(
        embedding=HuggingFaceEmbeddings(model_name='all-MiniLM-L12-v2'),
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    ).from_loaders(loaders)
    return index.vectorstore

# # Setup session state to hold the conversation
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # Display the conversation
# # st.header("Chat with your PDF")
# chat_container = st.container()
# with chat_container:
#     for message in st.session_state.messages:
#         st.chat_message(message['role']).markdown(message['content'])




# Setup a session state variable to hold all the old messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

if 'pdf_path' in st.session_state:
    prompt = st.chat_input("Ask a question about the PDF...")

    if prompt:
        st.chat_message('user').markdown(prompt)
        # Store the user prompt in state
        st.session_state.messages.append({'role':'user', 'content': prompt})

        groq_sys_prompt = ChatPromptTemplate.from_template("""You are very smart at everything, you always give the best, 
                                                the most accurate and most precise answers. Answer the following Question: {user_prompt}.
                                                Start the answer directly. No small talk please""")

        model = 'llama3-8b-8192'
        groq_chat = ChatGroq(
            groq_api_key=os.getenv('GROQ_API_KEY'),
            model_name=model
        )

        try:
            with st.spinner("Processing..."):
                vectorstore = get_vectorstore(st.session_state.pdf_path)
                if vectorstore is None:
                    st.error("Failed to load document")

                chain = RetrievalQA.from_chain_type(
                    llm=groq_chat,
                    chain_type='stuff',
                    retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
                )
                
                result = chain({"query": prompt})
                response = result["result"]  # Extract just the answer

                st.chat_message('assistant').markdown(response)
                st.session_state.messages.append({'role':'assistant', 'content': response})

        except Exception as e:
            st.error(f"An error occurred while processing your request: {str(e)}")
