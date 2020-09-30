from gtts import gTTS
import pyglet
import time, os

#Speak function tts = text to speech
def tts(text, lang):
    #text : The text you want to be spoken
    #lang : the language you want the text to be spoken
    file = gTTS(text = text, lang = lang)
    filename = '/tmp/temp.mp3'
    file.save(filename)

    music = pyglet.media.load(filename, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)
