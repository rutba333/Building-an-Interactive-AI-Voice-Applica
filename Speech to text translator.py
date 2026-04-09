import speech_recognition as sr
import pyttsx3
from googletrans import Translator #Google Translate API

#Initialize text-to-speech engine
def speak(text,language="en"):
    engine=pyttsx3.init()
    engine.setProperty('rate',150) #speed of Speech
    voices=engine.getProperty('voices')


    #Set voice for english or other language if supported by pyttsx3
    if language=="en":
        engine.setProperty('voice',voices[0].id) #Default english voice

    else:
        engine.setProperty('voice',voices[1].id) #Falback to another voice if available


    engine.say(text)
    engine.runAndwait()

#Speech to text:Recognize spoken language
def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("???? please speak now in english...")

        audio=recognizer.listen(source)



    try:
        print("???Recognizing speech....")

        text=recognizer.recognize_google(audio,language="en-US") #Use English for speech recognition

        print(f"✅You said:{text}")
        return text
    
    except sr.UnknownValueError:
        print("❌Could not understand the audio.")

    except sr.RequestError as e:
        print(f"❌API Error:{e}")

    return ""

#Translate text using Google translate API
def translate_text(text,target_language="es"):
    translator=Translator()
    translation=translator.translate(text,dest=target_language)
    print(f"?????Translated text:{translation.text}")
    return translation.text


#display language options to the users
def display_language_options():
    print("?????Available translation languages:")
    print("1. Hindi(hi)")
    print("2.Tamil (ta)")
    print("3.Telugu(te)")
    print("4.Bengali(bn)")
    print("5.Marathi(mr)")
    print("8.Punjabi(pa)")


#user selects language
    choice=input("Please select the target language number(1-8):")
    language_dict={
       "1":"hi",
    "2":"ta",
    "3":"te",
    "4":"bn",
    "5":"mr",
    "6":"pa"


   }
    return language_dict.get(choice,"es") #default to spanish if invalid input

#main function to combine all steps
def main():
    #Step 1:Display language options and get user's choice
    target_language=display_language_options

    #step 2:Speech to text (recognizing English speech)
    original_text=speech_to_text()


    if original_text:
        #Step 3: Translate to selected target language
        translated_text=translate_text(original_text,target_language=target_language)


        #step 4: Text to speech (translate output and speak it)
        speak(translated_text,language="en") #speak the translation In English
        print("✅Translation spoken out!")


if __name__=="__main__":
    main()




 


