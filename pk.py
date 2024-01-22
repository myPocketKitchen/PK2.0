from openai import OpenAI
import base64
from PIL import Image
import io
import os 
from dotenv import load_dotenv
import subprocess

load_dotenv()
client = OpenAI()

path = "/home/pk/PK2.0/photo.jpg"


def take_photo():
    photo_path = "/home/pk/PK2.0/photo.jpg"
    # Command to take a photo with libcamera-still
    command = ['libcamera-still', '-o', photo_path]

    # Run the command
    subprocess.run(command)

    print(f"Photo taken and saved to {photo_path}")


def process_image(image_path):
  # Resize the image
  fridge_pic = Image.open(image_path)
  image_size = fridge_pic.size
  fridge_pic.resize((image_size[0] // 5, image_size[1] // 5)).save("mini_photo.jpg", optimize=True, quality=95)
  # mini_pic = Image.open("mini_photo.jpg")

  # print(f"Image resized to {mini_pic.size}")

  # Function to encode image to base64
  def encode_image_to_base64(image_path):
    with Image.open(image_path) as image:
      buffered = io.BytesIO()
      image.save(buffered, format="JPEG")
      return base64.b64encode(buffered.getvalue()).decode()

  # Encode the image
  encoded_image = encode_image_to_base64("mini_photo.jpg")

  response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "You are an expert in identifying items of food from images of the inside of a fridge. List the food items in this image and specify the quantity of each and the ripeness / state of decay, if you can. Tupperware containers are usually contain leftovers. Give responses only in the format: 'In your fridge, you have: - [food item]\n - [food item]\n - [food item]'"},
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

  return response.choices[0].message.content

def get_recipes(ingredients):
  response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "You are an expert in coming up with recipes from a list of ingredients. Given a list of ingredients, suggest a recipe that can be made from them. Give responses only in the format 'You could make [recipe suggestion]. Here's the recipe: [recipe for suggestion]'"},
          {
            "type": "text",
            "text": f"{ingredients}",
          },
        ],
      }
    ],
    max_tokens=300,
  )
  return response.choices[0].message.content
