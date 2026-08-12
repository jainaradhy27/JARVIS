"""
Jarvis — a simple voice assistant.
Say "jarvis" to wake it up, then give it a command:
  - "open google"
  - "open youtube"
  - "play <song name>"   (songs come from the MUSIC dict below)
"""

import speech_recognition as sr
import webbrowser
import pyttsx3

MUSIC = {
    "geography": "https://www.youtube.com/watch?v=gRRMSF0nB0c",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI",
}

# say "open <name>" for any of these
SITES = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "spotify": "https://open.spotify.com",
    "netflix": "https://netflix.com",
    "amazon": "https://amazon.com",
    "wikipedia": "https://wikipedia.org",
    "twitter": "https://twitter.com",
    "instagram": "https://instagram.com",
    "facebook": "https://facebook.com",
    "whatsapp": "https://web.whatsapp.com",
    "maps": "https://maps.google.com",
    "drive": "https://drive.google.com",
    "reddit": "https://reddit.com",
    "linkedin": "https://linkedin.com",
    "calendar": "https://calendar.google.com",
    "chatgpt": "https://chat.openai.com",
    "claude": "https://claude.ai",
}

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print(f"jarvis: {text}")
    engine.say(text)
    engine.runAndWait()


def process_command(command):
    command = command.lower()

    if command.startswith("open"):
        parts = command.split(" ", 1)
        site = parts[1].strip() if len(parts) > 1 else ""
        if site in SITES:
            webbrowser.open(SITES[site])
        else:
            speak(f"I don't have {site or 'that'} set up to open.")
    elif command.startswith("play"):
        parts = command.split(" ", 1)
        song = parts[1].strip() if len(parts) > 1 else ""
        if song in MUSIC:
            webbrowser.open(MUSIC[song])
        else:
            speak(f"I don't have {song} in my playlist.")
    else:
        speak("I didn't catch a command I know.")


def listen_once(prompt, timeout=5, phrase_time_limit=5):
    with sr.Microphone() as source:
        # calibrate to background noise for ~0.5s before listening —
        # without this, quiet mics/rooms often get missed entirely
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print(prompt)
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    return recognizer.recognize_google(audio)


def main():
    speak("Initializing Jarvis...")
    while True:
        print("\nlistening for wake word...")
        try:
            word = listen_once("Say something!")
            print(f"heard: {word}")

            # was an exact match (word.lower() == "jarvis") — too strict,
            # since Google's transcription rarely returns just that one
            # word cleanly. "in" catches "jarvis", "hey jarvis", etc.
            if "jarvis" in word.lower():
                speak("Yes? I'm listening.")
                try:
                    command = listen_once("jarvis active — say a command")
                    print(f"command heard: {command}")
                    process_command(command)
                except sr.WaitTimeoutError:
                    speak("I didn't hear a command in time.")
                except sr.UnknownValueError:
                    speak("Sorry, I didn't catch that.")

        except KeyboardInterrupt:
            speak("Shutting down.")
            break
        except sr.WaitTimeoutError:
            print("(no speech detected in time — still listening)")
        except sr.UnknownValueError:
            print("(couldn't understand the audio — still listening)")
        except sr.RequestError as e:
            print(f"speech recognition service error (check your internet connection): {e}")
        except Exception as e:
            print(f"error: {e}")


if __name__ == "__main__":
    main()
