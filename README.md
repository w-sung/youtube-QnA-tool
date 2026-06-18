Ask questions about any YouTube video. Paste a URL, type your question, and get an answer based on the video's transcript. Uses Groq ai api.

**Tech used:** Python · Streamlit · Groq API (Llama 3.1) · youtube-transcript-api

**Prerequisites:** Python 3.8+

# How to install:

**1. Clone the repo**

`git clone https://github.com/w-sung/Youtube-QnA-Tool.git
cd Youtube-QnA-Tool`

**2. Install dependencies**

`pip install streamlit youtube-transcript-api groq`

**3. Set up your API key**

Create a .streamlit/secrets.toml file with this line:

`GROQ_API_KEY = "your-key-here"`

Fill in the key with a free API key at console.groq.com.

**4. Run the app by pasting into terminal:**

`python -m streamlit run app.py`

# How to use:

**1. Paste a YouTube URL into the first field **

**2. Type your question about the video**

**3. Hit Ask — the answer appears on the left, the full transcript on the right**


Note: Only works with videos that have subtitles/captions enabled.
