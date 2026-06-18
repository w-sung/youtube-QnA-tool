import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from groq import Groq
import re # regular expression - specifies a set of strings that matches it

######### Backend Functions

def get_video_id(url): # takes id out of youtube video url
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11})' # id expression
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_transcript(url):
    video_id = get_video_id(url)
    if not video_id:
        return None, "Couldn't extract video ID"
    try:
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id)
        return ' '.join([item.text for item in transcript_data]), None
    except Exception as e:
        return None, str(e)

def ask_groq(transcript, question):
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"""Here is the transcript of a YouTube video:

                {transcript[:8000]}

                Based only on this transcript, answer this question:
                {question}"""
            }
        ]
    )
    return response.choices[0].message.content


######### UI

st.title("YouTube Video Q&A")
st.write("Paste a YouTube link and ask anything about the video.")

url = st.text_input("YouTube URL")
question = st.text_input("Your question")


if st.button("Ask"):
    if not url or not question:
        st.warning("Fill in both fields first.")
    else:
        with st.spinner("Fetching transcript..."):
            transcript, error = get_transcript(url)
        
        if transcript is None:
            st.error(f"Error: {error}")
        else:
            with st.spinner("Thinking..."):
                answer = ask_groq(transcript, question)
            st.success("Answer:")
            st.write(answer)


