import pyttsx3 as p

engine = p.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello There, I am your Voice Assistant.")
engine.runAndWait()
