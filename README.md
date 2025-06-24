# **UPSC & PCS AI-Powered Quiz Generator**

## 🚩 Problem Statement

Preparing for highly competitive exams like **UPSC** (Union Public Service Commission) and **PCS** (Provincial Civil Service) presents significant challenges:

* Limited access to quality practice materials
* Lack of immediate feedback and performance insights
* No adaptive learning to match individual proficiency levels
* Manual quiz creation is time-intensive
* Inadequate coverage across diverse subjects and topics

This project addresses these gaps with an **AI-driven quiz generation platform** that customizes and automates quiz creation for UPSC and PCS aspirants.

---

## 🎯 Use Cases & Industry Applications

### 🏫 Education & Test Preparation

* Online learning platforms
* Coaching institutes
* Self-paced study programs
* Assessment and mock test tools

### 🏛 Competitive Exam Training

* UPSC & PCS coaching centers
* Government job preparation hubs
* Public sector entrance training modules

### 🏢 Corporate & Skill-Based Assessment

* Employee evaluation platforms
* Professional skill development
* Knowledge retention testing
* Learning & development systems

---

## 🛠️ Tools & Technologies

### Core Stack

* **Python 3.8+** – Primary language
* **Streamlit** – Interactive web UI
* **Groq LLM API** – AI-powered question generation
* **Pandas** – Data manipulation and storage

### Libraries & Frameworks

* `langchain-groq`
* `pydantic`
* `python-dotenv`
* `streamlit`
* `pandas`

### Dev Environment

* **VSCode / PyCharm** – Recommended IDEs
* **Git** – Version control
* **Virtual Environment** – Isolation via `venv` or `conda`

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd upsc-pcs-quiz-generator
```

### 2. Create a Virtual Environment

```bash
conda create -p env python=3.10 -y
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Launch the Application

```bash
streamlit run app.py
```

---

## 🗂 Project Structure

```
├── main.py              # Streamlit app entry point
├── utils.py             # Utility functions for quiz generation
├── requirements.txt     # List of dependencies
├── .env                 # API keys and environment variables
├── results/             # Directory to store quiz results
└── README.md            # Project documentation
```

---

## 🚀 Features

### ✍️ Question Generation

* Multiple-choice questions
* Fill-in-the-blank type
* Difficulty level customization
* Topic-wise question selection

### 🧪 Quiz Management

* Interactive, responsive quiz interface
* Real-time scoring and feedback
* Track progress over time

### 📊 Result Analysis

* Score breakdown and performance insights
* Exportable quiz results
* Historical data tracking for revision planning

---

## 🔮 Planned Enhancements

### Technical Upgrades

* Add caching for faster response times
* Support multiple LLM providers
* Improve error handling & API reliability
* Introduce user authentication system

### New Features

* Add true/false, matching-type questions
* Integrate spaced repetition for long-term retention
* Implement quiz templates and topic-based analytics

### User Experience Enhancements

* Mobile-friendly and responsive UI
* Dark mode support
* Multi-language support
* User profile and quiz history tracking
* Smart difficulty adjustment engine

### Content & Integration

* Link quizzes to study resources
* Pre-built question banks for major subjects
* Topic suggestion system based on weak areas
* Collaborative quiz creation and sharing
* Peer performance comparison and leaderboard

---

This project aims to revolutionize how aspirants prepare for UPSC and PCS by combining **AI** with **interactivity**, **adaptability**, and **analytics**.


