import cv2 
import matplotlib.pyplot as plt


image = cv2.imread('images.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
plt.imshow(image_rgb)
plt.title("RGB IMAGE")
plt.show()


image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray)
plt.title("GRAYSCALE")
plt.show()


cropped_image = image[100:300 , 200:400]
cropped_rgb = cv2.cvtColor(cropped_image , cv2.COLOR_BGR2RGB)
plt.imshow(cropped_image)
plt.title("CROPPED")
plt.show()