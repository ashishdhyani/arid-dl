import cv2
import numpy as np
import os

class KIND:
    def __init__(self, frame):
        self.frame = frame
        self.initialize()
    
    def initialize():
        print("initialized")
    
    def illuminate():
		input = 'models/KiND/test/predict.png'
		output = 'models/KiND/results/test/predict.png'
		if os.path.isfile(input)
			os.remove(input)
			
		if os.path.isfile(output)
			os.remove(output)

		cv2.imwrite(input, self.frame)
		cv2.waitKey(0)
		
		os.system("python models/KiND/scripts/evaluate.py");
		
		frame = cv2.imread(output)
		
        return frame

