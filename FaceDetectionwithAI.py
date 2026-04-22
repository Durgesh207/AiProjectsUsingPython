import cv2 # it is for computer vision , cv2 se hum photose / videos ko read kar sakte hai
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # haarcascade_frontalface_default.xml is a pre-trained model for face detection
cam = cv2.VideoCapture(0) # ye vidio capture karne ke liye use hota hai, (0,1,2,3) ye no. of cameras hai
while True:
    _, img = cam.read() # cam se image read karne ke liye
    text = "Normal"
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert the image to grayScale , esse face detection fast hota hai
    faces = haar_cascade.detectMultiScale(grayImg, 1.3, 4) # haar cascade se face detect karne ke liye, 1.3 is the scale factor and 4 is the minNeighbors
    for(x,y,w,h) in faces: # x,y,w,h is the coordinates of the face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # draw a rectangle around the face
        text = "Face is Detected"
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2)
        
    cv2.imshow("FaceDetection", img) # show the image with detected faces
    
    key = cv2.waitKey(10) # wait for 10 ms
    print(key) # print the key pressed
    if key == 27: # if the key is 'Esc' then break the loop
        break
cam.release() # release the camera
cv2.destroyAllWindows() # destroy all the windows