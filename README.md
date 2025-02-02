# Gen AI App Using DeepSeek-R1 with Langchain and Ollama

## Overview

This project is a Gen AI application leveraging **DeepSeek-R1**, **Langchain**, and **Ollama** to provide advanced generative AI capabilities. The application integrates DeepSeek-R1 models with Langchain for efficient prompt engineering and Ollama for seamless model deployment and management.

## Features

- Integration with **DeepSeek-R1** for powerful AI model performance
- Use of **Langchain** for effective prompt management and chaining
- **Ollama** for model orchestration and deployment

## Prerequisites

- Python 3.11
- Ollama

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/lokendrasolanki/GenAi-with-Deepseek-r1.git
cd GenAi-with-Deepseek-r1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama from below link

[Ollama Download](https://ollama.com/download)

### 4. Dwonload the DeepSeek-R1 Model with Ollama

```bash
ollama run deepseek-r1:1.5b
```

Ensure the model is running correctly by checking the Ollama dashboard or logs:

## Usage

### Running the Application

```bash
streamlit run app.py
```

---

For more information, visit [Ollama Documentation](https://ollama.ai/docs) and [Langchain Documentation](https://docs.langchain.com/).
