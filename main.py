from image_processor import *
from PIL import Image


def main():
    image_to_convert = Image.open()
    processor = ImageProcessor(image_to_convert, 5)
    text = processor.image_to_ascii()
    print(text)


if __name__ == "__main__":
    main()
