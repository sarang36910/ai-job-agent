# 🚀 AI Job Market Intelligence Assistant

An end-to-end **AI-powered job market analytics system** that automatically collects job data, stores it in a cloud database, and provides intelligent insights through a web application.

---

# 📌 Project Overview

This project is designed to analyze the **real-time job market** using automation and AI.

It:

* Scrapes job listings from Naukri
* Stores data in a cloud database (Supabase)
* Uses AI (Groq LLM) to answer user questions
* Provides a web interface using Streamlit
* Runs automatically using scheduled pipelines

---

# 🧠 Key Features

✅ Automated job scraping (multi-role, multi-page)
✅ Cloud database storage (Supabase PostgreSQL)
✅ AI-powered question answering (Groq LLM)
✅ Interactive web app (Streamlit)
✅ Live updating system (scheduler / automation)
✅ Duplicate prevention using unique constraints
✅ Scalable architecture for large datasets

---

# 🏗️ System Architecture

```
Job Portal (Naukri)
        ↓
Playwright Scraper (Python)
        ↓
Proxy Layer (Anti-blocking)
        ↓
Supabase (Cloud Database)
        ↓
Streamlit App (Frontend)
        ↓
Groq AI (LLM for Insights)
        ↓
User (Web Interface)
```

---

# ⚙️ Tech Stack

* **Python**
* **Playwright** (Web Scraping)
* **PostgreSQL (Supabase)** (Database)
* **Streamlit** (Web App)
* **Groq API (Llama Models)** (AI)
* **GitHub Actions / Scheduler** (Automation)
* **SQLAlchemy & Psycopg2** (DB Connection)

---

# 📊 Data Collected

Each job record contains:

* Job Title
* Company Name
* Experience Required
* Location
* Job Link
* Scraped Timestamp

---

# 💡 Example Questions You Can Ask

* How many data analyst jobs are available?
* Which location has the highest demand?
* Which company is hiring the most?
* Which role is trending in the market?
* Where should I move for better opportunities?

---

# 🖥️ Web App

The application provides a simple interface where users can:

* Ask questions in natural language
* Get AI-generated insights
* Explore job trends dynamically

---

# 🔄 Automation

The system supports:

* Scheduled scraping (daily updates)
* Continuous data growth
* Real-time insights based on latest data

---

# 🔐 Security

* API keys are stored using **Streamlit Secrets**
* Sensitive data is not exposed in code
* Database connection is secured

---

# 🚀 How to Run Locally

### 1. Clone repository

```
git clone https://github.com/your-username/ai-job-agent.git
cd ai-job-agent
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run scraper

```
python large_scraper.py
```

---

### 4. Run app

```
streamlit run app.py
```

---

# 🌐 Deployment

* App deployed on Streamlit Cloud
* Database hosted on Supabase
* AI powered by Groq API

---

# 📈 Future Improvements

* Salary extraction and analysis
* Skill demand detection
* Job recommendation system
* Resume-job matching AI
* Real-time dashboards with charts

---

# 👨‍💻 Author

**Sarange**

Data Analyst | Aspiring Data Scientist

---

# ⭐ Why This Project Matters

This project demonstrates:

* Real-world data engineering skills
* AI integration with production systems
* End-to-end system design
* Automation and scalability

It goes beyond traditional dashboards and showcases a **complete intelligent data system**.

---
