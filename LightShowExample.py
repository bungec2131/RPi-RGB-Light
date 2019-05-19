import pyaudio
import LightShow

#audio setup
CHUNK = 512 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
DEVICE_INDEX = 2

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=DEVICE_INDEX)
stream.stop_stream()

lights = LightShow.LightShow(21, 26,19)



#loop for lights
while (True):
    if stream.is_stopped():
        stream.start_stream()
    #create fft data
    data = stream.read(CHUNK)
    stream.stop_stream()
    lights.setLights(data, CHUNK)
    
    
