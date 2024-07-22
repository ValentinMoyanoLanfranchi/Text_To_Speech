import pyttsx3
import PyPDF2

file_name = '' # Insert file name, the file must be in the same folder or insert the path
mp3_name = 'pdf_example'

with open(file_name, 'rb') as file:
    pdfreader = PyPDF2.PdfReader(file)
    speaker = pyttsx3.init()
    # Change Voice (Spanish Voice)
    # speaker.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
    full_text = ""
    for page_num in range(len(pdfreader.pages)):
        page = pdfreader.pages[page_num]
        text = page.extract_text()
        clean_text = text.strip().replace('\n', ' ')
        full_text += clean_text + " "
    speaker.save_to_file(full_text, mp3_name + '.mp3')
    speaker.runAndWait()
    speaker.stop()

    