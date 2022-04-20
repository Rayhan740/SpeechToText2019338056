# Importing the speech recognition library
import speech_recognition as sr
# Initialize the recognizer
r = sr.Recognizer()

# Open the file
with sr.Microphone() as source:
    print("Speak Anything : ")
     # Listen for the data(load audio to memory)
    audio = r.listen(source)
    try:
        # Recognize(speech to text)
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said!")
