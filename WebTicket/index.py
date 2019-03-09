import urllib
import json
import requests

api = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

header = {
	"Ocp-Apim-Subscription-Key":"a32cb4860bd3403a9cca74deaffc6116",
	"Content-Type":"application/octet-stream"
        }
image = "filename.jpg"
with open(image, 'rb') as file:
	f = file.read()
	# print(f)
data = {"url":"https://pbs.twimg.com/profile_images/1717956431/BP-headshot-fb-profile-photo_400x400.jpg"}
# data = {"url"}
r = requests.post(api, headers = header, data=f)

# j = json.loads(r.text)
# print(j[0]['faceId'])
print(r.text)