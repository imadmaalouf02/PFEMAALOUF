# RAG - Retrieval-Augmented Generation Application

## Description

This project is an interactive [**Streamlit** application](https://github.com/imadmaalouf02/RAG/blob/main/model_ollama/main.py) designed to enhance text generation tasks using document retrieval. Users can upload their own documents and choose from various language models to perform tasks like summarization, translation, or question-answering. The app integrates the power of multiple large language models (LLMs) to handle a wide variety of natural language processing (NLP) use cases.

## Features

- **Document Upload**: Upload your own PDF files.
- **Retrieval-Augmented Generation (RAG)**: Combines document retrieval with text generation.
- **Multiple Language Models**: Choose from Llama 2, Mistral, CodeLlama, and Llama 3.1 for generating responses.
- **Core Functionalities**:

  -[Document process](https://github.com/imadmaalouf02/RAG/blob/main/model_ollama/process_pdf.py) 
  - [Document Summarization](https://github.com/imadmaalouf02/RAG/blob/main/model_ollama/summarizer.py)
  - [Translation](https://github.com/imadmaalouf02/RAG/blob/main/model_ollama/translator.py)
  - [Question-Answering](https://github.com/imadmaalouf02/RAG/blob/main/model_ollama/question_handler.py)
- **Intuitive UI**: Simple and user-friendly interface built with Streamlit.
- **Customizable Output**: Select from available tasks to get the output you need (summarize, translate, or answer questions).

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/imadmaalouf02/RAG.git
   ```

2. Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes the following key libraries:

   - `pypdf`: For handling PDF files.
   - `streamlit`: For building the app’s web interface.
   - `beautifulsoup4`: For web scraping or text processing.
   - `langchain`, `langchain_ollama`, `langchain_chroma`, `langchain_community`: Various LangChain modules to enable advanced LLM functionalities.

3. (Optional) Install Streamlit via Conda if using Conda environment:

   ```bash
   conda install -c conda-forge streamlit
   ```

4. Run the Streamlit application:

   ```bash
   streamlit run model_ollama/main.py
   ```

5. Access the documentation:

   ```bash
   https://rag.readthedocs.io/en/latest/index.html#
   ```
## Usage

- Access the Streamlit interface in your browser.
- Upload a PDF document to analyze.
- Select the language model of your choice (Llama 2, Mistral, CodeLlama, Llama 3.1).
- Choose the task you want to perform (summarization, translation, or question-answering).
- View the results directly on the interface.

## Supported Language Models

- **Llama 2**: A versatile model for both text generation and comprehension tasks.
- **Mistral**: Efficient and fast for general text generation.
- **CodeLlama**: Tailored for code-related tasks and technical text.
- **Llama 3.1**: An advanced model optimized for complex text generation tasks.

## Documentation

For a more in-depth guide on how the application works, as well as an explanation of the code structure, please refer to the official documentation hosted on **ReadTheDocs**.

You can access the documentation [here](https://rag.readthedocs.io/en/latest/index.html#).


