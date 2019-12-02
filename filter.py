import glob, os, shutil

def main():
    testA, testB = 200, 400
    for filename in glob.iglob('/Users/shihaoli/Downloads/face-pics/**', recursive=True):
        if os.path.isfile(filename): # filter dirs
            fn = os.path.basename(filename)
            age = int(fn.split('_')[0])
            if age <= 5:
                if testA > 0:
                    shutil.move(filename, "/Users/shihaoli/Downloads/old2young/testA")
                    testA -= 1
                else:
                    shutil.move(filename, "/Users/shihaoli/Downloads/old2young/trainA")
            elif 25 <= age <= 35:
                if testB > 0:
                    shutil.move(filename, "/Users/shihaoli/Downloads/old2young/testB")
                    testB -= 1
                else:
                    shutil.move(filename, "/Users/shihaoli/Downloads/old2young/trainB")

if __name__ == "__main__":
    main()