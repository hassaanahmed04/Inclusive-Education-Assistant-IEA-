import streamlit as st
from text_to_speech import text_to_speech_section
from image_recognition import image_recognition_section
from interactive_videos import interactive_videos_section
from video_summarization import video_summarization_section
from adaptive_learning import adaptive_learning_section
from assistive_technologies import assistive_technologies_section
from collaboration_support import collaboration_support_section
from openai import OpenAI
client=OpenAI(api_key="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")

# Initialize the OpenAI client

# Page configuration
st.set_page_config(
    page_title="Inclusive Education Assistant (IEA)",
    page_icon="📘",
    layout="wide",
)

# Custom CSS
st.markdown("""
    <style>
    /* Custom button style */
    .stButton>button {
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        border-radius: 5px; /* Rounded corners */
        padding: 10px 24px; /* Padding */
        font-size: 16px; /* Increase font size */
    }

    /* Custom text area style */
    .stTextArea textarea {
        background-color: #f1f1f1; /* Light gray background */
        border: 1px solid #ccc; /* Border */
        border-radius: 5px; /* Rounded corners */
        padding: 10px; /* Padding */
        font-size: 16px; /* Increase font size */
    }

    /* Custom header style */
    .stHeader {
        color: #4CAF50; /* Green color for headers */
        font-size: 24px; /* Increase font size */
    }

    /* Custom subheader style */
    .stSubheader {
        color: #2196F3; /* Blue color for subheaders */
        font-size: 20px; /* Increase font size */
    }
    </style>
""", unsafe_allow_html=True)

# Main title
st.title("Inclusive Education Assistant (IEA)")

st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Text-to-Speech & Speech-to-Text",
        "Image Recognition",
        "Video Summarization",
        "Interactive Videos",
        "Adaptive Learning",
        "Assistive Technologies",
        "Collaboration and Support"
    ]
)

# Home section
if section == "Home":
    st.header("Welcome to the Inclusive Education Assistant!")
    st.write("Use the sidebar to navigate to different features.")

# Text-to-Speech & Speech-to-Text section
elif section == "Text-to-Speech & Speech-to-Text":
    text_to_speech_section(client)

# Image Recognition section
elif section == "Image Recognition":
    image_recognition_section(client)

# Video Summarization section
elif section == "Video Summarization":
    video_summarization_section(client)

# Interactive Videos section
elif section == "Interactive Videos":
    interactive_videos_section()

# Adaptive Learning section
elif section == "Adaptive Learning":
    adaptive_learning_section(client)

# Assistive Technologies section
elif section == "Assistive Technologies":
    assistive_technologies_section()

# Collaboration and Support section
elif section == "Collaboration and Support":
    collaboration_support_section()