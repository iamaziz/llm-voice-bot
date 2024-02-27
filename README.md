# 🎙️ Voice LLM Bot

Speak to Ollama LLMs in any language.

## Demo (📢 voice on)


https://github.com/iamaziz/llm-voice-bot/assets/3298308/e444d4db-f8d9-4b7d-996d-cb783d704c61


<hr>

**Note**

- If a langauge is not available in the dropdown list, it can be added [here](https://github.com/iamaziz/llm-voice-bot/blob/main/app.py#L11).
- Thanks to [streamlit_mic_recorder](https://github.com/B4PT0R/streamlit-mic-recorder).

<hr>


> Interesting how LLMs responded differently to switching languages in the same conversation.
> Almost all the tested models understood the question in its original langauge, but they varied in how they reponded.
> Mistral models consistently answered in English. While other models stumbled going back and forth.

Here are some examples:

mistral
![image](https://github.com/iamaziz/llm-voice-bot/assets/3298308/4d0b97c9-e42e-4d83-9cd2-fee970cba86f)

dolphin-mistral
<img width="1204" alt="image" src="https://github.com/iamaziz/llm-voice-bot/assets/3298308/978c281d-143f-4b03-8ae2-2393a8229d44">


llama2:13b
<img width="1469" alt="image" src="https://github.com/iamaziz/llm-voice-bot/assets/3298308/ffdfeb91-89e8-4618-86da-ef8436da0868">

qwen:7b
<img width="1470" alt="image" src="https://github.com/iamaziz/llm-voice-bot/assets/3298308/b769ef75-e97c-4480-b8d3-80c1e7f2934a">

gemma:7b (worst)
<img width="1501" alt="image" src="https://github.com/iamaziz/llm-voice-bot/assets/3298308/26fa44b4-1000-4c56-bbea-fde66ec4f6da">


And GPT-4 for comparison:

<img width="975" alt="image" src="https://github.com/iamaziz/llm-voice-bot/assets/3298308/028e6136-d886-4421-9ae4-aa90273827d9">

