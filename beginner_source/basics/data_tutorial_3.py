"""
`Learn the Basics <intro.html>`_ ||
`Quickstart <quickstart_tutorial.html>`_ ||
`Tensors <tensorqs_tutorial.html>`_ ||
**Datasets & DataLoaders** ||
`Transforms <transforms_tutorial.html>`_ ||
`Build Model <buildmodel_tutorial.html>`_ ||
`Autograd <autogradqs_tutorial.html>`_ ||
`Optimization <optimization_tutorial.html>`_ ||
`Save & Load Model <saveloadrun_tutorial.html>`_

Datasets & DataLoaders
======================

"""

#################################################################
# Code for processing data samples can get messy and hard to maintain; we ideally want our dataset code
# to be decoupled from our model training code for better readability and modularity.
# PyTorch provides two data primitives: ``torch.utils.data.DataLoader`` and ``torch.utils.data.Dataset``
# that allow you to use pre-loaded datasets as well as your own data.
# ``Dataset`` stores the samples and their corresponding labels, and ``DataLoader`` wraps an iterable around
# the ``Dataset`` to enable easy access to the samples.
#
# PyTorch domain libraries provide a number of pre-loaded datasets (such as FashionMNIST) that
# subclass ``torch.utils.data.Dataset`` and implement functions specific to the particular data.
# They can be used to prototype and benchmark your model. You can find them
# here: `Image Datasets <https://pytorch.org/vision/stable/datasets.html>`_,
# `Text Datasets  <https://pytorch.org/text/stable/datasets.html>`_, and
# `Audio Datasets <https://pytorch.org/audio/stable/datasets.html>`_
#

############################################################
# Loading a Dataset
# -------------------
#
# Here is an example of how to load the `Fashion-MNIST <https://research.zalando.com/project/fashion_mnist/fashion_mnist/>`_ dataset from TorchVision.
# Fashion-MNIST is a dataset of Zalando’s article images consisting of 60,000 training examples and 10,000 test examples.
# Each example comprises a 28×28 grayscale image and an associated label from one of 10 classes.
#
# We load the `FashionMNIST Dataset <https://pytorch.org/vision/stable/datasets.html#fashion-mnist>`_ with the following parameters:
#  - ``root`` is the path where the train/test data is stored,
#  - ``train`` specifies training or test dataset,
#  - ``download=True`` downloads the data from the internet if it's not available at ``root``.
#  - ``transform`` and ``target_transform`` specify the feature and label transformations


import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt


training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)


#################################################################
# Iterating and Visualizing the Dataset
# -------------------------------------
#
# We can index ``Datasets`` manually like a list: ``training_data[index]``.
# We use ``matplotlib`` to visualize some samples in our training data.

labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()

#################################################################
# ..
#  .. figure:: /_static/img/basics/fashion_mnist.png
#    :alt: fashion_mnist


######################################################################
# --------------
#

#################################################################
# Creating a Custom Dataset for your files
# ---------------------------------------------------
#
# A custom Dataset class must implement three functions: `__init__`, `__len__`, and `__getitem__`.
# Take a look at this implementation; the FashionMNIST images are stored
# in a directory ``img_dir``, and their labels are stored separately in a CSV file ``annotations_file``.
#
# In the next sections, we'll break down what's happening in each of these functions.


import os
import pandas as pd
from torchvision.io import read_image

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
