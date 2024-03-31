import cv2
from pyzbar.pyzbar import decode

def read_qr_code_from_camera():
    # Open camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read frame from camera
        ret, frame = cap.read()

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Decode QR codes
        decoded_objects = decode(gray_frame)

        # Display frame with detected QR codes
        cv2.imshow('QR Code Scanner', frame)

        # Check if any QR code is found
        if decoded_objects:
            for obj in decoded_objects:
                # Print QR code data
                print('Type:', obj.type)
                print('Data:', obj.data.decode('utf-8'))

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    read_qr_code_from_camera()
