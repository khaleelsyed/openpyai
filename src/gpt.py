import os

from openai import OpenAI
import streamlit as st

GPT_MODEL = "gpt-4o"

st.title(f'Model: "{GPT_MODEL}"')

client = OpenAI(api_key=os.getenv("OPENAI_TOKEN"))

def clear_messages() -> None:
    st.session_state.messages = st.session_state.messages[0:1]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = GPT_MODEL

system_prompt = st.text_area("System Prompt", "You are a helpful assistant that is knowledgeable on everything.")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
else:
    st.session_state.messages[0] = {"role": "system", "content": system_prompt}

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter user prompt"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
