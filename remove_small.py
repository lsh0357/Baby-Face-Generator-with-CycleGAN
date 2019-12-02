import glob, os, shutil
from PIL import Image

def main():
    for filename in glob.iglob('/Users/shihaoli/Downloads/old2young-cropped/trainB/**', recursive=True):
        if os.path.isfile(filename): # filter dirs
            with Image.open(filename) as im:
                x, y = im.size
            if x < 180 or y < 180:
                shutil.move(filename, "/Users/shihaoli/Downloads/old2young-cropped/small-images-B")

if __name__ == "__main__":
    main()