import pyttsx3
def talk(say):
    e = pyttsx3.init()
    e.say(say)
    e.runAndWait()
