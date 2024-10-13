import cv2
photo = cv2.imread("SNIPERS ROOFF.png")

cv2.imshow("Exibit B",photo)

sp = (0,0)
ep = (300,250)
color = (0,255,0)
thickness = 10

line = cv2.line(photo,sp,ep,color,thickness)
cv2.imshow("Exibit B but with a line", line)
cv2.waitKey(0)
cv2.destroyAllWindows()