from PIL import Image, ImageDraw, ImageFont
import random
import time
import os
random.seed(time.time())

# References - 
# https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
# It might not be perfect (not really random, etc)
# A small starting point at least
# https://stackoverflow.com/questions/64185819/pillow-draw-text-on-image-clear-between-iterations-python
# Clearing text when we are "randomly creating"

# Start big, resize using this code
# https://stackoverflow.com/questions/42516212/how-to-save-a-resized-image-in-python
def resize_img(img, new_w):
    new_img = img.resize((new_w, new_w),)
    # new_img = img.resize((new_w, new_w), Image.ANTIALIAS)
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
        for _ in range(min(randomAmount, 100)): # Capped randomAmount to 100 to prevent too many images, can change if you want
            # from https://stackoverflow.com/questions/64185819/pillow-draw-text-on-image-clear-between-iterations-python
            # to avoid overlap
            clear_im = image.copy()
            draw = ImageDraw.Draw(clear_im)
            # Adjusting randomness to be more close to the center
            # r_x, r_y = random.random() * (W - text_w), random.random() * (H - text_h) OLD CODE
            # Adjust the randint values depending on how far away you want it from the center, since current size is 250
            # 25 is 10% of it, but can be adjusted even smaller if needed
            r_x, r_y = (W-text_w)/2 + random.randint(-25, 25), (H-text_h)/2 + random.randint(-25, 25)
            draw.text((r_x, r_y), message, font=font, fill=fontColor)
            clear_im = resize_img(clear_im, 96)
            save_path = f'res/id{message}/photo_{random.randint(100 * num, 100 * (num + 1))}_{random.randint(0, 10000000)}.png'
            clear_im.save(save_path, "PNG")
    else:
        # Generate a single image with the text in the "middle"
        draw.text(((W-text_w)/2, (H-text_h)/2), message, font=font, fill=fontColor)
        save_path = f'res/id{message}/photo_{random.randint(100 * num, 100 * (num + 1))}_{random.randint(0, 10000000)}.png'
        image.save(save_path, "PNG")
    
    return

def run_image_generator(font, font_color, amount):
    # General code to loop and run the image generation
    msg = "123456789"
    for each_num in msg:
        image_generate(each_num, font, font_color , createRandomLoc = True, randomAmount = amount)

def prepareResultDirs():
    result_dir = "./res"
    os.makedirs(result_dir, exist_ok=True)
    for dir in "123456789":
        dir_name = f'{result_dir}/id{dir}'
        os.makedirs(dir_name, exist_ok=True)

if __name__ == "__main__":
    fontsFiles = []
    directory_path = "./fonts"
    
    all_entries = os.listdir(directory_path)

    for entry in all_entries:
        full_path = os.path.join(directory_path, entry)
        if os.path.isfile(full_path):
            if full_path.endswith(".ttf") or full_path.endswith(".otf"):
                fontsFiles.append(full_path)
    
    prepareResultDirs()

    for font in fontsFiles:
        sizeUsed = set()
        for i in range(10):
            size = random.randint(180, 250)

            while size in sizeUsed :
                size = random.randint(180, 250)

            sizeUsed.add(size)
            print("Font:", font, "with size", size)
            font_to_use = ImageFont.truetype(font, size)
            font_color = 'black'
            run_image_generator(font_to_use, font_color, amount = 10)
