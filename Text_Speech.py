import pyttsx3

speaker = pyttsx3.init()

# Change Voice (Spanish Voice)
# speaker.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
    
text = "Change this text"
mp3_name = 'example'
    
speaker.save_to_file(text, mp3_name + ".mp3")
speaker.runAndWait()
speaker.stop()