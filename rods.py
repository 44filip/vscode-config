class Rod:
    def __init__(self):
        self.quality = 3
        self.max_quality = self.quality

    def fish(self) -> None:
        while self.quality > 0:
            print("Casting reel...")
            self.quality -= 1
        self.quality = self.max_quality
        

class Pro(Rod):
    def __init__(self):
        self.quality = 4
        self.max_quality = self.quality
    
