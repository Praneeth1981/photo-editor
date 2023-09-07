from PIL import Image, ImageEnhance, ImageFilter
import os

print("-------------------------------------------------------------------")
print("--------------------- Welcome Photo Editor ------------------------")
print("You can change the Contrast, Brightness and Saturation of the image")
print("-------------------------------------------------------------------")

path = './pics_py'
pathOut = './edited_pics_py'

if not os.path.exists(pathOut):
    os.makedirs(pathOut)

try:

    contrast_factor = float(input("Enter the CONTRAST increase factor (ex: 1.0, 1.5): "))
    brightness_factor = float(input("Enter the BRIGHTNESS increase factor (ex: 1.0, 1.5): "))
    saturation_factor = float(input("Enter the SATURATION increase factor (ex: 1.0, 1.5): "))
    rotation_angle_input = input("Enter the ROTATION-ANGLE in degrees (e.g.,empty for no change, 90 for right, -90 for left): ")

    if rotation_angle_input.strip():
        rotation_angle=float(rotation_angle_input)
    else:
        rotation_angle=0.0

    for filename in os.listdir(path):
        img = Image.open(os.path.join(path, filename))
        edit = img.filter(ImageFilter.SHARPEN)

        enhancer_contrast=ImageEnhance.Contrast(edit)
        edit= enhancer_contrast.enhance(contrast_factor)

        enhancer_brightness=ImageEnhance.Brightness(edit)
        edit=enhancer_brightness.enhance(brightness_factor)

        enhancer_saturation=ImageEnhance.Color(edit)
        edit= enhancer_saturation.enhance(saturation_factor)

        if rotation_angle!=0:
            edit=edit.rotate(rotation_angle,expand=True)

        clean_name = os.path.splitext(filename)[0]
        edit.save(os.path.join(pathOut, f'{clean_name}_edited.jpg'))

    print("Edit Success! Edited image is saved in your pathout directory.")

except ValueError as e:
    print("Error : Invalid Input. Please enter valid decimals and rotation angle.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
