import cv2 #opencv
import imutils # resize
cam = cv2.VideoCapture(0) #cam id ## 0,1,2,3
firstFrame = None
area = 500
while True:
    _, img = cam.read() # read from the camra,image(_)-placeholder
    text = "Normal"
    img = imutils.resize(img,width = 500) # Resize
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # cvtcolor(convert color) 2 gray scale imag
    gaussianImg = cv2.GaussianBlur(grayImg,(21,21),0) # Smoothened
    if firstFrame is None:
        firstFrame = gaussianImg # capturing the first frame
        continue
    imgDiff = cv2.absdiff(firstFrame,gaussianImg) # abs-absilute diff-diffrence
    threshImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1] # (Source_image, threshold_value , max_value, type) // binery image me sirf 2 values hoti hai 0(black), 255(white)
                                                                   # (THRESH_BINARY = (Pixels > 25 = 225(white),(pixels <= 25 = 0 (black))))
                                                                   # [1] besicaly THRESH_BINARY 2 chize deta hai (o,1) so 0 = return valule & 1 (thrdholded image, final img )
    threshImg = cv2.dilate(threshImg,None,iterations=2) #left over-erotions or diletes , it is use to remove lactose and dark circles of the threshImg
    cnts = cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # make complate contors (RETR = retrive (nikalna lena),EXTERNAL = bahar wala)
    cnts = imutils.grab_contours(cnts) # auter layer finde karta hai
    for c in cnts: # counter list in multiple objects
        if cv2.contourArea(c)<area: # mack full area (ye function ka area(size) nikalta hai)
            continue                # if contourArea(object size < area(500) se less hoga to us obj ko skip karke continue (500 se jyada wale obj pe kam karege))
        (x,y,w,h) = cv2.boundingRect(c)  # buildingRect(c) obje(contour)ke around ractangle banane me value deta hai.g
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4) # obj ke upar rectanngle banega x = top left starting point, y = rect top vertical starting point , x = width, h = highht ,, B = 0, G= 0, R=255 => red rectangle ka
        text = "Moving Object detected"                 # 5 ractangle ke lines ki thikness hai (-1,1,3,5)
        #priint(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2) # x=10 left se 10 pixel, y =20 top se 20 pixel , FONT_HERSHRY_SIMPLEX(Text ka font size style hai) , 1 -> normal,font size scale 
    cv2.imshow("cameraFeed",img) # imshow (ye screen per window open karta hai) , cameraFeed = window nam , img = image/ frame jo show karna hai (it means camra ka live video show ho raha hai)
    key = cv2.waitKey(10)  # ye 10 milisecond wait karta hai,our chack karta hai koi key press hui ya nahi,, bina waitkey ke window properly kam nahi karti
    if key == ord("q"): # ord("q") ASCII value of 'q' (it means if user ne q key press ki to break ho jayega or camera band ho jayega)
        break
cam.release()
cv2.destroyAllWindows()
 # Flow:
#Capture video from webcam.
#Resize frame.
#Convert frame to grayscale.
#Blur image to reduce noise.
#Save first frame as background.
#Compare current frame with first frame.
#Convert difference into binary image.
#Dilate white regions to fill gaps.
#Find contours.
#If contour area is bigger than 500, mark it as moving object. 