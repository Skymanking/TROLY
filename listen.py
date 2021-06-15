import speech_recognition as sr
def listen():
    ear = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening")
        ear.pause_threshold = 0.8
        ear.adjust_for_ambient_noise(mic, duration= 0.5)
        audio = ear.listen(mic, timeout= 5)
        print("1")
    text = ear.recognize_google(audio, language="es-ES")
    return text

