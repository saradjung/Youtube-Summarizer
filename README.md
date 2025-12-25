# 🎥 YouTube Video Summarizer

An AI-powered web application built with **Django** that generates concise, readable summaries of YouTube videos using their transcripts.

Users can paste a YouTube URL and instantly get:
- TL;DR summaries
- Key points
- Concise summaries
- Detailed summaries
all through a clean, modern dark-themed UI.

---

## 🚀 Features

- 🔗 Accepts multiple YouTube URL formats
- 🧠 AI-powered(Gemini) summarization
- 📄 Supports different summary types (TLDR, Key Points, Concise, Detailed)
- 🕘 Summary history with pagination
- 🎨 Modern dark glassmorphism UI
- ▶️ Embedded YouTube player with fallback
- 📜 Expandable transcript view
- 🧾 Markdown-rendered summaries

---
## 🖼️ Preview

### 🏠 Home Page
![Home Page]<img width="896" height="764" alt="YT1" src="https://github.com/user-attachments/assets/8be512d2-4906-42eb-8277-c9ca03ecda24" />


### 📝 Summary Detail Page
![Summary Detail]<img width="866" height="1117" alt="yt2" src="https://github.com/user-attachments/assets/eb8e908c-a887-4a66-84e3-1f2a844e7383" />


### 📚 Summary History
![History Page]<img width="931" height="526" alt="yt3" src="https://github.com/user-attachments/assets/404a2438-ee8b-478b-b3cc-8589f8a3518b" />



---
## 🛠️ Tech Stack
- **Backend:** [Django](https://www.djangoproject.com/)
- **AI Brain:** [Google Gemini API](https://aistudio.google.com/) (`google-genai` SDK)
- **Data Extraction:** `youtube-transcript-api`
- **Frontend:** Bootstrap 5 & `django-markdownify`

## ⚙️ Installation & Setup

### 1️ Clone the repository
```bash
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
```

### 2 Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
### 3 Install dependencies
```bash
pip install -r requirements.txt
```
### 4 Run migrations
```bash
python manage.py migrate
```
### 5 Start the server
```bash
python manage.py runserver
```
### Author
Sarad Thapa
Computer Science Student | Django & ML Enthusiast
