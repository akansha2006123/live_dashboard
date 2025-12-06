import cv2
import numpy as np

def apply_heatmap(frame,points):
    heatmap=np.zeros((frame.shape[0],frame.shape[1]),dtype=np.float32)
    for(x,y)in points:
        cv2.circle(heatmap,(x,y),40,1,-1)
    heatmap =cv2.GaussianBlur(heatmap,(51,51),0)
    heatmap=np.uint8(255*heatmap/np.max(heatmap))

    heatmap_img = cv2.applyColorMap(heatmap,cv2.COLORMAP_JET)    
    overlay = cv2.addWeighted(frame,0.6,heatmap_img,0.4,0)

    return overlay