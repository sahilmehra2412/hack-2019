import urllib
import json
import requests
params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': '{string}',
})

api = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?s",+params

header = {
	"Ocp-Apim-Subscription-Key":"a32cb4860bd3403a9cca74deaffc6116",
	"Content-Type":"application/octet-stream"
        }
image = "Mark.jpg"
with open(image, 'rb') as file:
	f = file.read()
	# print(f)
data = {"url":"https://pbs.twimg.com/profile_images/1717956431/BP-headshot-fb-profile-photo_400x400.jpg"}
# data = {"url"}
r = requests.post(api, headers = header, data=f)



# print(dir(r))
print(r.text)