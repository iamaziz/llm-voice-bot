import streamlit as st
import ollama as ol
from voice import record_voice

st.set_page_config(page_title="🎙️ Voice Bot", layout="wide")
st.title("🎙️ Speech Bot")
st.sidebar.title("`In any language`")


def language_selector():
    lang_options = ["ar", "de", "en", "es", "fr", "it", "ja", "nl", "pl", "pt", "ru", "zh"]
    with st.sidebar: 
        return st.selectbox("Speech Language", ["en"] + lang_options)

def llm_selector():
    ollama_models = [m['name'] for m in ol.list()['models']]
    with st.sidebar:
        return st.selectbox("LLM", ollama_models)


def check_rtl(text):
    if any("\u0600" <= c <= "\u06FF" for c in text):
        return f"<p style='direction: rtl; text-align: right;'>{text}</p>"
    return text


def print_chat_message(message):
    if message["role"] == "user":
        with st.chat_message("user", avatar="🎙️"):
            st.markdown(check_rtl(message['content']), unsafe_allow_html=True)
    else:
        with st.chat_message("assistant", avatar="🦙"):
            st.markdown(check_rtl(message['content']), unsafe_allow_html=True)

def main():
    
    model = llm_selector()
    with st.sidebar:
        question = record_voice(language=language_selector())
    
    # init chat history for a model
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = {}
    if model not in st.session_state.chat_history:
        st.session_state.chat_history[model] = []
    chat_history = st.session_state.chat_history[model]
    # print conversation history
    for message in chat_history: print_chat_message(message)

    if question:
        user_message = {"role": "user", "content": question}
        print_chat_message(user_message)
        chat_history.append(user_message)
        response = ol.chat(model=model, messages=chat_history)
        answer = response['message']['content']
        ai_message = {"role": "assistant", "content": answer}
        print_chat_message(ai_message)
        chat_history.append(ai_message)

        # truncate chat history to keep 20 messages max
        if len(chat_history) > 20:
            chat_history = chat_history[-20:]
        
        # update chat history
        st.session_state.chat_history[model] = chat_history


if __name__ == "__main__":
    main()