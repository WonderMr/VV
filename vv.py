from vosk import Model, KaldiRecognizer
import deep_translator
import time
import pyttsx3
import os
import json
import pyaudio

M                       =   deep_translator.MyMemoryTranslator(source='ru',target='en')
tts                     =   pyttsx3.init()
EN_VOICE                =   'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
tts.setProperty('voice', EN_VOICE)
#voices                  =   tts.getProperty('voices')
#model                   =   Model(r"c:/Repos/VV/models/vosk-model-ru-0.10") # полный путь к модели
model                   =   Model(r"c:/Repos/VV/models/vosk-model-small-ru-0.22") # полный путь к модели
rec                     =   KaldiRecognizer(model, 16000)
p                       =   pyaudio.PyAudio()
stream                  =   p.open(
    format              =   pyaudio.paInt16,
    channels            =   1,
    rate                =   16000,
    input               =   True,
    frames_per_buffer   =   8000
)
stream.start_stream()
while True:
    try:
        # if tts.isBusy():
        #     time.sleep(0.1)
        #     continue
        data            =   stream.read(8000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res         =   json.loads(rec.Result())
            if res["text"] == "":
                continue
            translated  =   M.translate(res["text"])
            print(translated)
            tts.say(translated)
            tts.runAndWait()
            tts.stop()
    except(Exception):
        #stream.stop_stream()
        #stream.start_stream()
        pass

print(rec.FinalResult())
#     print(rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult())
#     RR              =   rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult()
#     ResultTxt       =   json.loads(RR)
#     if ResultTxt.exist("text") & ResultTxt['text'] == "":
#         if not Text=="":
#             print(Text)
#     else:
#         Text        =   ResultTxt['text']
#
# print(Text)