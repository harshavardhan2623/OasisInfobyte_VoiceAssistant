import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()

def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

def main():
    speak("Hello! I'm your basic voice assistant. How can I assist you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hai")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

            speak("what else you want to know?")

        elif "date" in command:
            current_date = datetime.date.today().strftime("%Y/%m/%d")
            speak(f"Today's date is {current_date}")
            
            speak("what else you want to know?")
        elif "search" in command:
            speak("What would you like me to search for?")
            search_query = listen()
            if search_query:
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            
            speak("what else you want to know?")

        elif "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("I'm sorry, I don't understand that command. Can you please repeat?")

if __name__ == "__main__":
    main()
