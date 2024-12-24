# 📄 Research Paper Query Assistant

**A Streamlit-based application for advanced document retrieval and question answering.**  

---

## 🚀 Features  

- 🗂 **Document Embedding**: Embed research papers for efficient retrieval using FAISS and HuggingFace.  
- 🔍 **Question Answering**: Query your documents with precise answers using ChatGroq and custom prompts.  
- 📜 **PDF Support**: Load and process multiple PDF documents with ease.  
- ⚡ **Fast Retrieval**: Leverages vector-based search for quick access to relevant information.  
- 🌐 **User-Friendly Interface**: Powered by Streamlit for a seamless user experience.  

---

## 🛠️ Tech Stack  

- **Programming Language**: Python 🐍  
- **Web Framework**: Streamlit 🌟  
- **Language Models**: ChatGroq, HuggingFace Embeddings 🤖  
- **Vector Store**: FAISS 📊  
- **Document Processing**: PyPDFDirectoryLoader 📄  

---

## 📋 Requirements  

Make sure you have the following installed before running the project:  

- Python 3.8+ 🐍  
- Streamlit  
- FAISS  
- LangChain  
- HuggingFace Embeddings  
- GROQ API Key 🔑  

Install dependencies with:  

```bash  
pip install -r requirements.txt  
```  

---

## 🚀 Quick Start  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/Rahulagowda004/RETRIEVAL_AUGMENTED_GENERATION_BOT.git  
   ```  

2. **Navigate to the project directory**:  
   ```bash  
   cd RETRIEVAL_AUGMENTED_GENERATION_BOT  
   ```  

3. **Set up environment variables**:  
   Create a `.env` file in the root directory:  
   ```  
   GROQ_API_KEY=your_groq_api_key  
   HF_TOKEN=your_huggingface_api_token  
   ```  

4. **Run the application**:  
   ```bash  
   streamlit run app.py  
   ```  

5. **Access the app**:  
   Open your browser and go to: `http://localhost:8501` 🌐  

---

## 📊 Workflow  

1. **Document Embedding** 🗂️:  
   - Load PDF documents from the `Data` folder.  
   - Split documents into chunks and generate vector embeddings.  

2. **Question Answering** 💬:  
   - Input your query in the text box.  
   - The app retrieves relevant chunks and generates answers using ChatGroq.  

3. **Result Display** 📜:  
   - View answers and explore related document content with similarity scores.  

---

## 🛡️ Security  

- Ensure your API keys are stored securely in a `.env` file. 🔒  
- Use only trusted sources for PDFs to avoid malicious content.  

---

## 🎉 Demo  

![Demo Screenshot](demo_screenshot.png)  
*(Replace with your demo image or GIF)*  

---

## 🤝 Contributions  

Contributions are welcome! Feel free to:  

- Open issues 🐛  
- Submit pull requests 🚀  
- Share your feedback 💡  

---
