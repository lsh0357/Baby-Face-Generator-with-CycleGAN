import glob, os, shutil

def main():
    trainA, trainB = 900, 1000
    print("here")
    for filename in glob.iglob('/Users/shihaoli/Downloads/old2young/trainB/**', recursive=True):
        if os.path.isfile(filename): # filter dirs
            trainB -= 1
            if trainB < 0:
                shutil.move(filename, "/Users/shihaoli/Downloads/old2young-redundant/trainB")

if __name__ == "__main__":
    main()