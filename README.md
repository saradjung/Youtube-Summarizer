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
![Home Page](<img width="899" height="849" alt="image" src="https://github.com/user-attachments/assets/7a22a312-934c-48ff-b60d-1d34f96dc7a8" />)

### 📝 Summary Detail Page
![Summary Detail](<img width="882" height="1124" alt="image" src="https://github.com/user-attachments/assets/85478192-d2b3-425b-bd2b-d5cad4115fbd" />)

### 📚 Summary History
![History Page](<img width="891" height="488" alt="image" src="https://github.com/user-attachments/assets/7c83b041-dd81-4f57-b3fb-eb971d8914a5" />)



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
