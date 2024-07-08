# import streamlit as st
# from langchain.llms import OpenAI
# from langchain.prompts import PromptTemplate


# st.title("🎈 AI powered quote generator")

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


# def generate_response(text):
#     print(text)
#     # # Instantiate LLM model
#     # llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)
#     # # Prompt
#     # template = "Generate a {text} quote. The quote should be concise, impactful and suitable for sharing on social media."
#     # prompt = PromptTemplate(input_variables=["text"], template=template)
#     # prompt_query = prompt.format(topic=text)
#     # # Run LLM model
#     # response = llm(prompt_query)
#     # # Print results
#     # return st.info(response)
#     # print(text)

# with st.form('form'):
#     option = st.selectbox(
#     "Select a theme",
#     ("inspirational ", "motivational", "humor", "wisdom"))
#     submitted = st.form_submit_button('submit')

# # if not openai_api_key:
# #     st.info("Please add your OpenAI API key to continue.")
# # elif submitted:
#     generate_response(option)

# Import necessary libraries
import os
import streamlit as st
import google.generativeai as genai 
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Google Generative AI with the API key
genai.configure(api_key=api_key)

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Google Gemini Models",
    page_icon="🤖"
)

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

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content('Teach me about how an LLM works')

st.write(response.text)
