#face and eye detection
from flask import Flask,render_template,Response
# render template -to link html file
import cv2


app=Flask(__name__)
camera=cv2.VideoCapture(0)
# to acccess some remote webcam which is situated somewhere else, we can use its ip address or username password
def generate_frames():
    while True:
      success,frame=camera.read()
      if not success:
          break
      else:
          detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
          eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
         
          gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
          faces=detector.detectMultiScale(gray,1.1,7, minSize=(30, 30))
          #draw rectangle around eac face
          for (x,y,w,h) in faces:
              cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
              roi_gray=gray[y:y+h,x:x+w]
              roi_color=frame[y:y+h,x:x+w]
              eyes=eye_cascade.detectMultiScale(roi_gray,1.1,10, minSize=(10, 10), maxSize=(60, 60))
              for (ex,ey,ew,eh) in eyes:
                  cv2.rectangle(roi_color,(ex,ey),(ex+w,ey+h),(0,255,0),2)
              
          
          ret,buffer=cv2.imencode('.jpg',frame)
          frame=buffer.tobytes()
      yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')
        
@app.route('/')
def ind():
    return render_template('ind.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(debug=True)
    