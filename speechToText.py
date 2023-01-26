import speech_recognition as sr
from pydub import AudioSegment
import tensorflow as tf
from tensorflow import keras
import tensorflow.keras as keras
import pandas as pd
import numpy as np
import string
from tensorflow.keras.models import load_model
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

fs = 44100  # Sample rate
seconds = 7  # Duration of recording

uni_words = {'great': 1,
 'work': 2,
 'today': 3,
 'class': 4,
 'who': 5,
 'can': 6,
 'tell': 7,
 'me': 8,
 'what': 9,
 'the': 10,
 'main': 11,
 'idea': 12,
 'of': 13,
 'this': 14,
 'lesson': 15,
 'is': 16,
 'anyone': 17,
 'give': 18,
 'an': 19,
 'example': 20,
 'that': 21,
 'concept': 22,
 'in': 23,
 'action': 24,
 "let's": 25,
 'review': 26,
 'we': 27,
 'learned': 28,
 'yesterday': 29,
 "i'm": 30,
 'here': 31,
 'to': 32,
 'help': 33,
 'you': 34,
 'succeed': 35,
 'do': 36,
 'it': 37,
 'break': 38,
 'down': 39,
 'into': 40,
 'smaller': 41,
 'steps': 42,
 'does': 43,
 'make': 44,
 'sense': 45,
 'everyone': 46,
 'someone': 47,
 'explain': 48,
 'their': 49,
 'own': 50,
 'words': 51,
 'glad': 52,
 'asked': 53,
 'question': 54,
 'looking': 55,
 'for': 56,
 'volunteers': 57,
 'present': 58,
 'open': 59,
 'hearing': 60,
 'your': 61,
 'suggestions': 62,
 'on': 63,
 'how': 64,
 'improve': 65,
 "don't": 66,
 'be': 67,
 'afraid': 68,
 'mistakes': 69,
 "that's": 70,
 'learn': 71,
 'resources': 72,
 'or': 73,
 'materials': 74,
 'use': 75,
 'us': 76,
 'better': 77,
 'understand': 78,
 'topic': 79,
 'try': 80,
 'problem': 81,
 'together': 82,
 'as': 83,
 'a': 84,
 'other': 85,
 'questions': 86,
 'have': 87,
 'about': 88,
 'support': 89,
 'every': 90,
 'step': 91,
 'way': 92,
 'hard': 93,
 'paying': 94,
 'off': 95,
 'find': 96,
 'solution': 97,
 'are': 98,
 'all': 99,
 'capable': 100,
 'achieving': 101,
 'greatness': 102,
 'strategies': 103,
 'found': 104,
 'helpful': 105,
 'when': 106,
 'learning': 107,
 'new': 108,
 'material': 109,
 'effort': 110,
 'making': 111,
 'difference': 112,
 'proud': 113,
 'progress': 114,
 "you've": 115,
 'made': 116,
 'apply': 117,
 'real-world': 118,
 'situations': 119,
 'think': 120,
 'most': 121,
 'important': 122,
 'thing': 123,
 'summary': 124,
 'covered': 125,
 "today's": 126,
 'take': 127,
 'few': 128,
 'minutes': 129,
 'reflect': 130,
 "we've": 131,
 'build': 132,
 'some': 133,
 'common': 134,
 'misconceptions': 135,
 'reach': 136,
 'full': 137,
 'potential': 138,
 'one': 139,
 'will': 140,
 'away': 141,
 'from': 142,
 'revisit': 143,
 'next': 144,
 'week': 145,
 'see': 146,
 'much': 147,
 'remember': 148,
 'share': 149,
 'thoughts': 150,
 'participation': 151,
 'greatly': 152,
 'appreciated': 153,
 'available': 154,
 'during': 155,
 'office': 156,
 'hours': 157,
 'if': 158,
 'need': 159,
 'extra': 160,
 'understanding': 161,
 'input': 162,
 'valuable': 163,
 'examples': 164,
 'impressive': 165,
 'achieve': 166,
 'goals': 167,
 'overcome': 168,
 'any': 169,
 'challenges': 170,
 'may': 171,
 'face': 172,
 'growth': 173,
 'and': 174,
 'development': 175,
 'ways': 176,
 'practice': 177,
 'reinforce': 178,
 'i': 179,
 'believe': 180,
 'abilities': 181,
 'guide': 182,
 'our': 183,
 'daily': 184,
 'lives': 185,
 'success': 186,
 'creative': 187,
 'solutions': 188,
 'problems': 189,
 'grow': 190,
 'curiosity': 191,
 'encouraged': 192,
 'obstacles': 193,
 'come': 194,
 'contributions': 195,
 'discussions': 196,
 'best': 197,
 'worry': 198,
 'rest': 199,
 "there's": 200,
 'no': 201,
 'such': 202,
 'stupid': 203,
 'things': 204,
 'makes': 205,
 "it's": 206,
 'them': 207,
 'matters': 208,
 'so': 209,
 'far': 210,
 'ask': 211,
 'brainstorm': 212,
 'ideas': 213,
 'skills': 214,
 'tackle': 215,
 'challenge': 216,
 'celebrate': 217,
 'accomplishments': 218,
 'power': 219,
 'positive': 220,
 'change': 221,
 'set': 222,
 'towards': 223,
 'member': 224,
 'valued': 225,
 'not': 226,
 'outside': 227,
 'box': 228,
 'ability': 229,
 'critically': 230,
 'collaborate': 231,
 'each': 232,
 'unique': 233,
 'strengths': 234,
 'talents': 235,
 'risks': 236,
 'encourage': 237,
 'dreams': 238,
 'develop': 239,
 'life': 240,
 'diversity': 241,
 "other's": 242,
 'differences': 243,
 'part': 244,
 'community': 245,
 'discover': 246,
 'passions': 247,
 'create': 248,
 'environment': 249,
 'impact': 250,
 'world': 251,
 'person': 252,
 'inspire': 253,
 'selves': 254,
 'choices': 255,
 'respect': 256,
 'safe': 257,
 'space': 258,
 'yourself': 259,
 'knowledge': 260,
 'embrace': 261,
 'opportunities': 262,
 'contributor': 263,
 'self-confidence': 264,
 'supportive': 265,
 'inclusive': 266,
 'future': 267,
 'leadership': 268,
 'others': 269,
 'go': 270,
 'over': 271,
 'plan': 272,
 'last': 273,
 'more': 274,
 'summarize': 275,
 'through': 276,
 'thought': 277,
 'process': 278,
 'provide': 279,
 'different': 280,
 'perspective': 281,
 'issue': 282,
 'small': 283,
 'groups': 284,
 'discuss': 285,
 'relate': 286,
 'previous': 287,
 'real': 288,
 'history': 289,
 'vote': 290,
 'which': 291,
 'direction': 292,
 'should': 293,
 'with': 294,
 'project': 295,
 'information': 296,
 'fit': 297,
 'already': 298,
 'know': 299,
 'counterargument': 300,
 'point': 301,
 'possible': 302,
 'connect': 303,
 'something': 304,
 'significance': 305,
 'key': 306,
 'points': 307,
 'personal': 308,
 'experience': 309,
 'related': 310,
 'interpretation': 311,
 'text/data/etc': 312,
 'time': 313,
 'too': 314,
 'busy': 315,
 "you're": 316,
 'living': 317,
 'up': 318,
 'disappointed': 319,
 'trying': 320,
 'enough': 321,
 'smart': 322,
 'care': 323,
 'hold': 324,
 'hand': 325,
 'patience': 326,
 'wasting': 327,
 'my': 328,
 "you'll": 329,
 'never': 330,
 'good': 331,
 'than': 332,
 'deal': 333,
 'tired': 334,
 'repeating': 335,
 'myself': 336,
 'putting': 337,
 'energy': 338,
 'going': 339,
 'spoon-feed': 340,
 'handling': 341,
 'students': 342,
 'like': 343,
 'lost': 344,
 'cause': 345,
 'successful': 346,
 'waste': 347,
 'necessary': 348,
 'cut': 349,
 'out': 350,
 'intelligent': 351,
 'worthy': 352,
 'attention': 353,
 'amount': 354,
 'anything': 355,
 'competent': 356,
 'complete': 357,
 'task': 358,
 'interested': 359,
 'excuses': 360,
 'grasp': 361,
 'teach': 362}


filename = "recording1.wav"

def get_model():
    model = load_model("deca.h5")
    return model

def phrase_encoder(text):
  arr = []
  for word in text:
    if word in uni_words.keys():
      arr.append(uni_words[word])
    else:
      arr.append(0)
  return arr

def analysis(my_model, phrase):
    my_dict = {"Content":phrase}
    my_data = pd.DataFrame(data = my_dict, index = [0])

    predict_data = my_data["Content"]
    predict_data = predict_data.apply(lambda review:review.split())
    predict_data = predict_data.apply(phrase_encoder)
    predict_data = keras.preprocessing.sequence.pad_sequences(predict_data, value=0, padding = 'post', maxlen = 12)
    print(my_model.predict(predict_data))
    if my_model.predict(predict_data) > 0.57:
        print("This was a nice phrase")
    else:
        print("This was a mean phrase")

def speechify():
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print("You said: " + text)
    return text

print("Started Listening")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
wv.write("recording1.wav", myrecording, fs, sampwidth=2)  # Save as WAV file 
print("Done Listening")
predictor = get_model()
speech_to_words = speechify()
analysis(predictor, speech_to_words)

