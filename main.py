API_KEY = "Fill your API key here"

'''Steps to get your API_key:-
    -Go to the OpenAI website and sign up for an account or log in if you already have one.
    -Navigate to the API section in your account dashboard to access API keys.
    -Click on the option to create a new API key. Label it appropriately for your project.
    -Copy the generated API key. Keep it secure and do not share it publicly.
    -Integrate the API key into your code to authenticate and make requests to OpenAI's API. Ensure it is stored securely.
    '''

import openai
import requests
from PIL import Image

def getImage():
    openai.api_key = API_KEY
    response = openai.Image.create(
        prompt = input("Which image you want to gen"),
        n=1,
        size="1024x1024"
    )

    image_url= response['data'][0]['url']
    return image_url

img_url= getImage()
res= requests.get(img_url)

with open("image.png", "wb") as image:
    image.write(res.content)

img = Image.open("image.png")
image.show()

