
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

fs = 44100  # Sample rate
seconds = 7  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
wv.write("recording1.wav", myrecording, fs, sampwidth=2)  # Save as WAV file 
print(myrecording)