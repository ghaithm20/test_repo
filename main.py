from tasks import resize_image


images = ['images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg']

for image in images:
    resize_image.delay(image, 200, 600)
