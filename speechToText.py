import speech_recognition as sr
from pydub import AudioSegment

                                                       
# sound = AudioSegment.from_wav("DecaProject\output.wav")
# sound.export("output.wav", format="wav")

filename = "d:\Programming\Projects\DecaProject\\recording1.wav"

r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)