import cv2

vcap = cv2.VideoCapture(0)
while(1):
    ret, frame = vcap.read()
    frame = cv2.resize(frame, None, None, fx=1, fy=2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vcap.release()
cv2.destroyAllWindows()
