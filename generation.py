import openai
from dotenv import load_dotenv
import os
import pyttsx3

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
def generation(question) :
    prompt = [{"role":"system","content":"You are a chatbot that is always lying"},
            {"role":"user", "content":question}]
    answer = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = prompt)
    return answer["choices"][0]["message"]["content"]

def text_to_speech(input):
    tts = pyttsx3.init()
    tts.say(input)
    tts.runAndWait()

answer = generation("How to find a treasure ?")
text_to_speech(answer)


