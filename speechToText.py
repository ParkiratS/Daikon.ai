import speech_recognition as sr
from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("D:\Programming\Projects\DecaProject\output.mp3")
sound.export("output.wav", format="wav")

filename = "D:\Programming\Projects\DecaProject\output.wav"

r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)