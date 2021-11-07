from vosk import Model, KaldiRecognizer
import deep_translator
import os
import json
import pyaudio

M                       =   deep_translator.MyMemoryTranslator(source='ru',target='en')
#model                   =   Model(r"c:/Repos/VV/models/vosk-model-ru-0.10") # полный путь к модели
model                  =   Model(r"c:/Repos/VV/models/vosk-model-small-ru-0.22") # полный путь к модели
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
    data                =   stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res             =   json.loads(rec.Result())
        translated      =   M.translate(res["text"])
        print(translated)

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