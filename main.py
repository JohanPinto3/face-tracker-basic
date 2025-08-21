import cv2

def main():
    # Load the pre-trained Haar Cascade classifier for face detection
    # This XML file contains the trained features for detecting frontal faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open a connection to the default webcam (0)
    cap = cv2.VideoCapture(0)

    # Check if the webcam was opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # If the frame was not read successfully, break the loop
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale for face detection (improves performance)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        # scaleFactor: Parameter specifying how much the image size is reduced at each image scale
        # minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it
        # minSize: Minimum possible object size. Objects smaller than that are ignored.
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # Green rectangle, thickness 2

        # Display the frame with detected faces
        cv2.imshow('Face Tracking', frame)

        # Exit if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2

def main():
    # Load the pre-trained Haar Cascade classifier for face detection
    # This XML file contains the trained features for detecting frontal faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open a connection to the default webcam (0)
    cap = cv2.VideoCapture(0)

    # Check if the webcam was opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # If the frame was not read successfully, break the loop
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale for face detection (improves performance)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        # scaleFactor: Parameter specifying how much the image size is reduced at each image scale
        # minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it
        # minSize: Minimum possible object size. Objects smaller than that are ignored.
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # Green rectangle, thickness 2

        # Display the frame with detected faces
        cv2.imshow('Face Tracking', frame)

        # Exit if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
