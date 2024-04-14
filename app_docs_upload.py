from openai import OpenAI
from gtts import gTTS
from io import BytesIO,StringIO
#Using streamlit app framework
import streamlit as st




#Creating client
client= OpenAI(
    api_key="sk-1234567890",
    base_url='http://localhost:8000/v1'
)


# Title of the app
st.title("TherapyBot- A Chatbot for Mental Health Support")




#Uploading medical records
uploaded_file = st.file_uploader("", type=["txt"], label_visibility="collapsed")
css = '''
<style>
    [data-testid='stFileUploader'] {
        width: max-content;
    }
    [data-testid='stFileUploader'] section {
        padding: 0;
        float: left;
    }
    [data-testid='stFileUploader'] section > input + div {
        display: none;
    }
    [data-testid='stFileUploader'] section + div {
        float: right;
        padding-top: 0;
    }

</style>
'''
st.markdown(css, unsafe_allow_html=True)

doc_data = ""
#If user uploads a file
if uploaded_file is not None:

    # To read file as string:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    doc_data = stringio.read()
    doc_data = "This is my medical record - "+doc_data
    


#Taking user input
prompt= st.chat_input('Chat to start or upload any medical records. How can I help?')


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
            'content': doc_data+" Please answer the following question based on the earlier medical record- "+prompt
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


