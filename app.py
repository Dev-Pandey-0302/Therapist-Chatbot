from openai import OpenAI
from gtts import gTTS
from io import BytesIO
#Using streamlit app framework
import streamlit as st

#Creating client
client= OpenAI(
    api_key="sk-1234567890",
    base_url='http://localhost:8000/v1'
)
# Title of the app
st.title("TherapyBot- A Chatbot for Mental Health Support")

prompt= st.chat_input('How can I help you today?')

#If users types prompt and hits enter
if prompt:
    st.chat_message("user").markdown(prompt)
    #Chat Completion
    reponse= client.chat.completions.create(
        #which model we wanna use
        model='D:\CHATBOT_PROJ_NEW\MentaLLaMA-chat-7b-GGUF-q8\MentaLLaMA-chat-7b-GGUF-q8.gguf',
        #pass through the prompt
        messages=[{
            'role': 'user',
            'content': prompt
        }],
        #Add streaming
        stream=True
    )
    with st.chat_message("ai"):
        completed_message = ""
        message= st.empty()
        #Streaming the response out
        for chunk in reponse:
            if chunk.choices[0].delta.content is not None:
                #print(chunk.choices[0].delta.content, flush=True, end="")
                completed_message += chunk.choices[0].delta.content
                message.markdown(completed_message)

        sound_file = BytesIO()
        tts = gTTS(completed_message, lang='en')
        tts.write_to_fp(sound_file)
        st.audio(sound_file)


