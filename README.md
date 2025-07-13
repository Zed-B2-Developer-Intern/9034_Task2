# 🧠 Ollama Local AI Setup (Task 2)

This folder contains screenshots and notes related to setting up and running **Ollama** locally using Python and Postman.

## ✅ Task Completed

* Installed and configured Ollama on Windows
* Pulled and tested `llama3.2:1b` model
* Used Python to send prompts to Ollama via API
* Used Postman to test the API with JSON payload
* Verified offline capability after model download
* Uploaded screenshots to GitHub
* Created Python chatbot script (`ollama.py`)

## 🛠️ Installation & Setup

### 🧰 1. Install Ollama

Download and install from the official site:
👉 [https://ollama.com/download](https://ollama.com/download)

Once installed, verify using:

```bash
ollama --version
```

### 📥 2. Pull a Model

Use the following command to pull a small model:

```bash
ollama pull llama3.2:1b
```

You only need to do this **once** (models are saved locally).

### 🚀 3. Start the Ollama Server

```bash
ollama serve
```

This runs the API on `http://localhost:11434`

### 🧪 4. Test with Python or Postman

Use either the provided `ollama.py` script or Postman to interact with the local model.

---

## 📸 Screenshots

This folder includes:

* ✅ Ollama serve running
* ✅ Python chatbot working
* ✅ Postman request and response
* ✅ Model pull and storage confirmation

## 🛠 Technologies Used

* 🐍 Python 3.11
* 🐋 Ollama (offline LLM serving)
* 🧪 Postman for API testing
* 🖥️ Windows 11

## 📂 Directory

```
ollama/
   ollama.py
└── screenshot/
    ├── serve_running.png
    ├── postman_test.png
    ├── python_chat.png
    └── model_pull.png
```

## 🚀 How to Run Locally

1. Start Ollama server:

   ```bash
   ollama serve
   ```

2. Pull a model:

   ```bash
   ollama pull llama3.2:1b
   ```

3. Run Python chatbot script:

   ```bash
   python ollama.py
   ```

4. Or test with Postman at:

   ```
   http://localhost:11434/api/generate
   ```

## 🎬 Video Demo

Watch the complete demo here: [🔗 Click to Watch](https://www.example.com/ollama-demo) 

---

Feel free to explore and contribute!
