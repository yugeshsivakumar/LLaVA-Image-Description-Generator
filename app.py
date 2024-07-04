import streamlit as st
import ollama
from PIL import Image
import io

# Function to interact with the model and get the description
def get_image_description(image, prompt):
    # Convert PIL image to bytes (if required by the ollama library)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='JPEG')  # Adjust format as necessary
    image_bytes.seek(0)
    
    res = ollama.chat(
        model='llava',
        messages=[
            {
                'role': 'user',
                'content': prompt,
                'images': [image_bytes]
            }
        ]
    )
    return res['message']['content']

# Streamlit UI
st.title("Image Description using llava")

# File uploader for image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Text input for prompt
prompt = st.text_input("Enter your prompt", value="Describe this image")

if uploaded_image is not None:
    # Open and resize the uploaded image
    image = Image.open(uploaded_image)
    resized_image = image.resize((400, 400))  # Resize the image to 400x400 pixels
    
    # Display image and description side by side using columns
    col1, col2 = st.columns([2, 3])
    
    with col1:
        # Display the resized image on the left
        st.image(resized_image, caption="Uploaded Image", use_column_width=True)

    with col2:
        # Display the description on the right
        if st.button("Get Description"):
            description = get_image_description(image, prompt)
            st.info(description)  # Display answer in an info box
