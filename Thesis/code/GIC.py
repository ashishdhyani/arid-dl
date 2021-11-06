import cv2
import numpy as np
import os

class GIC:
    def __init__(self, frame):
        self.frame = frame
        self.init_gamma_table(gamma=10)

    def init_gamma_table(self):
        invGamma = 1.0 / gamma
        LU_table = np.array([((i / 255.0) ** invGamma) * 255
                             for i in np.arange(0, 256)]).astype("uint8")

    def illuminate(self, beta=0.9):
        new_frame = cv2.LUT(self.frame, LU_table)
        return new_frame