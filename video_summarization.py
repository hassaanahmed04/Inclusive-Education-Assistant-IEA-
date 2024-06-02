import streamlit as st
import base64

def video_summarization_section(client):
    st.header("Video Summarization and Captioning")
    st.write("Upload a video for summarization and captioning")
    video_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
    if video_file is not None:
        st.video(video_file)
        video_data = base64.b64encode(video_file.read()).decode("utf-8")
        
        response = client.chat.completions.create(
            model="gpt-4o", 
            messages=[
                {
                    "role": "user",
                    "content": video_data
                }
            ],
            max_tokens=150,  
            temperature=0.7,  
                        stop=["\n", "###"]  
        )
        
        if response.choices[0].message.content[0].content[0].type == "text":
            st.write("GPT-3 Video Summary: " + response.choices[0].message.content[0].content[0].text)
        elif response.choices[0].message.content[0].content[0].type == "error":
            st.error("Video summarization failed. Please try again.")
