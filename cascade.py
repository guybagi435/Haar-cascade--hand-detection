import os
import sys
import cv2
import keyboard
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
a=0
cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hand_cascade=cv2.CascadeClassifier(resource_path('palm.xml'))
    fist_cascade=cv2.CascadeClassifier(resource_path('fist.xml'))
    fist=fist_cascade.detectMultiScale(gray,1.3,3)
    hands = hand_cascade.detectMultiScale(gray, 1.3, 3)
    if len(fist)!=0:
        keyboard.press("down")
    elif len(hands)!=0:
        keyboard.press("up")
    else:
        pass

   # for (x, y, w, h) in hands:
    #    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
     #   cv2.putText(frame,"palm",org=(00, 185),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(150, 0, ),thickness=2)
    #for (x, y, w, h) in fist:
     #   frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #    cv2.putText(frame,"fist",org=(00, 185),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(150, 0, ),thickness=2)
    #cv2.putText(mask,a,org=(00, 185),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(150, 0, ),thickness=2)
    #cv2.imshow('frame', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
