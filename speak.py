import speech_recognition as sr
import pyaudio


r = sr.Recognizer()


with sr.Microphone() as source:
    # aumentar ou diminuir o tempo de pausa entre 0.7 a 1.5
    r.pause_threshold=1.2
    print('Estou ouvindo: ')

    audio = r.listen(source)

  
    try:
        text = r.recognize_google(audio, language='pt-br')
        print(text)
    except Exception as e:
        print(e)
        print('Erro')



