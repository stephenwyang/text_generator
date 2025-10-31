from PIL import Image, ImageDraw, ImageFont
import random
import time
random.seed(time.time())
# Try using PIL?
# https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
# It might not be perfect (not really random, etc)
# A small starting point at least

# https://stackoverflow.com/questions/64185819/pillow-draw-text-on-image-clear-between-iterations-python
# Clearing text when we are "randomly creating"

def image_generate_old(message, font, fontColor, createRandomLoc = False, randomAmount = 0):

    W, H = 250, 250
    size = (W, H)
    image = Image.new('RGB', size, 'white')
    # TODO: First draw the text (any digit) in the middle of the screen
    # Need to either implement a random position here or add start X and Y into another function
    draw = ImageDraw.Draw(image)
    _, _, text_w, text_h = draw.textbbox((0, 0), message, font=font)
    if text_w > W or text_h > H:
        print("Error: Text is exceeding the size of the image. Please make the font size smaller")
        return -1
    draw.text(((W-text_w)/2, (H-text_h)/2), message, font=font, fill=fontColor)
    
    return image

# Start big, resize using this code
# https://stackoverflow.com/questions/42516212/how-to-save-a-resized-image-in-python
def resize_img(img, new_w):
    new_img = img.resize((new_w, new_w), Image.ANTIALIAS)
    return new_img

def image_generate(message, font, fontColor, createRandomLoc = False, randomAmount = 0):

    W, H = 250, 250
    size = (W, H)
    image = Image.new('RGB', size, 'white')
    draw = ImageDraw.Draw(image)
    _, _, text_w, text_h = draw.textbbox((0, 0), message, font=font)
    num = int(message)
    # Error catching
    if text_w > W or text_h > H:
        print("Error: Text is exceeding the size of the image. Please make the font size smaller.")
        return
    if randomAmount <= 0 and createRandomLoc:
        print("Error: Please choose a number greater than 1 to create amounts of.")
        return

    if createRandomLoc:
        for _ in range(min(randomAmount, 100)):
            # from https://stackoverflow.com/questions/64185819/pillow-draw-text-on-image-clear-between-iterations-python
            # to avoid overlap
            clear_im = image.copy()
            
            draw = ImageDraw.Draw(clear_im)
            r_x, r_y = random.random() * (W - text_w), random.random() * (H - text_h)
            draw.text((r_x, r_y), message, font=font, fill=fontColor)
            clear_im = resize_img(clear_im, 96)
            clear_im.save(f'res/id{message}/photo_{random.randint(100 * num, 100 * (num + 1))}_{random.randint(0, 100000)}.png', "PNG")
    
    return

def run_image_generator(font, font_color, amount):
    # General code to loop and run the image generation
    msg = "123456789"
    for each_num in msg:
        image_generate(each_num, font, font_color , createRandomLoc = True, randomAmount = amount)

if __name__ == "__main__":
    font_to_use = ImageFont.truetype('fonts/roboto-12.ttf', 100)
    font_color = 'black'
    run_image_generator(font_to_use, font_color, 10)
    
    """
    message = "1"
    # Get this text or figure out how to access system text for this
    test_font = ImageFont.truetype('fonts/roboto-12.ttf', 100)
    testImage = image_generate(message, test_font, 'black')
    num = 1
    if testImage:
        testImage.save(f'img_dump/photo{num}.png', "PNG")
    """