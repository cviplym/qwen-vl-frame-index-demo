import numpy as np
from PIL import Image
import cv2
import math

def create_image_grid(images, num_columns=8):
    # images(경로) -> pil image
    pil_images = [Image.fromarray(cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)) for image in images]
    num_rows = math.ceil(len(images) / num_columns)

    img_width, img_height = pil_images[0].size
    grid_width = num_columns * img_width
    grid_height = num_rows * img_height
    grid_image = Image.new('RGB', (grid_width, grid_height))

    for idx, image in enumerate(pil_images):
        row_idx = idx // num_columns
        col_idx = idx % num_columns
        position = (col_idx * img_width, row_idx * img_height)
        grid_image.paste(image, position)

    return grid_image