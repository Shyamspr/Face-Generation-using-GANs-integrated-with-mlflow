# Face Generation
Face Generation using DCGAN on celebA dataset using Tensorflow 2.0

## Dataset Link
http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html

## Getting Started
I will be using the Deep Convolution Generative Adversarial Network(DC-GAN) for this task. <br>
I am using CelebA dataset for training the network. This dataset contains 2,00,000 images of well-known people.

### Prerequisites
All the dependencies for the environment in which the model was trained has been provided in conda.yaml file.<br>
MLflow takes care of the environment creation.<br>
Alternately you can use ``` conda env create -f conda.yaml ``` to create the virtual environment to run this code.

- `GAN.py` contains the main DCGAN code.
- `MLProject` specifies entry point and environment to be created.
- `Run.py` would start training with default parameters.
- `conda.yaml` contains all the dependencies to run the DCGAN code.
- `helper.py` is a python file to download, align and preprocess the images from the dataset.
<br>

## Deployment
Training model based on following parameters:
<br>
* learning_rate=0.0001
* epochs=150
* noise_dim=100 
* num_examples_to_generate=16
* buffer_size=202599
* batch_size=256
<br>
Given above are the default values of the hyperparameters.

To run use the following command:
```
!mlflow run . -e GAN.py -P learning_rate=0.0001 -P epochs=10 -P noise_dim=100 -P num_examples_to_generate=16 -P buffer_size=202599 -P batch_size=256
```
## Future Prospects
Integration with Neptune.ml for organization and collaboration in a beautiful hosted UI that Neptune gives you.

