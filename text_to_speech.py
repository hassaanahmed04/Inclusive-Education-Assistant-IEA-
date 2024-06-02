import streamlit as st

def text_to_speech_section(client):
    st.header("Text-to-Speech & Speech-to-Text")

    st.subheader("Text-to-Speech")
    text_input = st.text_area("Enter text here", height=150)
    speed = st.slider("Select speech speed:", 0.5, 2.0, 1.0, 0.1)
    pitch = st.slider("Select speech pitch:", -20, 20, 0, 1)
    volume = st.slider("Select speech volume:", 0.0, 1.0, 0.5, 0.1)
    voice = st.selectbox("Select voice:", ["Alloy", "Echo", "Fable", "Onyx", "Nova", "Shimmer"])
    
    
    
    language = st.selectbox("Select language:", ["English", "Spanish", "French"])
    
    bg_music = st.file_uploader("Upload background music (optional)", type=["mp3"])

    emotion = st.selectbox("Select emotion:", ["Neutral", "Happy", "Sad"])

    effects = st.multiselect("Select effects:", ["Echo", "Reverb", "Robot Voice"])

    if st.button("Convert to Speech"):
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice.lower(),
            input=text_input,
            speed=speed,
            # pitch=pitch,
            # volume=volume,
            # language=language.lower(),
            # bg_music=bg_music,
            # emotion=emotion.lower(),
            # effects=effects
        )
        st.audio(response['audio'], format='audio/wav')
        st.write("This will convert the text to speech using a TTS service. (Backend integration needed)")
        if st.button("Save Speech"):
            with open("generated_speech.wav", "wb") as f:
                f.write(response['audio'])

    st.markdown("---")


    st.subheader("Speech-to-Text")
    st.write("Upload an audio file for transcription")
    audio_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])
    if audio_file is not None:
        language = st.selectbox("Select audio language:", ["English", "Spanish", "French"])
        if st.button("Transcribe"):
            transcript = transcribe_audio(audio_file, language.lower())
            st.write("Transcription:")
            st.write(transcript)
            if st.button("Save Transcript"):
                with open("transcript.txt", "w") as f:
                    f.write(transcript)

import io
import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio(audio_file, language):
    recognizer = sr.Recognizer()

    try:
        audio_data = io.BytesIO(audio_file.read())

        audio = AudioSegment.from_file(audio_data, format="mp3")
        
        wav_audio = audio.export(format="wav")

        with sr.AudioFile(wav_audio) as source:
            audio_data = recognizer.record(source)

        if language == "english":
            text = recognizer.recognize_google(audio_data, language="en-US")
        elif language == "spanish":
            text = recognizer.recognize_google(audio_data, language="es-ES")
        elif language == "french":
            text = recognizer.recognize_google(audio_data, language="fr-FR")
        else:
            return "Unsupported language for transcription."

        return text
    except Exception as e:
        return f"Error: {str(e)}"