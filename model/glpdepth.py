# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 04:08:02 2022

@author: Admin
"""

import torch
from transformers import GLPNForDepthEstimation, GLPNFeatureExtractor

class GLP():
    def __init__(self, pretrained):
        self.feature_extractor =  GLPNFeatureExtractor.from_pretrained(pretrained) # vinvino02/glpn-kitti, vinvino02/glpn-nyu2
        self.model = GLPNForDepthEstimation.from_pretrained(pretrained)
        
        self.model.eval()
        
    def predict(self, img, img_shape):
        with torch.no_grad(): # Depth map
            pixel_values = self.feature_extractor(img, return_tensors="pt").pixel_values
            outputs = self.model(pixel_values) 
            predicted_depth = outputs.predicted_depth
            
            # interpolate to original size
            prediction = torch.nn.functional.interpolate(
                                predicted_depth.unsqueeze(1),
                                size=img_shape[:2],
                                mode="bicubic",
                                align_corners=False,
                         )
            prediction = prediction.squeeze().cpu().numpy() # shape => (375, 1242)
        
        return prediction