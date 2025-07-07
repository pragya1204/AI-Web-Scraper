# AI Web Scraper with Streamlit + LangChain + Groq

A simple yet powerful AI-powered web scraper built with **Streamlit**, **LangChain**, **Selenium**, and **BeautifulSoup4**, leveraging the **Groq LLM** (`meta-llama-4 `) to extract and understand structured content from web pages.

---

## 🚀 Features

* Enter a URL and ask specific questions about the content (e.g., "Extract all product names")
* Uses `Selenium` to render and capture dynamic content
* Parses HTML using `BeautifulSoup` with `lxml`/`html5lib`
* AI-powered parsing with Groq + LangChain
* Streamlit UI for interactive input/output

---

## 🔧 Tech Stack

* **Frontend**: Streamlit
* **Backend/Parsing**: Selenium, BeautifulSoup4, lxml, html5lib
* **AI Model**: `meta-llama/llama-4-scout-17b-16e-instruct` via `langchain-groq`
* **Environment Handling**: python-dotenv

---

## 🛠 Installation

```bash
# Clone the repo
https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 📁 .env Configuration

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL_NAME=meta-llama/llama-4-scout-17b-16e-instruct
SBR_WEBDRIVER=https://your-webdriver-url:port  # If using a remote driver
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 📦 Requirements

Included in `requirements.txt`:

* streamlit
* langchain
* langchain-groq
* selenium
* beautifulsoup4
* lxml
* html5lib
* python-dotenv

---


