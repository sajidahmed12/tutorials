#!/bin/bash

DATADIR=/data/tutorialsdata
mkdir -p advanced_source/data
mkdir -p beginner_source/data
mkdir -p intermediate_source/data
mkdir -p prototype_source/data

ZIPOPTS=-qo
TAROPTS=

# transfer learning tutorial data
# wget -nv -N https://download.pytorch.org/tutorial/hymenoptera_data.zip -P $DATADIR
unzip $ZIPOPTS $DATADIR/hymenoptera_data.zip -d beginner_source/data/

# nlp tutorial data
# wget -nv -N https://download.pytorch.org/tutorial/data.zip -P $DATADIR
unzip $ZIPOPTS $DATADIR/data.zip -d intermediate_source/  # This will unzip all files in data.zip to intermediate_source/data/ folder

# data loader tutorial
# wget -nv -N https://download.pytorch.org/tutorial/faces.zip -P $DATADIR
unzip $ZIPOPTS $DATADIR/faces.zip -d beginner_source/data/

# wget -nv -N https://download.pytorch.org/models/tutorials/4000_checkpoint.tar -P $DATADIR
cp $DATADIR/4000_checkpoint.tar beginner_source/data/

# neural style images
rm -rf advanced_source/data/images/ || true
mkdir -p advanced_source/data/images/
cp -r _static/img/neural-style/ advanced_source/data/images/

# Download dataset for beginner_source/dcgan_faces_tutorial.py
# wget -nv -N https://s3.amazonaws.com/pytorch-tutorial-assets/img_align_celeba.zip -P $DATADIR
unzip $ZIPOPTS $DATADIR/img_align_celeba.zip -d beginner_source/data/celeba

# Download dataset for beginner_source/hybrid_frontend/introduction_to_hybrid_frontend_tutorial.py
# wget -nv -N https://s3.amazonaws.com/pytorch-tutorial-assets/iris.data -P $DATADIR
cp $DATADIR/iris.data beginner_source/data/

# Download dataset for beginner_source/chatbot_tutorial.py
# wget -nv -N https://s3.amazonaws.com/pytorch-tutorial-assets/cornell_movie_dialogs_corpus_v2.zip -P $DATADIR
unzip $ZIPOPTS $DATADIR/cornell_movie_dialogs_corpus_v2.zip -d beginner_source/data/

# Download dataset for beginner_source/audio_classifier_tutorial.py
# wget -nv -N https://s3.amazonaws.com/pytorch-tutorial-assets/UrbanSound8K.tar.gz -P $DATADIR
tar $TAROPTS -xzf $DATADIR/UrbanSound8K.tar.gz -C ./beginner_source/data/

# Download model for beginner_source/fgsm_tutorial.py
# wget -nv -N 'https://docs.google.com/uc?export=download&id=1HJV2nUHJqclXQ8flKvcWmjZ-OU5DGatl' -O $DATADIR/lenet_mnist_model.pth
cp $DATADIR/lenet_mnist_model.pth ./beginner_source/data/lenet_mnist_model.pth

# Download model for advanced_source/dynamic_quantization_tutorial.py
# wget -nv -N https://s3.amazonaws.com/pytorch-tutorial-assets/word_language_model_quantize.pth -P $DATADIR
cp $DATADIR/word_language_model_quantize.pth advanced_source/data/word_language_model_quantize.pth

# Download data for advanced_source/dynamic_quantization_tutorial.py
# wget -nv -N https://s3.amazonaws.com/pytorch-tutorial-assets/wikitext-2.zip -P $DATADIR
unzip $ZIPOPTS $DATADIR/wikitext-2.zip -d advanced_source/data/

# Download model for advanced_source/static_quantization_tutorial.py
# wget -nv -N https://download.pytorch.org/models/mobilenet_v2-b0353104.pth -P $DATADIR
cp $DATADIR/mobilenet_v2-b0353104.pth advanced_source/data/mobilenet_pretrained_float.pth


# Download model for prototype_source/graph_mode_static_quantization_tutorial.py
# wget -nv -N https://download.pytorch.org/models/resnet18-5c106cde.pth -P $DATADIR
cp $DATADIR/resnet18-5c106cde.pth prototype_source/data/resnet18_pretrained_float.pth

# Download vocab for beginner_source/flava_finetuning_tutorial.py
# wget -nv -N http://dl.fbaipublicfiles.com/pythia/data/vocab.tar.gz -P $DATADIR
tar $TAROPTS -xzf $DATADIR/vocab.tar.gz -C ./beginner_source/data/

# Download dataset for beginner_source/torchtext_custom_dataset_tutorial.py
# wget -nv -N https://www.manythings.org/anki/deu-eng.zip -P $DATADIR
unzip -o $DATADIR/deu-eng.zip -d beginner_source/data/
