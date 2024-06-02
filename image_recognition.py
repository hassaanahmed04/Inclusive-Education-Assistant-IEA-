import streamlit as st
import base64

def image_recognition_section(client):
    st.header("Image Recognition and Description")
    st.write("Upload an image for description")
    image_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    if image_file is not None:
        st.image(image_file, caption='Uploaded Image', use_column_width=True)
        image_data = base64.b64encode(image_file.read()).decode("utf-8")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What’s in this image?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_data}"  
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        if response.choices[0].message.content[0].content[0].type == "text":
            st.write("OpenAI Image Recognition: " + response.choices[0].message.content[0].content[0].text)
        elif response.choices[0].message.content[0].content[0].type == "error":
            st.error("Image recognition failed. Please try again.")
        confidence = response.choices[0].message.content[0].content[0].metadata.get("confidence")
        if confidence is not None:
            st.write("Confidence Score:", confidence)
