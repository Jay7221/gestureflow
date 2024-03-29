import cv2

class Runner:
    def __init__(self) -> None:
        pass

    def loop(self, tracker):
        cap = cv2.VideoCapture(0)  # Use 0 for default camera, or specify the camera index
        while cap.isOpened():
            # Read a frame from the live stream
            ret, frame = cap.read()
            if not ret:
                break

            # Flip the image 
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            tracker.run(frame)

            if cv2.waitKey(1) and 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()



