class Color:
    def __init__(self):
        #set position in the spectrum 
        self.spectrumIndex = 0
        
        #initialize the spectum
        self.size = 1536
        self.spectrum = []
        for i in range(self.size):
            self.spectrum.append([])
        #create red values
        for i in range(256):
            self.spectrum[i].append(255 - i)
        for i in range(256, 512):
            self.spectrum[i].append(0)
        for i in range(512, 768):
            self.spectrum[i].append(0)
        for i in range(768, 1024):
            self.spectrum[i].append(i - 768)
        for i in range(1024, 1280):
            self.spectrum[i].append(255)
        for i in range(1280, 1536):
            self.spectrum[i].append(255)
        #create green values
        for i in range(256):
            self.spectrum[i].append(0)
        for i in range(256, 512):
            self.spectrum[i].append(i - 256)
        for i in range(512, 768):
            self.spectrum[i].append(255)
        for i in range(768, 1024):
            self.spectrum[i].append(255)
        for i in range(1024, 1280):
            self.spectrum[i].append(1279 - i)
        for i in range(1280, 1536):
            self.spectrum[i].append(0)
        #create blue values
        for i in range(256):
            self.spectrum[i].append(255)
        for i in range(256, 512):
            self.spectrum[i].append(255)
        for i in range(512, 768):
            self.spectrum[i].append(767 - i)
        for i in range(768, 1024):
            self.spectrum[i].append(0)
        for i in range(1024, 1280):
            self.spectrum[i].append(0)
        for i in range(1280, 1536):
            self.spectrum[i].append(i - 1280)
            
        
    def increment(self, num):
        if (type(num) != int):
            return
        self.spectrumIndex += num
    
    def set(self, input):
        if (input >= 0 and input < 1):
            self.spectrumIndex = round(input * self.size)
        return
            
    
    def get(self):
        return self.spectrum[int(self.spectrumIndex%self.size)]
            
        
                