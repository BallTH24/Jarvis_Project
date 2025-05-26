import speech_recognition as sr
import pyttsx3
import datetime
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

print("Welcome to Jarvis: AI Assistant")
engine.say("Jarvis is ready")
engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Jarvis listening...")

            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)

            if "hello" in text:
                print("Jarvis said: Hello")
                engine.say("Hello")

            elif "your name" in text:
                print("Jarvis said: My name is Jarvis")
                engine.say("My name is Jarvis")

            elif "good morning" in text:
                print("Jarvis said: Good morning")
                engine.say("Good morning")

            elif "goodbye" in text:
                print("Jarvis said: Bye")
                engine.say("Bye")
                engine.runAndWait()
                break

            elif "what time is it" in text:
                now = datetime.datetime.now().strftime("%H:%M")
                print(f"Jarvis said: The time is {now}")
                engine.say(f"The time is {now}")

            elif "open notepad" in text:
                print("Jarvis said: Opening Notepad")
                engine.say("Opening Notepad")
                os.system("start notepad")

            elif "thank you" in text:
                print("Jarvis said: You're welcome")
                engine.say("You're welcome")

            else:
                print("Jarvis said: I didn't catch a command.")
                engine.say("I didn't catch a command.")

            engine.runAndWait()

    except sr.UnknownValueError:
        print("Jarvis said: Sorry, I couldn't understand that.")
        engine.say("Sorry, I couldn't understand that.")
        engine.runAndWait()

    except Exception as e:
        print(f"Jarvis said: Microphone error. {e}")
        engine.say("Microphone error")
        engine.runAndWait()