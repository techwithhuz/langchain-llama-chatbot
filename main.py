#Integrate code with OpenAI API

import os
import streamlit as st 
from langchain_community.llms import Ollama



llm = Ollama(model="llama2")

#Steamlit framework
st.title('Langchain Demo with OpenAI')
input_text=st.text_input("search the topic you want")


if input_text:
    st.write(llm.invoke(input_text))