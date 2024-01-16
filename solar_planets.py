import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun",
            (0,250),
            cv2.FONT_HERSHEY_COMPLEX,
            1.5,
            (255,255,255),
            )
cv2.putText(img,
            "Mercury",
            (120,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (183,110,121),
            )
cv2.putText(img,
            "Venus",
            (195,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (0,255,0),
            )
cv2.putText(img,
            "Earth",
            (290,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (196, 180, 84),
            )
cv2.putText(img,
            "Mars",
            (385,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (150,121,200),
            )
cv2.putText(img,
            "Jupiter",
            (570,380),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (25,300,450),
            )
cv2.putText(img,
            "Saturn",
            (780,330),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (100,75,0),
            )
cv2.putText(img,
            "Uranus",
            (970,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (120,18,80),
            )
cv2.putText(img,
            "Neptune",
            (1120,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (196, 180, 104),
            )

cv2.imwrite("solar-system.jpg" ,img)

cv2.imshow("Solar System" , img)
cv2.waitKey(0)
