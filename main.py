import sys
sys.path.append("/mnt/c/Users/Byeongyong/Desktop/Python_Codes/ffmpeg-5.0.1-essentials_build/bin/")
log = 1
import speech_recognition as sr
from pydub import AudioSegment
import os.path
r = sr.Recognizer()
filepath = '/mnt/c/Users/Byeongyong/Desktop/Python_Codes/'
audio_filename = filepath + 'Onur_Mutlu_-_Dig_Design_Comp_Arc_(getmp3.pro)' + '.mp4'
#audio_filename = filepath + 'Call_recording_1.m4a'
if 'm4a' in audio_filename:
    if log: print("Converting m4a audio file to wav file format ...")

    wav_filename = audio_filename.replace('m4a', 'wav')
    if os.path.exists(wav_filename): 
        print(f"WAV file already exists! {wav_filename}")
        # exit(1)
    else:
        track = AudioSegment.from_file(audio_filename, format='m4a')
        file_handle = track.export(wav_filename, format='wav')
    audio_filename = wav_filename
elif 'mp4' in audio_filename:
    if log: print("Converting mp4 audio file to wav file format ...")
    import subprocess
    wav_filename = audio_filename.replace('mp4', 'wav')
    if os.path.exists(wav_filename):
        print(f"WAV file already exists! {wav_filename}")
    else:
        track = AudioSegment.from_file(audio_filename, format='mp4')
        file_handle = track.export(wav_filename, format='wav')
      # command = "ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {}".format(audio_filename, wav_filename)
      # subprocess.call(command, shell=True)
    audio_filename = wav_filename
#if os.path.exists(wav_filename): 
#        print(f"WAV file already exists! {wav_filename}")
#       audio_filename = wav_filename
#       # exit(1)
#   else:
#       file_handle = track.export(wav_filename, format='wav')
#       audio_filename = wav_filename

audio_file = sr.AudioFile(audio_filename)

with audio_file as source:
    # r.adjust_for_ambient_noise(source)
    duration_period = 200
    cur_time = 600
    while True:
        audio = r.record(source, offset = cur_time, duration = duration_period)
        cur_time += duration_period
        print(r.recognize_google(audio, language = "en-US"))


