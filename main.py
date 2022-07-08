from image_processor import *
from PIL import Image


def main():
    image_to_convert = Image.open("<image file name>")
    processor = ImageProcessor()
    text = processor.image_to_ascii(image_to_convert, 2)
    print(text)


if __name__ == "__main__":
    main()
