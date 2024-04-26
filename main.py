import cv2, numpy, os


datasets="datasets"
subdata="Juan"
face="haarcascade_frontalface_default.xml"

path=os.path.join(datasets,subdata)

facedetect=cv2.CascadeClassifier(face)

webcam=cv2.VideoCapture(0)

width,height=130,100

count=1

while count<30:
    ret, frame=webcam.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=facedetect.detectMultiScale(grey,1.3,4)
    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        person=grey[y:y+h,x:x+w]
        person_resize=cv2.resize(person,(width,height))
        cv2.imwrite("% s/% s.png" % (path,count),person)
    
    count+=1




    cv2.imshow("webcam",frame)
    k=cv2.waitKey(10)
    if k==27:
        break

