import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from emotion_movies import emotion_to_movies

# Load the emotion detection model
model = load_model("best_model.h5")

# Load Haar cascade for face detection
face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# List of emotions
emotions = list(emotion_to_movies.keys())

# Start webcam
cap = cv2.VideoCapture(0)

print("Press 'q' to quit...")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray_img[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (224, 224))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)
        max_index = int(np.argmax(predictions))
        predicted_emotion = emotions[max_index]

        # Display predicted emotion
        cv2.putText(frame, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Recommend movies based on emotion
        recommended = emotion_to_movies[predicted_emotion]
        recommendation_text = ", ".join(recommended[:2])  # show top 2
        cv2.putText(frame, f"Try: {recommendation_text}", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    resized_frame = cv2.resize(frame, (1000, 700))
    cv2.imshow("Emotion-Based Movie Recommender", resized_frame)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
