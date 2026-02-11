# 📰 Inshorts Clone — Real-Time News Web App

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=Streamlit\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![NewsAPI](https://img.shields.io/badge/NewsAPI-2B3137?style=for-the-badge\&logo=google-news\&logoColor=white)

A clean, fast, and interactive **Inshorts-style News Aggregator Web App** built using **Python** and **Streamlit**, powered by real-time data from **NewsAPI.org**. The app shows one article at a time with an image, short description, and navigation controls (Previous / Next) plus a link to read the full article.

---

## 🌐 Live Demo

**Try it now:**
[https://inshorts-clone-week-06.streamlit.app/](https://inshorts-clone-week-06.streamlit.app/)

---

## ✨ Features

* 📰 Real-time news fetching using NewsAPI
* 📱 Inshorts-style interface — one article at a time
* ⬅️ ➡️ Next & Previous navigation (session-state based)
* 🔗 Read Full Article button linking to original source
* 🖼 Image, title and short description display
* ⚡ Lightweight, fast, and mobile friendly
* ✅ Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack & Tools

* **Language:** Python
* **Web UI:** Streamlit
* **HTTP:** requests
* **API:** NewsAPI.org
* **Deployment:** Streamlit Cloud

---

## 📂 Project Structure

```
Inshorts-Clone/
│
├── app.py              # Main Streamlit app (UI + navigation)
├── news_api.py         # Logic to fetch news from NewsAPI
├── config.py           # API config (reads env / secret)
├── requirements.txt    # Dependencies
├── runtime.txt         # Python runtime for Streamlit Cloud (e.g. python-3.11)
└── README.md           # This file
```

---

## 💻 Run Locally (Quick Start)

1. **Clone the repository**

```bash
git clone https://github.com/Wajid0005/inshorts-clone.git
cd inshorts-clone
```

2. **Create & activate a virtual environment (recommended)**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your NewsAPI key**

You have two safe options:

**Option A — Local config (quick & simple)**
Open `config.py` and add your key (not recommended for public repos):

```python
API_KEY = "your_newsapi_key_here"
BASE_URL = "https://newsapi.org/v2/everything"
```

**Option B — Environment variable (recommended)**
Export an environment variable and read it from `config.py`:

```bash
# Windows (PowerShell)
$env:NEWS_API_KEY="your_newsapi_key_here"

# macOS / Linux
export NEWS_API_KEY="your_newsapi_key_here"
```

Then `config.py` should use `os.getenv("NEWS_API_KEY")`.

5. **Run the app**

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) if the browser does not open automatically.

---

## 🔒 Deploying to Streamlit Cloud

1. Ensure your repo root contains:

   * `app.py`, `news_api.py`, `config.py`, `requirements.txt`, `runtime.txt`
2. `requirements.txt` (recommended minimal):

```
streamlit==1.32.0
requests==2.31.0
```

3. `runtime.txt` — force a supported Python runtime (example):

```
python-3.11
```

4. Add your API key to Streamlit Cloud secrets:

   * App → Settings → Secrets
   * Add `NEWS_API_KEY="your_newsapi_key_here"`

5. Ensure `config.py` reads from the environment:

```python
import os
API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"
```

6. Deploy or reboot the app in Streamlit Cloud. The live URL will be provided by Streamlit.

---

## 🧭 How it works (brief)

1. `news_api.py` calls NewsAPI (`/v2/everything`) with query parameters (q, language, sortBy, pageSize).
2. `get_news()` returns a list of article dicts (`title`, `description`, `url`, `urlToImage`, ...).
3. `app.py` stores the current article index in `st.session_state` and shows one article at a time.
4. Buttons change the index and Streamlit re-renders the selected article.

---

## ✅ Notes & Troubleshooting

* If you get **401 / apiKeyMissing** on deployment, double-check Streamlit Cloud secrets and ensure `config.py` reads `NEWS_API_KEY` from the environment.
* If deployment fails with an installer error, confirm:

  * `requirements.txt` is in the **repo root**.
  * `runtime.txt` specifies a supported Python version (e.g., `python-3.11`).
  * Keep `requirements.txt` minimal — Streamlit will pull its internal dependencies.
* Use the `everything` endpoint when `top-headlines` returns zero results for certain country+category combos on free plans.

---

## 🔮 Future Improvements

* Category selection and filters (Business, Tech, Sports, etc.)
* Bookmarking and history
* Dark mode / improved UI styling
* AI-generated summaries (optional)
* Pagination or infinite scroll
* User personalization and save-for-later

---

## 🎥 Reference

Built with guidance from Campus X tutorial:
[https://youtu.be/b-YBvPmCTew](https://youtu.be/b-YBvPmCTew)

---

## 👨‍💻 Author

**Wajid Iqbal**
GitHub: [Github](https://github.com/Wajid0005)
LinkedIn: *[LinkedIn](https://www.linkedin.com/in/wajid-iqbal-629770327/)*
