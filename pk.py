from openai import OpenAI
import base64
from PIL import Image
import io
import os 
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

peppers = Image.open("peppers.jpg")
peppers.resize((216, 216)).save("mini_peppers.jpg", optimize=True, quality=95)

# Function to encode image to base64
def encode_image_to_base64(image_path):
    with Image.open(image_path) as image:
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()

# Encode your image
encoded_image = encode_image_to_base64("mini_peppers.jpg")

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "List the food items in this image"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{encoded_image}",
            },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)
