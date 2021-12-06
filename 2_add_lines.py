import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

orange = (0, 140, 255)

coorx = [0] * 21
coory = [0] * 21

wrist = thumb_tip = index_mcp = index_tip = midle_mcp = midle_tip = ring_tip = pinky_tip = (0,0)

def moveData():
    global wrist
    global thumb_tip
    global index_mcp
    global index_tip
    global midle_mcp
    global midle_tip
    global ring_tip
    global pinky_tip
    wrist = coorx[0],coory[0]
    thumb_tip = coorx[4],coory[4]
    index_mcp = coorx[5],coory[5]
    index_tip = coorx[8],coory[8]
    midle_mcp = coorx[9],coory[9]
    midle_tip = coorx[12],coory[12]
    ring_tip = coorx[16],coory[16]
    pinky_tip = coorx[20],coory[20]

def shiningLine(back_img, coor1, coor2, color, size):
    #draw dot
    cv2.circle(img, coor1, size+1, color, cv2.FILLED)
    cv2.circle(img, coor2, size+1, color, cv2.FILLED)
    #draw color line
    cv2.line(back_img, coor1, coor2, color, size)       
    #draw white line
    cv2.line(back_img, coor1, coor2, (255, 255, 255), round(size/2))

def drawLine():
    #draw line
    shiningLine(img, thumb_tip, index_tip, orange, 2)
    shiningLine(img, thumb_tip, midle_tip, orange, 2)
    shiningLine(img, thumb_tip, ring_tip, orange, 2)
    shiningLine(img, thumb_tip, pinky_tip, orange, 2)

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                # coorx, coory = int(lm.x * w), int(lm.y * h)
                # cv2.circle(img, (coorx,coory), 6, (0,255,0), cv2.FILLED)
                coorx[id], coory[id] = int(lm.x * w), int(lm.y * h)
     
            moveData()
            drawLine()
     
            # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)