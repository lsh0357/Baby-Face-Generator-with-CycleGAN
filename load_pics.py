import glob, os, shutil

def main():
    trainB = 400
    skip = 1000
    for filename in glob.iglob('/Users/shihaoli/repo/FaceAging-by-cycleGAN/datasets/young2old/trainA_women/**', recursive=True):
        if skip > 0:
            skip -= 1
            continue
        if os.path.isfile(filename): # filter dirs
            trainB -= 1
            shutil.move(filename, "/Users/shihaoli/Downloads/old2young-cropped/trainB")
            if trainB < 0:
                break
                

if __name__ == "__main__":
    main()