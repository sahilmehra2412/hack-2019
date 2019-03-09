import requests , json
import cv2
api = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"
url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/verify"
header = {
	"Ocp-Apim-Subscription-Key":"a32cb4860bd3403a9cca74deaffc6116",
	"Content-Type":"application/octet-stream"
	}
headers = {
	"Ocp-Apim-Subscription-Key":"a32cb4860bd3403a9cca74deaffc6116",
	"Content-Type":"application/json"
	}
with open("sample.jpg", "rb") as img:
	f=img.read()
r = requests.post(api, headers=header, data=f)
j = json.loads(r.text)
faceId1 = j[0]['faceId']
print(faceId1)

cam =cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
	_,frame = cam.read()
	faces = face_cascade.detectMultiScale(frame, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
	cv2.imshow('Face', frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cv2.imwrite('Test.jpg', frame[y:y+h,x:x+w])
cam.release()
cv2.destroyAllWindows()

with open("Test.jpg", "rb") as file:
	sh=file.read()
p = requests.post(api, headers=header, data=sh)
jo = json.loads(p.text)

faceId2 = jo[0]['faceId']
print(faceId2)

body = {
	'faceId1':faceId1,
	'faceId2':faceId2,
}

new = requests.post(url, headers=headers, data=json.dumps(body))
facial = json.loads(new.text)
if facial["isIdentical"] == 'false':
	print('Both persons are different. Matching percentage is '+ str(facial["confidence"]*100))
else:
	print('Both persons are same. Matching percentage is '+ str(facial["confidence"]*100))