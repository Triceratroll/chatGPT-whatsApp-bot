import os
import openai
import speech_recognition as sr
from dotenv import load_dotenv
from gtts import gTTS
from playsound import playsound 

def jarvis_speaks(text):

  print(f'Jarvis: {text}') 
  tts = gTTS(text, lang='es', tld='es')

  if os.path.exists("./audio.mp3"):
    os.remove("./audio.mp3")

  tts.save('./audio.mp3') 
  playsound('./audio.mp3')


def main():

  load_dotenv()
  openai.api_key = os.getenv("OPENAI_API_KEY") 

  # Create a Recognizer instance
  r = sr.Recognizer()
  # Create a microphone instance
  mic = sr.Microphone()

  jarvis_speaks('Hola soy Jarvis a su servicio')

  while True:

    with mic as source:

      r.adjust_for_ambient_noise(source)
      audio = r.listen(source) 

    try:

      text = r.recognize_google(audio, language='es-ES')
      print(f'You said: {text}')

      response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.6,
        max_tokens=250, 
      )
      response_text = response.choices[0].text
      jarvis_speaks(response_text)

    except sr.UnknownValueError:
      print('Sorry, I could not understand what you said')
    except sr.RequestError as e:
      print(f'Error while making the request: {e}')
      
if __name__ == "__main__":
  main()