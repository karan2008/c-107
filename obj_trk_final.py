import cv2
import sys

# Initialize the tracker (you can use any tracking algorithm here)
tracker = cv2.TrackerCSRT_create()

# Initialize the video capture
video_capture = cv2.VideoCapture('video.mp4')  # Replace 'video.mp4' with your video file path

# Read the first frame from the video
success, frame = video_capture.read()

# Initialize the bounding box (x, y, w, h)
bbox = cv2.selectROI("Select Object to Track", frame, False)
tracker.init(frame, bbox)

def drawBox(img, bbox):
    # Extract the coordinates and dimensions of the bounding box
    x, y, w, h = [int(i) for i in bbox]
    
    # Draw a rectangle around the tracked object
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Add tracking text
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

while True:
    # Read the next frame from the video
    success, img = video_capture.read()
    
    # Update the tracker
    success, bbox = tracker.update(img)
    
    if success:
        # If tracking is successful, draw the bounding box
        drawBox(img, bbox)
    else:
        # If tracking is lost, display "LOST" text
        cv2.putText(img, "LOST", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # Display the image
    cv2.imshow("Object Tracking", img)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
