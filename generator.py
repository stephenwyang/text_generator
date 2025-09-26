from PIL import Image, ImageDraw, ImageFont
# Try using PIL?
# https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
# It might not be perfect (not really random, etc)
# A small starting point at least

# https://stackoverflow.com/questions/64185819/pillow-draw-text-on-image-clear-between-iterations-python
# Clearing text when we are "randomly creating"

def image_generate(message, font, fontColor, createRandom = False, randomAmount = 0):

    W, H = 250, 250
    size = (W, H)
    image = Image.new('RGB', size, 'white')
    # TODO: First draw the text (any digit) in the middle of the screen
    # Need to either implement a random position here or add start X and Y into another function
    
    return

# Start big, resize using this code
# https://stackoverflow.com/questions/42516212/how-to-save-a-resized-image-in-python
def resize_img(img, new_w):
    new_img = img.resize((new_w, new_w), Image.ANTIALIAS)
    return new_img

