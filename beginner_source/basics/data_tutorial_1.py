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
