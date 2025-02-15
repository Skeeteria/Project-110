# import the opencv library
import cv2
import numpy as num

# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):

    check,frame = video.read()
    img = cv2.resize(frame,(224,224))

    test_image = np.array(img, dtype=np.float32)
    test_image = np.expand_dims(test_image, axis=0)

    normalised_image = test_image/255.0

    prediction = model.predict(normalised_image)

    print("Prediction : ", prediction)

    cv2.imshow("Result", frame)
    
    key = cv2.waitKey(1)

    if key == 32:
        print("closing")
        break

    video.release()
      
    # Capture the video frame by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # Quit window with spacebar
    key = cv2.waitKey(1)
    
    if key == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()