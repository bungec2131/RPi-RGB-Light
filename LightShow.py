import pigpio
import numpy as np
import pyaudio
import audioop
import Color
import struct
import random

class LightShow:
    def __init__(self, redPin, greenPin, bluePin):
        self.RED_PIN = redPin
        self.GREEN_PIN = greenPin
        self.BLUE_PIN = bluePin
        
        #color values
        self.r = 0
        self.g = 0
        self.b = 0
        self.brightness = 1
        
        #set data storage values
        self.memSize = 5000
        self.rms = [] 
        self.means = []  
        self.counter = 0
        for i in range(self.memSize):
            self.rms.append(random.randint(1,5000))
            #self.rms.append(i)
        for i in range(self.memSize):
            self.means.append(random.randint(1,5000))
            #self.means.append(i)
            
            
        
        
        #initialize imported objects
        self.pi = pigpio.pi()
        self.displayColor = Color.Color()
    
    
    #takes in raw audio data
    def setLights(self, data, CHUNK):
        #Do heavy lifting
        data_int = struct.unpack(str(2*CHUNK) + 'B', data)
        data_fft = np.abs(np.fft.fft(data_int)) / (128 * CHUNK)
        rmsValue = audioop.rms(data, 2)
        threshold = np.sum(data_fft) / 2
        temp = 0
        index = 0
        while (temp < threshold):
            temp += data_fft[index]
            index += 1
        #Store data from calculations
        self.means[self.counter%self.memSize] = index
        self.rms[self.counter%self.memSize] = rmsValue
        rmsDivisor = (np.mean(self.rms) + np.max(self.rms)) / 2
        
        #Calculate values
        self.brightness = (rmsValue / rmsDivisor) ** 2
        self.means.sort()
        position = self.means.index(index)
        
        #set rgb values
        self.displayColor.set(position / self.memSize)
        rgb = self.displayColor.get()
        self.r = rgb[0] * self.brightness
        self.g = rgb[1] * self.brightness
        self.b = rgb[2] * self.brightness
        if (self.b > 255):
            self.b = 255
        if (self.g > 255):
            self.g = 255
        if (self.r > 255):
            self.r = 255
            
        #print(self.r, self.g, self.b)
        #for i in range(100):
            #print(self.means[i]),
        #print(rmsValue)
        
        #set pins
        self.pi.set_PWM_dutycycle(self.RED_PIN, self.r)
        self.pi.set_PWM_dutycycle(self.GREEN_PIN, self.g)
        self.pi.set_PWM_dutycycle(self.BLUE_PIN, self.b)
        
        #increment
        self.counter += 1
        
    def musicOff(self):
        self.pi.set_PWM_dutycycle(self.RED_PIN, 255)
        self.pi.set_PWM_dutycycle(self.GREEN_PIN, 0)
        self.pi.set_PWM_dutycycle(self.BLUE_PIN, 0)
        
        
