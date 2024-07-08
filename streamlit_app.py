# Import necessary libraries
import os
import streamlit as st
import google.generativeai as genai 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Google Generative AI with the API key
genai.configure(api_key=api_key)

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="AI powered quote generator"
)

def generate_response(text):
    config = {
        "temperature": 0.8,
        "max_output_tokens": 2048,
        }
        
    prompt = f"""Generate a {text} quote. The quote should be concise, impactful and suitable for sharing on social media.
    """
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(prompt)
    
    st.write(response.text)


# Check if the Google API key is provided in the sidebar
with st.sidebar:
    if 'GOOGLE_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        api_key = st.secrets['GOOGLE_API_KEY']
    else:
        api_key = st.text_input('Enter Google API Key:', type='password')
        if not (api_key.startswith('AI')):
            st.warning('Please enter your API Key!', icon='⚠️')
        else:
            st.success('Success!', icon='✅')
    os.environ['GOOGLE_API_KEY'] = api_key
    "[Get a Google Gemini API key](https://ai.google.dev/)"

# Set the title and caption for the Streamlit app
st.title("🤖 Google Gemini Models")
st.caption("🚀 A streamlit app powered by Google Gemini")

with st.form('form'):
    option = st.selectbox(
    "Select a theme",
    ("inspirational ", "motivational", "humor", "wisdom"))
    submitted = st.form_submit_button('submit')

if not api_key:
    st.info("Please add your Gemini API key to continue.")
elif submitted:
    generate_response(option)
