import cv2

def main():
    image = cv2.imread('passphoto.jpeg')

    blurred_image=cv2.GaussianBlur(image, (85,85), 0)
    cv2.imwrite('passphoto-blurred.jpeg', blurred_image)

if __name__ == "__main__":
    main()