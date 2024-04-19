# Therapy-Bot
Therapy-Bot is a locally running, completely data-secure chatbot designed to provide support for mental health-related inquiries. It uses the [llama.cpp](https://github.com/ggerganov/llama.cpp) framework. The chatbot can provide helpful responses, read psychiatric reports of patients, answer queries based on said reports and output a voice generated message.
## Table of Contents
* Features
* Setup
* Model
* Disclaimer
* Author
## Features
* Data Secure: All processing is done locally on your machine, ensuring complete data privacy and security.
* Mental Health Model: Utilizes a fine-tuned Chat-LLaMA model for mental health support.
* Medical Report Reading: Can read psychiatric reports of patients if needed and answer queries based on them.
## Setup
1. Git clone https://github.com/ggerganov/llama.cpp 
2. Run the make commands: 
- Mac: `cd llama.cpp && make`
- Windows (from <a href="https://github.com/ggerganov/llama.cpp/blob/master/README.md">here</a> ):
    1. Download the latest fortran version of [w64devkit](https://github.com/skeeto/w64devkit/releases).
    2. Extract `w64devkit` on your pc.
    3. Run `w64devkit.exe`.
    4. Use the `cd` command to reach the `llama.cpp` folder.
    5. From here you can run:
        ```bash
        make
        ```
3. pip install openai 'llama-cpp-python[server]' pydantic instructor streamlit
4. Start the server:
`python -m llama_cpp.server --model D:\CHATBOT_PROJ_NEW\MentaLLaMA-chat-7b-GGUF-q8\MentaLLaMA-chat-7b-GGUF-q8.gguf --n_gpu -1`

## Model
- Chat_LLAMA: [WesselvanGils/MentaLLaMA-chat-7b-GGUF-q8](https://huggingface.co/WesselvanGils/MentaLLaMA-chat-7b-GGUF-q8)


## Disclaimer
Therapy-Bot is not a substitute for licensed therapists or professional medical advice. This bot should not be used as a replacement for actual therapy or mental health treatments. Always seek professional advice for any mental health concerns.

## Author
👨🏾‍💻 Author: Dev Pandey <br />
