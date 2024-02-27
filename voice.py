import streamlit as st
from streamlit_mic_recorder import speech_to_text


def record_voice(language="en"):
    # https://github.com/B4PT0R/streamlit-mic-recorder?tab=readme-ov-file#example

    state = st.session_state

    if "text_received" not in state:
        state.text_received = []

    text = speech_to_text(
        start_prompt="🎤 Click and speak to ask question",
        stop_prompt="⚠️Stop recording🚨",
        language=language,
        use_container_width=True,
        just_once=True,
    )

    if text:
        state.text_received.append(text)

    result = ""
    for text in state.text_received:
        result += text

    state.text_received = []

    return result if result else None
