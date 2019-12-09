# Baby-Face-Generator-with-CycleGAN

## Contribution

This repo is heavily based on [**Original CycleGAN implementation**](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). Most of our work involves adding code to better handle the dataset we are working with.

## Prerequisites
- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

## Getting Started
### Installation

- Clone this repo:
```bash
git clone https://github.com/lsh0357/Baby-Face-Generator-with-CycleGAN.git
cd Baby-Face-Generator-with-CycleGAN
```

- Install [PyTorch](http://pytorch.org and) 0.4+ and other dependencies (e.g., torchvision, [visdom](https://github.com/facebookresearch/visdom) and [dominate](https://github.com/Knio/dominate)).
  - For pip users, please type the command `pip install -r requirements.txt`.

### Play with your own images!

- If you would like to try the model with 2 or more input images, you could use http://www.morphthing.com/morph to morph your images, else if only one image as input, look into the next step.
- The model is restricted to face only images, so please follow https://github.com/kb22/Create-Face-Data-from-Images to extract face from images or use any other tool to clean up the background noisies.
- The trained model is saved at ./trained_model. Move the whole trained_model directory to ./checkpoints
- To generate a baby style face of your input, simply run
```bash
python test.py --dataroot <PATH_TO_TEST_SET> --name trained_model --model test
```
- Look at your baby face at ./results

### CycleGAN train/test
- To view training results and loss plots, run `python -m visdom.server` and click the URL http://localhost:8097.
- Train a model:
```bash
#!./scripts/train_cyclegan.sh
python train.py --dataroot <PATH_TO_TRAINING_SET> --name <NAME_FOR_THE_MODEL> --model cycle_gan
```
To see more intermediate results, check out `./checkpoints/<NAME_FOR_THE_MODEL>`.
- Test the model:
```bash
#!./scripts/test_cyclegan.sh
python test.py --dataroot <PATH_TO_TEST_SET> --name <NAME_FOR_THE_MODEL> --model cycle_gan
python test.py --dataroot <PATH_TO_TEST_SET> --name <NAME_FOR_THE_MODEL> --model test(For one side test, such as only from adult to baby)
```
- The test results will be saved to a html file here: `./results/<NAME_FOR_THE_MODEL>/latest_test/index.html`.

### Apply a pre-trained model (CycleGAN)

- Look at the options directory or the original repo for more information about how to do a pre-train and pther advantage training and testing options.
