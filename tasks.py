from celery import Celery
from PIL import Image

app = Celery('tasks', broker='amqp://localhost')

@app.task
def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img_resized = img.resize((width, height))
    img_resized.save(f'resized_{image_path}')
