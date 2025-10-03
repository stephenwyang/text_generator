from PIL import Image, ImageDraw, ImageFont
# Try using PIL?
# https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
# It might not be perfect (not really random, etc)
# A small starting point at least

# https://stackoverflow.com/questions/64185819/pillow-draw-text-on-image-clear-between-iterations-python
# Clearing text when we are "randomly creating"

def image_generate(message, font, fontColor, createRandomLoc = False, randomAmount = 0):

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

if __name__ == "__main__":
    message = "7"
    test_font = ImageFont.truetype('fonts/roboto-12.ttf', 100)
    testImage = image_generate(message, test_font, 'black')
    if testImage:
        testImage.save('img_dump/photo.png', "PNG")