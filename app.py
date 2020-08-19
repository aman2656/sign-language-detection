from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np
#from keras.models import load_model

model = load_model('CNNmodel.h5')

root = Toplevel()
root.title("sign language detection")
root.configure(bg='black')

img = Image.open("asl.jpg")

img = img.resize((400, 400), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
i=-1

lbl1 = Label(root, text="Sign Language", bg="black", fg="white", font="none 24 bold", anchor=CENTER,)
lbl1.pack()


panel = Label(root, image=img)
root.geometry('600x600') 
panel.pack()

top, right, bottom, left = 10, 300, 400, 590
color = (255, 0, 0) 
thickness = 2

flag = 0
def open_webcam():
        img = cv2.imread("black.jpg")
        cap = cv2.VideoCapture(0)
        j=0
        while True:
            global flag
            global i
            _, image = cap.read() 
            image = cv2.rectangle(image, (left, top), (right, bottom), color, thickness) 
            cv2.imshow("image", image)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                roi =  image[top:bottom, right:left]
                cv2.imshow("crop", roi)
                i=i+1
                
                # preprocessing of an image
                image_grayscale = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                image_grayscale_blurred = cv2.GaussianBlur(image_grayscale, (15,15), 0)
                im3 = cv2.resize(image_grayscale_blurred, (28,28), interpolation = cv2.INTER_AREA)
                im4 = np.resize(im3, (28, 28, 1))
                im5 = np.expand_dims(im4, axis=0)

                # Model Predicion
                pred_probab = model.predict(im5)[0]
                print("predicted probabability of all alphabets are: ", pred_probab)

                #finding the character with the maximum probability
                pred_class = list(pred_probab).index(max(pred_probab))

                # Finding the corresponding ASCII character
                pred_character = chr(pred_class+ 65)
                print("predicted character is: ", pred_character)


                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, pred_character, (20+j, 20), font, 1, (255,255,255), 2, cv2.LINE_AA)
                cv2.imshow("img", img)
                j=j+20  
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                flag = 1
                break 
    
lbl2 = Label(root, text="click here to open Webcam", fg="white", bg="black", font="none 24 bold", anchor=CENTER, pady = 10)    
lbl2.pack()    
button = Button(root, text ="Webcam", command = open_webcam)
button.pack()


root.mainloop()