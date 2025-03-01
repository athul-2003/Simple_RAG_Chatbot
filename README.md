# 📝 Simple RAG Chatbot - Chat with Your PDF

## 📖 Project Overview
This is a Retrieval-Augmented Generation (RAG) chatbot built with Streamlit. The chatbot lets you upload a PDF document and ask questions about its content. It reads and understands the PDF, providing precise and accurate answers using advanced language models.

## ❓ Problem Statement
Reading long PDF documents and finding specific information can be time-consuming and frustrating. This chatbot solves that problem by letting users interact with PDF content directly — ask questions and get relevant, well-structured answers in seconds.

## 🚀 Demo Video


https://github.com/user-attachments/assets/e2911ed9-85c2-4c74-aee0-ec48462e8ce5



## 🧑‍💻 Tech Stack
- **Python** 🐍
- **Streamlit** 🌐 (Frontend)
- **Langchain** 🧠 (RAG Implementation)
- **Groq API (LLaMA 3 Model)** 💬
- **Hugging Face Embeddings** 🖼️ (all-MiniLM-L12-v2)
- **PyPDFLoader** 📄 (PDF Parsing)
- **ChromaDB** 🗂️ (Vector Database)

## 📝 Requirements
Create a `requirements.txt` file with the following:
```
streamlit
langchain
langchain_community
langchain_core
langchain_groq
transformers
chromadb
sentence-transformers
PyPDF2
```

## 🏗️ How to Set Up
1. **Clone the Repository:**
```bash
git clone https://github.com/athul-2003/Simple_RAG_Chatbot
cd Simple_RAG_Chatbot
```
2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```
3. **Set Up Environment Variable:**
Make sure you have your Groq API key set:
```bash
export GROQ_API_KEY='your-api-key-here'
```
4. **Run the App:**
```bash
streamlit run app.py
```

## 💡 How It Works
1. **Upload a PDF:** Use the sidebar to upload a PDF document.
2. **Ask Questions:** Type a question related to the PDF content.
3. **Get Smart Answers:** The chatbot fetches precise and context-aware responses.

## 🗂️ Project Structure
```
.
├── app.py                # Main Streamlit App
├── requirements.txt      # Python Dependencies
```

## ❗ Known Issues
- Ensure your PDF contains selectable text (not just scanned images)
- The app may take time for large PDF documents

## 📝 Future Enhancements
- Support for multiple PDF uploads
- Enhanced document search capabilities(ie supports complex documents)
- More language model options

## 🤝 Contributing
Pull requests and feedback are welcome! Let’s build something awesome together.

---

📧 For any questions, feel free to reach out!

---

👨‍💻 Created by **H Athulkrishnan**  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/h-athulkrishnan)
