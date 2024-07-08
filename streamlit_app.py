import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


st.title("🎈 AI powered quote generator")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(text):
    print(text)
    # # Instantiate LLM model
    # llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)
    # # Prompt
    # template = "Generate a {text} quote. The quote should be concise, impactful and suitable for sharing on social media."
    # prompt = PromptTemplate(input_variables=["text"], template=template)
    # prompt_query = prompt.format(topic=text)
    # # Run LLM model
    # response = llm(prompt_query)
    # # Print results
    # return st.info(response)
    # print(text)

with st.form('form'):
    option = st.selectbox(
    "Select a theme",
    ("inspirational ", "motivational", "humor", "wisdom"))
    submitted = st.form_submit_button('submit')

# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.")
# elif submitted:
    generate_response(option)