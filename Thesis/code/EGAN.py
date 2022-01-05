import cv2
import numpy as np
import os


class EGAN:
    def __init__(self, frame):
		self.frame = frame
        initialize()
    
    def initialize():
        print("initialized")
    
    def illuminate():
	
		input = 'models/EGAN/test_dataset/testA/predict.png'
		output = 'models/EGAN/test_dataset/testB/predict.png'
		if os.path.isfile(input)
			os.remove(input)
			
		if os.path.isfile(output)
			os.remove(output)

		cv2.imwrite(input, self.frame)
		cv2.waitKey(0)
		
        os.system("python models/EGAN/scripts/script.py --predict");
		
		frame = cv2.imread(output)
		
        return frame

