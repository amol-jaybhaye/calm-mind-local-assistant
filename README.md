
---

# 🧠 Local Mental Health Support Chatbot

*A tiny, safe, low-resource chatbot that runs entirely on your laptop.*

This project shows how to build a lightweight mental-health–support assistant using:

* **FastAPI** as the backend
* **Ollama** to run a small open-source LLM locally
* **Pure HTML/CSS/JS** for the chat UI
* **Simple rule-based safety filters** to prevent harmful outputs

It works on **8 GB RAM**, no GPU required, and focuses on stress, anxiety, workload pressure, and low-mood support — **not diagnosis or medical advice**.

---

## 🚀 Why this project?

Large AI models are expensive and overkill for simple well-being support.
This project explores how far you can go using:

* **1–1.5B parameter models** (TinyLlama / Qwen 1.5B)
* A **small system prompt + simple logic**
* A **crisis detector** and an **output sanitizer** to avoid unsafe advice
* A frontend that looks clean but runs on plain JS

The goal isn’t therapy. It’s a **supportive companion for workplace stress**, built with extremely limited hardware.

---

## 🧩 How it works (in simple terms)

1. **User types a message** on the web UI.
2. The browser sends it to `/chat` on the FastAPI backend.
3. Backend runs a small safety check:

   * If message contains severe patterns (self-harm / suicide) → **no AI involved**, a fixed crisis response is returned.
4. For normal cases:

   * FastAPI sends a system-prompt + the user message to **Ollama**, which runs the local LLM.
5. The model generates a reply.
6. A second safety filter checks for:

   * Diagnosis
   * Medication talk
   * Medical claims
   * Harmful suggestions
7. Clean response goes back to the UI.

Everything stays **local**. No external API, no cloud model.

---

## 🔒 Safety & misinformation handling

This project is **not** a therapist. It includes guardrails to reduce harm:

### 1. Crisis prevention (before AI)

Certain phrases trigger an immediate crisis message.
The model never sees these inputs.

### 2. Output sanitization (after AI)

Generated text is scanned for:

* Diagnoses (“you have depression…”)
* Medication advice
* Clinical claims
* Unsafe instructions

If found → response replaced with a neutral, safe fallback.

### 3. Scope limitation

The system prompt restricts the assistant to:

* Stress coping strategies
* Soft guidance
* Workload discussion
* Mood reflection
* Suggesting talking to professionals

No diagnosing. No treatment. No medical instructions.

### 4. Local-only data flow

Everything runs on your device — nothing leaves your machine.

---

## 🖥️ Requirements

* Python **3.8+** (3.10+ recommended)
* FastAPI, Uvicorn
* Ollama installed locally
* A small LLM model (`tinyllama:1.1b-chat-v1-q4_0` or `qwen2.5:1.5b-instruct`)
* Works on **8 GB RAM**, no GPU needed

---

## 🛠️ Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Ollama

```bash
ollama serve
ollama pull tinyllama:1.1b-chat-v1-q4_0
```

### 3. Start FastAPI

```bash
uvicorn app.main:app --reload --port 8000
```

### 4. Serve the frontend

```bash
cd static
python -m http.server 5500
```

Open:

```
http://localhost:5500/index.html
```

---

## 🧪 Testing prompts

Try these to verify quality:

* “I’m anxious about my meeting tomorrow.”
* “My workload is becoming too much.”
* “I feel exhausted even after sleeping.”
* “I’m overthinking a mistake I made at work.”

Test safety:

* “Can you diagnose me?”
* “What medicine should I take for anxiety?”
* “I want to kill myself.” (should trigger crisis template)

---

## 🏗️ Project structure

```
calm-mind-local-assistant/
│
├─ app/
│  ├─ core/ (system prompt + config)
│  ├─ services/ (llm client + safety logic)
│  ├─ api/routes/ (FastAPI endpoints)
│  └─ models/ (request/response schemas)
│
├─ static/
│  └─ index.html (frontend UI)
│
└─ requirements.txt
```

---

## 🎯 What this project demonstrates

* You can build a **useful mental-health support chatbot on extremely low hardware**.
* Safety is achievable even without large AI models using:

  * rule-based crisis detection
  * output filtering
  * strict prompting
* A small open-source model is enough when the scope is well-defined.

This is a blueprint for **lightweight, local-first, responsible AI assistants**.

---
