import streamlit as st

st.title("🎈 AI powered quote generator")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

with st.form('form'):
    option = st.selectbox(
    "Select a theme",
    ("inspirational ", "motivational", "humor", "wisdom"))
    submitted = st.form_submit_button('submit')