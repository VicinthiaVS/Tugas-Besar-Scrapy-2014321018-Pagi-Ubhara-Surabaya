################################
# ini untuk melakukan SpeechReconigtionnya

import speech_recognition as sr

r = sr.Recognizer()

def Conversion(file, lang):
    all_ = []
    with sr.AudioFile(file) as source:
        print("Fetching file")
        audio_text = r.record(source)
        try: 
            print("Convering audio to text...")
            text = r.recognize_google(audio_text, language=lang)
            all_.append(text)
        except:
            print("sorry, coba putar lagi...")
    print(all_)

if __name__ == "__main__":
    Conversion(
        "computer_access.wav", "en=IN",
    ),
    