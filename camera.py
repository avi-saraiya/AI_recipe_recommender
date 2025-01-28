import cv2

def capture_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return None

    print("Press 'c' to capture an image, or 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow("Camera Feed", frame)

        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("c"):
            image_path = "captured_image.jpg"
            cv2.imwrite(image_path, frame)
            print(f"Image captured and saved as {image_path}")
            break
        elif key == ord("q"):
            print("Exiting camera capture.")
            break

    cap.release()
    cv2.destroyAllWindows()

    return image_path
